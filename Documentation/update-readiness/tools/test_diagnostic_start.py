"""Offline tests; never launches CK3 or touches its real configuration."""
from contextlib import contextmanager
import io
import json
import shutil
import unittest
import uuid
from unittest.mock import patch
from pathlib import Path
from diagnostic_start import capture, changed, digest, inventory, restore_config, validate_exports, EXPORTS
from diagnostic_start import crash_inventory, launch_arguments, profile_warnings


@contextmanager
def test_directory():
    from diagnostic_start import ROOT
    path = ROOT / ("offline-test-" + uuid.uuid4().hex)
    # tempfile's Windows private ACL is incompatible with the sandbox token.
    path.mkdir(mode=0o777)
    try:
        yield path
    finally:
        if not path.resolve().is_relative_to(ROOT.resolve()):
            raise RuntimeError("Test cleanup target escaped Documentation.")
        shutil.rmtree(path)


class DiagnosticsTests(unittest.TestCase):
    def test_normal_start_has_no_automatic_actions(self):
        self.assertEqual(launch_arguments(Path("ck3.exe")),
                         ["ck3.exe", "-gdpr-compliant", "-debug_mode", "-suppress_error_log"])

    def test_old_exports_do_not_count(self):
        before = {name: {"sha256": "old", "mtime_ns": 1, "size": 1} for name in EXPORTS}
        self.assertEqual(changed(before, dict(before)), {})
        self.assertEqual(set(validate_exports("script-docs", {})), EXPORTS)

    def test_fresh_exports_and_gui_are_required(self):
        fresh = {name: {"size": 10} for name in EXPORTS}
        self.assertEqual(validate_exports("script-docs", fresh), [])
        fresh["effects.log"]["size"] = 0
        self.assertIn("effects.log", validate_exports("script-docs", fresh))
        self.assertTrue(validate_exports("data-types", {"debug.log": {"size": 10}}))
        self.assertEqual(validate_exports("data-types", {"data_types/types.log": {"size": 10}}), [])
        self.assertTrue(validate_exports("data-types", {"data_types/types.log": {"size": 0}}))

    def test_restore_preserves_original_bytes_and_external_edits(self):
        with test_directory() as directory:
            path = Path(directory) / "config.json"
            original, temporary, external = b'{"enabled_mods":["mine"]}\r\n', b'{}', b'{"changed":true}'
            path.write_bytes(temporary)
            self.assertTrue(restore_config(path, original, digest(temporary)))
            self.assertEqual(path.read_bytes(), original)
            path.write_bytes(external)
            self.assertFalse(restore_config(path, original, digest(temporary)))
            self.assertEqual(path.read_bytes(), external)

    def test_capture_keeps_raw_bytes_and_detects_races(self):
        # Capture paths must be inside the documentation root, even in offline tests.
        from diagnostic_start import ROOT
        with test_directory() as directory:
            base = Path(directory)
            source = base / "logs"
            source.mkdir()
            path = source / "types.log"
            raw = b'\xff\xfe\x00\r\n'
            path.write_bytes(raw)
            selected = inventory(source)
            rows = capture(source, base / "copies", selected)
            self.assertEqual((base / "copies/types.log.raw").read_bytes(), raw)
            self.assertEqual(rows[0]["sha256"], digest(raw))
            path.write_bytes(b"changed")
            with self.assertRaises(RuntimeError):
                capture(source, base / "race", selected)

    def test_crash_capture_excludes_saves_settings_and_dumps(self):
        with test_directory() as directory:
            crash = directory / "crashes" / "old"
            (crash / "logs").mkdir(parents=True)
            for name in ["exception.txt", "meta.yml", "last_save.ck3", "minidump.dmp", "pdx_settings.txt"]:
                (crash / name).write_bytes(b"\xef\xbb\xbffixture" if Path(name).suffix in {".txt", ".yml"} else b"fixture")
            (crash / "logs/error.log").write_bytes(b"error")
            (crash / "logs/unexpected.ck3").write_bytes(b"save")
            before = crash_inventory(directory / "crashes")
            self.assertEqual(set(before), {"old/exception.txt", "old/meta.yml", "old/logs/error.log"})
            self.assertEqual(changed(before, crash_inventory(directory / "crashes")), {})
            fresh = directory / "crashes" / "new"
            fresh.mkdir()
            (fresh / "exception.txt").write_bytes(b"\xef\xbb\xbfaccess violation")
            rows = changed(before, crash_inventory(directory / "crashes"))
            self.assertEqual(set(rows), {"new/exception.txt"})
            copied = capture(directory / "crashes", directory / "copies", rows)
            self.assertEqual(len(copied), 1)
            self.assertTrue((directory / "copies/new/exception.txt.raw").exists())

    def test_profile_warnings_do_not_claim_crash_cause(self):
        with test_directory() as directory:
            (directory / "error.log").write_bytes(b"Failed to read agot_canon_children_disabled")
            warnings = profile_warnings(directory, {"error.log": {"size": 1}})
            self.assertEqual(warnings[0]["references"], ["agot_canon_children_disabled"])
            self.assertIn("unknown", warnings[0]["interpretation"])

    def run_mock_game(self, *, has_export=True, crash=False, crash_exit=1, external_edit=False, launch_failure=False):
        import diagnostic_start as runner
        with test_directory() as directory:
            install = directory / "install"
            for name in ["game/_commandline_options.info", "launcher/launcher-settings.json", "binaries/checksum.txt", "binaries/ck3.exe"]:
                path = install / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b"\xef\xbb\xbffixture" if path.suffix == ".txt" else b"fixture")
            logs = directory / "logs"
            logs.mkdir()
            (logs / "effects.log").write_bytes(b"retained script export")
            config = directory / "dlc_load.json"
            original = b'{"enabled_mods":["mine"],"disabled_dlcs":[]}\r\n'
            config.write_bytes(original)
            crashes = directory / "crashes"
            runs = directory / "runtime-evidence"
            version = {"version": "fixture"}

            def fake_launch(*args, **kwargs):
                if launch_failure:
                    raise OSError("fixture launch failure")
                self.assertEqual(args[0], launch_arguments(install / "binaries/ck3.exe"))
                self.assertEqual(json.loads(config.read_bytes())["enabled_mods"], [])
                if has_export:
                    (logs / "data_types").mkdir()
                    (logs / "data_types/types.log").write_bytes(b"fresh types")
                if crash:
                    report = crashes / "new"
                    report.mkdir(parents=True)
                    (report / "exception.txt").write_bytes(b"\xef\xbb\xbffixture crash")
                    (report / "minidump.dmp").write_bytes(b"private dump")
                if external_edit:
                    config.write_bytes(b'{"external":true}')
                class Process:
                    returncode = crash_exit if crash else 0
                    def poll(self):
                        return self.returncode
                return Process()

            with patch.multiple(runner, ROOT=directory, INSTALL=install, LOGS=logs, CONFIG=config, CRASHES=crashes), \
                    patch.object(runner, "check_environment", return_value=(version, install / "binaries/ck3.exe", original,
                        {"enabled_mods": ["mine"], "disabled_dlcs": []})), \
                    patch.object(runner.subprocess, "Popen", side_effect=fake_launch), \
                    patch("sys.stdout", new_callable=io.StringIO):
                if crash or external_edit or not has_export or launch_failure:
                    with self.assertRaises((RuntimeError, OSError)):
                        runner.execute()
                else:
                    runner.execute()
            record = json.loads(next(runs.glob("*/run.json")).read_text())
            self.assertEqual(config.read_bytes(), b'{"external":true}' if external_edit else original)
            self.assertEqual((logs / "effects.log").read_bytes(), b"retained script export")
            self.assertEqual(record["configuration_restored"], not external_edit)
            return record

    def test_normal_exit_collects_gui_and_restores(self):
        record = self.run_mock_game()
        self.assertEqual(record["status"], "captured-review-pending")
        self.assertEqual(len(record["stages"]), 1)

    def test_missing_export_is_incomplete_and_restores(self):
        self.assertEqual(self.run_mock_game(has_export=False)["status"], "incomplete")

    def test_crash_is_incomplete_even_with_export(self):
        record = self.run_mock_game(crash=True)
        self.assertEqual(record["status"], "incomplete")
        self.assertEqual(len(record["crash_reports"]), 1)

    def test_external_config_edit_is_preserved(self):
        record = self.run_mock_game(external_edit=True)
        self.assertFalse(record["configuration_restored"])
        self.assertEqual(record["status"], "incomplete")

    def test_crash_report_marks_zero_exit_incomplete(self):
        self.assertEqual(self.run_mock_game(crash=True, crash_exit=0)["status"], "incomplete")

    def test_launch_failure_restores_selection(self):
        self.assertEqual(self.run_mock_game(launch_failure=True)["status"], "incomplete")


if __name__ == "__main__":
    unittest.main()
