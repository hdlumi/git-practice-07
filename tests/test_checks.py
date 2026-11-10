import unittest
from pathlib import Path

from gitpractice.checks import (
    CONFLICT_PREFIXES,
    find_conflict_markers,
    missing_paths,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"


class CheckTests(unittest.TestCase):
    def test_missing_paths_reports_readme(self) -> None:
        missing = missing_paths(FIXTURES / "missing")
        self.assertIn("README.md", missing)

    def test_clean_exercise_has_no_markers(self) -> None:
        self.assertEqual(find_conflict_markers(FIXTURES / "clean"), [])

    def test_unresolved_marker_is_detected(self) -> None:
        markers = find_conflict_markers(FIXTURES / "conflict")
        self.assertEqual(len(markers), 3)
        self.assertEqual(markers[0].path, "exercises/03-conflict/conflict-demo.md")
        self.assertEqual(markers[0].line_number, 1)
        self.assertTrue(markers[0].line.startswith(CONFLICT_PREFIXES))

    def test_non_text_file_is_ignored(self) -> None:
        self.assertEqual(find_conflict_markers(FIXTURES / "ignored"), [])


if __name__ == "__main__":
    unittest.main()
