"""Project checks used by the command line tool and the test suite."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

REQUIRED_PATHS: tuple[str, ...] = (
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    "docs/00-quickstart.md",
    "docs/01-branch.md",
    "docs/02-merge.md",
    "docs/03-conflict.md",
    "docs/04-pr.md",
    "docs/05-recovery.md",
    "exercises/README.md",
    "exercises/01-branch/README.md",
    "exercises/02-merge/README.md",
    "exercises/03-conflict/README.md",
    "exercises/03-conflict/conflict-demo.md",
    "exercises/04-pr/README.md",
    "exercises/05-recovery/README.md",
)

SCAN_DIRS: tuple[str, ...] = ("exercises", "sandbox")
CONFLICT_PREFIXES: tuple[str, ...] = ("<<<<<<<", "=======", ">>>>>>>")
TEXT_SUFFIXES: frozenset[str] = frozenset(
    {".md", ".txt", ".py", ".toml", ".yml", ".yaml", ".json", ".sh", ".ps1"}
)


@dataclass(frozen=True)
class ConflictMarker:
    """A line that still looks like an unresolved merge conflict marker."""

    path: str
    line_number: int
    line: str


@dataclass
class CheckResult:
    """The result of checking a practice project."""

    missing: list[str] = field(default_factory=list)
    markers: list[ConflictMarker] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.missing and not self.markers


def missing_paths(root: Path | str) -> list[str]:
    """Return required project paths that do not exist below *root*."""

    base = Path(root)
    return [path for path in REQUIRED_PATHS if not (base / path).exists()]


def _is_text_candidate(path: Path) -> bool:
    return path.suffix.lower() in TEXT_SUFFIXES or path.name in {
        "LICENSE",
        ".gitignore",
        "Makefile",
    }


def iter_scan_files(root: Path | str):
    """Yield text files that may contain unresolved conflict markers."""

    base = Path(root)
    for directory in SCAN_DIRS:
        scan_root = base / directory
        if not scan_root.exists():
            continue
        for path in scan_root.rglob("*"):
            if path.is_file() and _is_text_candidate(path):
                yield path


def find_conflict_markers(root: Path | str) -> list[ConflictMarker]:
    """Find unresolved conflict markers in the practice directories."""

    base = Path(root)
    markers: list[ConflictMarker] = []
    for path in iter_scan_files(base):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError):
            continue
        for number, line in enumerate(lines, start=1):
            if line.startswith(CONFLICT_PREFIXES):
                markers.append(
                    ConflictMarker(
                        path=path.relative_to(base).as_posix(),
                        line_number=number,
                        line=line.strip(),
                    )
                )
    return markers


def check_project(root: Path | str) -> CheckResult:
    """Run all checks for a practice project rooted at *root*."""

    return CheckResult(
        missing=missing_paths(root),
        markers=find_conflict_markers(root),
    )
