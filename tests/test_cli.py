import contextlib
import io
import unittest

from gitpractice.cli import main


class CliTests(unittest.TestCase):
    def test_help_without_command(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = main([])
        self.assertEqual(code, 0)
        self.assertIn("git-practice", output.getvalue())

    def test_version_exits(self) -> None:
        output = io.StringIO()
        with self.assertRaises(SystemExit) as raised:
            with contextlib.redirect_stdout(output):
                main(["--version"])
        self.assertEqual(raised.exception.code, 0)
        self.assertIn("0.1.0", output.getvalue())


if __name__ == "__main__":
    unittest.main()
