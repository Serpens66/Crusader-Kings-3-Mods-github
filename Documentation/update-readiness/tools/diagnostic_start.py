"""User-invoked CK3 diagnostics; no input automation, installation or mod edits."""
import argparse
import csv
import hashlib
import io
import json
import msvcrt
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
INSTALL = Path(r"E:\ProgrammeE\Steam\steamapps\common\Crusader Kings III")
USER = Path(r"C:\Users\Serpens66\Documents\Paradox Interactive\Crusader Kings III")
CONFIG = USER / "dlc_load.json"
LOGS = USER / "logs"
CRASHES = USER / "crashes"
EXPECTED = "1.20.0.3"
EXPORTS = {"effects.log", "triggers.log", "event_scopes.log", "event_targets.log",
           "modifiers.log", "on_actions.log"}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(data, indent=2, ensure_ascii=False) + "\n").replace("\n", "\r\n")
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(raw.encode("utf-8"))
    os.replace(temporary, path)


def inventory(directory):
    rows = {}
    if directory.exists():
        for path in directory.rglob("*"):
            if not path.is_file() or path.is_symlink():
                continue
            raw = path.read_bytes()
            rows[path.relative_to(directory).as_posix()] = {
                "sha256": digest(raw), "mtime_ns": path.stat().st_mtime_ns,
                "size": len(raw)}
    return rows


def changed(before, after):
    # An unchanged old export must never satisfy a current-build evidence gate.
    return {name: row for name, row in after.items() if before.get(name) != row}


def capture(directory, destination, selected):
    copied = []
    for name, row in selected.items():
        source = directory / name
        raw = source.read_bytes()
        if digest(raw) != row["sha256"] or source.stat().st_mtime_ns != row["mtime_ns"]:
            raise RuntimeError("Log changed while being collected: " + str(source))
        # Raw evidence retains its bytes. This avoids recoding game-written txt/yml.
        target = destination / (name + ".raw")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
        copied.append({"source": str(source), "relative_source": name,
                       "copy": str(target.relative_to(ROOT)), **row})
    return copied


def process_running(image):
    result = subprocess.run(["tasklist.exe", "/FI", "IMAGENAME eq " + image, "/FO", "CSV", "/NH"],
                            capture_output=True, check=True,
                            creationflags=subprocess.CREATE_NO_WINDOW)
    rows = csv.reader(io.StringIO(result.stdout.decode("mbcs", errors="replace")))
    return any(row and row[0].lower() == image.lower() for row in rows)


def ck3_running():
    return process_running("ck3.exe")


def launch_arguments(exe):
    return [str(exe), "-gdpr-compliant", "-debug_mode", "-suppress_error_log"]


def crash_inventory(directory):
    rows = {}
    if not directory.exists():
        return rows
    for folder in directory.iterdir():
        if not folder.is_dir() or folder.is_symlink():
            continue
        # An allowlist avoids reading personal saves, settings and memory dumps.
        allowed = [folder / "exception.txt", folder / "meta.yml"]
        if (folder / "logs").is_dir() and not (folder / "logs").is_symlink():
            allowed += list((folder / "logs").rglob("*.log"))
        for path in allowed:
            if not path.is_file() or path.is_symlink():
                continue
            raw = path.read_bytes()
            rows[path.relative_to(directory).as_posix()] = {
                "sha256": digest(raw), "mtime_ns": path.stat().st_mtime_ns, "size": len(raw)}
    return rows


def profile_warnings(directory, fresh):
    references = set()
    for name in fresh:
        if Path(name).suffix == ".log":
            text = (directory / name).read_bytes().decode("utf-8-sig", errors="replace")
            references.update(re.findall(r"\bagot_[A-Za-z0-9_]+", text))
    if not references:
        return []
    return [{"kind": "existing-profile-rule-references", "references": sorted(references),
             "interpretation": "AGOT references observed in logs; relation to any crash is unknown. "
                               "User profile, settings and saves were not cleaned or deleted."}]


def restore_config(path, original, temporary_hash):
    # Do not overwrite a launcher/user edit made while diagnostics were running.
    if path.exists() and digest(path.read_bytes()) == temporary_hash:
        path.write_bytes(original)
        return True
    if path.exists() and path.read_bytes() == original:
        return True
    return False


def validate_exports(stage, fresh):
    names = {Path(name).name for name in fresh}
    if stage == "script-docs":
        return sorted(EXPORTS - {Path(name).name for name, row in fresh.items() if row["size"] > 0})
    if stage in {"data-types", "main-menu-data-types"}:
        return [] if any(Path(name).parts[0] == "data_types" and row["size"] > 0
                         for name, row in fresh.items()) else ["nonempty logs/data_types export"]
    return [] if "code_revisions.log" in names else ["fresh code_revisions.log"]


def check_environment():
    if os.name != "nt":
        raise RuntimeError("This starter is configured for the local Windows installation.")
    if ck3_running():
        raise RuntimeError("CK3 is already running. Close it before starting diagnostics.")
    for image in ["dowser.exe", "Paradox Launcher.exe"]:
        if process_running(image):
            raise RuntimeError("Close the Paradox launcher before diagnostics: " + image)
    audit = json.loads((ROOT / "evidence/diagnostic-start-audit.json").read_text(encoding="utf-8"))
    for source in audit["local_sources"]:
        path = Path(source["path"])
        if not path.exists() or digest(path.read_bytes()) != source["sha256"]:
            raise RuntimeError("Audited diagnostic source changed; review before launching: " + str(path))
    version_path = INSTALL / "launcher/launcher-settings.json"
    version = json.loads(version_path.read_text(encoding="utf-8-sig"))
    if version.get("rawVersion") != EXPECTED:
        raise RuntimeError("Installation version changed; refresh the source audit first: " + str(version.get("version")))
    exe = INSTALL / "binaries/ck3.exe"
    if not exe.is_file() or not CONFIG.is_file():
        raise RuntimeError("Game executable or existing dlc_load.json is missing.")
    original = CONFIG.read_bytes()
    for prior in (ROOT / "runtime-evidence").glob("*/run.json"):
        prior_record = json.loads(prior.read_text(encoding="utf-8"))
        if (not prior_record.get("configuration_restored", False)
                and digest(original) != prior_record.get("original_config_sha256")):
            raise RuntimeError("An earlier run needs configuration recovery/review first: " + str(prior.parent))
    config = json.loads(original.decode("utf-8-sig"))
    if not isinstance(config.get("enabled_mods"), list) or not isinstance(config.get("disabled_dlcs"), list):
        raise RuntimeError("Unexpected dlc_load.json format; nothing was changed.")
    native = INSTALL / "game/_commandline_options.info"
    contract = native.read_text(encoding="utf-8-sig")
    for flag in ["-debug_mode", "-suppress_error_log"]:
        if flag not in contract:
            raise RuntimeError("Missing audited startup option: " + flag)
    return version, exe, original, config


def recover(run):
    run = Path(run).resolve()
    allowed = (ROOT / "runtime-evidence").resolve()
    if not run.is_relative_to(allowed):
        raise RuntimeError("Recovery folder must be inside runtime-evidence.")
    if ck3_running():
        raise RuntimeError("Close CK3 before restoring its mod selection.")
    record = json.loads((run / "run.json").read_text(encoding="utf-8"))
    original = (run / "original-dlc-load.json.raw").read_bytes()
    if digest(original) != record["original_config_sha256"]:
        raise RuntimeError("Backup hash mismatch; recovery aborted.")
    if not restore_config(CONFIG, original, record["temporary_config_sha256"]):
        raise RuntimeError("dlc_load.json was changed elsewhere. Backup preserved; manual review required.")
    record["configuration_restored"] = True
    write_json(run / "run.json", record)
    print("Original mod selection restored.")


def execute():
    version, exe, original, config = check_environment()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    run = ROOT / "runtime-evidence" / stamp
    run.mkdir(parents=True, exist_ok=False)
    (run / "original-dlc-load.json.raw").write_bytes(original)
    before = inventory(LOGS)
    backup = capture(LOGS, run / "previous-logs", before)
    clean = dict(config)
    clean["enabled_mods"] = []
    temporary = json.dumps(clean, ensure_ascii=False).encode("utf-8")
    record = {"started_utc": stamp, "status": "prepared", "installation_version": version["version"],
              "executed_version": "pending review of fresh runtime logs; empty code_revisions.log is not proof",
              "executed_checksum": "pending runtime evidence review",
              "exe": str(exe), "exe_sha256": digest(exe.read_bytes()),
              "original_config_sha256": digest(original), "temporary_config_sha256": digest(temporary),
              "configuration_restored": False, "enabled_mods": [],
              "disabled_dlcs": config["disabled_dlcs"],
              "dlc_entitlements": "Not inferred from disabled_dlcs; verify loaded DLC in fresh logs",
              "previous_logs": backup, "stages": [],
              "limits": ["Main-menu/export only; no campaign, feature UI, saved-game, mod or multiplayer tests",
                         "File production is not proof of command semantics or mod compatibility"]}
    for name in ["game/_commandline_options.info", "launcher/launcher-settings.json", "binaries/checksum.txt"]:
        path = INSTALL / name
        raw = path.read_bytes()
        record.setdefault("installation_sources", []).append({"path": str(path), "sha256": digest(raw)})
        capture(path.parent, run / "installation" / path.parent.name,
                {path.name: {"sha256": digest(raw), "mtime_ns": path.stat().st_mtime_ns, "size": len(raw)}})
    write_json(run / "run.json", record)
    print("Evidence folder:", run, flush=True)
    crash_before = crash_inventory(CRASHES)
    record["mode"] = "normal-debug-manual-gui-export"
    record["requested_console_command"] = "dump_data_types"
    record["baseline_kind"] = "main-menu; user profile retained"
    record["crash_reports"] = []
    record["profile_warnings"] = []
    # Handle Ctrl+C only between game processes; never restore mods under a live child.
    try:
        if CONFIG.read_bytes() != original:
            raise RuntimeError("Mod selection changed during preparation; launch aborted.")
        CONFIG.write_bytes(temporary)
        before = inventory(LOGS)
        argv = launch_arguments(exe)
        stage = {"name": "main-menu-data-types", "argv": argv,
                 "start_utc": datetime.now(timezone.utc).isoformat(), "state": "launching"}
        record["stages"].append(stage)
        record["status"] = "running"
        write_json(run / "run.json", record)
        print("CK3 starts normally in debug mode. At the MAIN MENU, open the console,", flush=True)
        print("enter dump_data_types once, then exit CK3 normally after export completes.", flush=True)
        print("The helper does not enter the command or close the game for you.", flush=True)
        previous_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
        try:
            with (run / "main-menu-data-types-process-output.raw").open("wb") as output:
                process = subprocess.Popen(argv, cwd=exe.parent, stdout=output, stderr=subprocess.STDOUT)
                while process.poll() is None:
                    try:
                        process.wait(timeout=30)
                    except subprocess.TimeoutExpired:
                        print("Waiting for your GUI export and normal game exit. Keep this terminal open.", flush=True)
                stage["exit_code"] = process.returncode
        finally:
            signal.signal(signal.SIGINT, previous_handler)
        # Capture crashes before log collection so a later log race cannot hide a report.
        crash_fresh = changed(crash_before, crash_inventory(CRASHES))
        record["crash_reports"] = capture(CRASHES, run / "crashes", crash_fresh)
        fresh = changed(before, inventory(LOGS))
        stage["files"] = capture(LOGS, run / stage["name"], fresh)
        stage["missing_expected"] = validate_exports(stage["name"], fresh)
        record["profile_warnings"] = profile_warnings(LOGS, fresh)
        if record["profile_warnings"]:
            print("Existing-profile AGOT references recorded; relation to a crash is unknown.", flush=True)
        stage["state"] = "captured"
        stage["end_utc"] = datetime.now(timezone.utc).isoformat()
        write_json(run / "run.json", record)
        problems = []
        if stage["exit_code"] != 0:
            problems.append("nonzero game exit: " + str(stage["exit_code"]))
        if record["crash_reports"]:
            problems.append("new/changed crash report files captured")
        if stage["missing_expected"]:
            problems.append("missing fresh exports: " + str(stage["missing_expected"]))
        if problems:
            raise RuntimeError("; ".join(problems))
        record["status"] = "captured-review-pending"
    except BaseException as error:
        record["status"] = "incomplete"
        record["error"] = str(error) or type(error).__name__
        raise
    finally:
        record["configuration_restored"] = restore_config(CONFIG, original, digest(temporary))
        if not record["configuration_restored"]:
            record["status"] = "incomplete"
            record["restoration_error"] = "Configuration changed elsewhere; original backup preserved for review."
        record["finished_utc"] = datetime.now(timezone.utc).isoformat()
        write_json(run / "run.json", record)
        if not record["configuration_restored"]:
            print("RESTORATION NEEDS REVIEW: original selection remains backed up in", run, flush=True)
        print("Evidence saved:", run, flush=True)
    if not record["configuration_restored"]:
        raise RuntimeError("Configuration changed elsewhere; manual restoration review is required.")
    print("Fresh GUI export and main-menu logs captured. Original mod selection restored. Review remains pending.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preflight", action="store_true", help="read-only checks, no CK3 launch")
    parser.add_argument("--restore", metavar="RUN_FOLDER", help="recover an interrupted run's original selection")
    args = parser.parse_args()
    try:
        if args.preflight:
            version, exe, original, config = check_environment()
            print("Read-only preflight passed:", version["version"], "| mods to temporarily disable:", len(config["enabled_mods"]))
        elif args.restore:
            recover(args.restore)
        else:
            # Windows releases this byte-range lock even if the helper crashes.
            lock_path = ROOT / "diagnostic-start.lock"
            with lock_path.open("a+b") as lock:
                if lock_path.stat().st_size == 0:
                    lock.write(b"Lock for CK3 diagnostic starter.\r\n")
                    lock.flush()
                lock.seek(0)
                try:
                    msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
                except OSError:
                    raise RuntimeError("Another diagnostic starter is already active.")
                try:
                    execute()
                finally:
                    lock.seek(0)
                    msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)
    except (Exception, KeyboardInterrupt) as error:
        print("Diagnostics stopped:", str(error) or type(error).__name__, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
