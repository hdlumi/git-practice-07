"""Command line entry point for git-practice-07."""

from __future__ import annotations

import argparse
import platform
import subprocess
import sys
from pathlib import Path

from . import __version__
from .checks import check_project


def _run_git(*args: str) -> tuple[bool, str]:
    """Run a Git command and return (success, combined output)."""

    try:
        completed = subprocess.run(
            ["git", *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except FileNotFoundError:
        return False, "未找到 git 命令，请先安装 Git。"
    output = (completed.stdout or completed.stderr or "").strip()
    return completed.returncode == 0, output


def _doctor(root: Path) -> int:
    print("git-practice-07 环境检查")
    print("=" * 34)
    print(f"Python : {platform.python_version()}")
    print(f"系统   : {platform.system()} {platform.release()}")

    git_ok, git_output = _run_git("--version")
    if git_ok:
        print(f"Git    : {git_output.replace('git version ', '')}")
    else:
        print(f"Git    : [失败] {git_output}")

    inside_ok, inside_output = _run_git("rev-parse", "--is-inside-work-tree")
    if inside_ok and inside_output.lower() == "true":
        branch_ok, branch = _run_git("branch", "--show-current")
        current = branch if branch_ok and branch else "(detached HEAD)"
        root_ok, repo_root = _run_git("rev-parse", "--show-toplevel")
        print(f"仓库   : {'是' if root_ok else '无法读取'}")
        print(f"分支   : {current}")
        if root_ok:
            print(f"根目录 : {repo_root}")
    else:
        print("仓库   : [提示] 当前目录不在 Git 仓库中")

    print("=" * 34)
    if git_ok:
        print("[OK] 基础环境可以使用，继续阅读 exercises/README.md。")
        return 0

    print("[FAIL] 请先安装 Git，再重新运行 doctor。")
    return 1


def _check(root: Path) -> int:
    result = check_project(root)
    print("git-practice-07 练习检查")
    print("=" * 34)

    if result.missing:
        print(f"[FAIL] 缺少 {len(result.missing)} 个必需文件：")
        for path in result.missing:
            print(f"  - {path}")
    else:
        print("[OK] 必需文件齐全。")

    if result.markers:
        print(f"[FAIL] 发现 {len(result.markers)} 处未解决的冲突标记：")
        for marker in result.markers:
            print(f"  - {marker.path}:{marker.line_number}  {marker.line}")
    else:
        print("[OK] 未发现未解决的冲突标记。")

    print("=" * 34)
    if result.ok:
        print("[OK] 检查通过。")
        return 0

    print("[FAIL] 请修复上面的问题后重试。")
    return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="git-practice",
        description="Git 分支练习沙盒：检查环境与练习文件。",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    subparsers = parser.add_subparsers(dest="command", metavar="命令")
    subparsers.add_parser("doctor", help="检查 Python、Git 和当前仓库状态")
    subparsers.add_parser("check", help="检查必需文件和未解决的冲突标记")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "doctor":
        return _doctor(Path.cwd())
    if args.command == "check":
        return _check(Path.cwd())

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
