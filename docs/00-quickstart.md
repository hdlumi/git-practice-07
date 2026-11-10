# 快速开始

## 你需要准备什么

- 一台可以安装 Git 的电脑（Windows、macOS、Linux 均可）
- Python 3.10 或更高版本
- 一个 GitHub 账号（练习 04 需要）
- 30–60 分钟，建议按顺序完成 5 个练习

## 第一步：获取项目

```bash
git clone https://github.com/hdlumi/git-practice-07.git
cd git-practice-07
```

如果你已经下载了 ZIP，也可以直接进入解压后的目录。练习不需要联网，只有模拟 PR 时需要 GitHub。

## 第二步：检查环境

```bash
python -m gitpractice doctor
```

正常输出会显示 Python 版本、Git 版本、当前分支和仓库根目录。如果提示 `未找到 git 命令`，请先安装 Git，并重新打开终端。

Windows 用户如果 `python` 不可用，可以尝试：

```powershell
py -3 -m gitpractice doctor
```

## 第三步：选择练习

```bash
# 查看练习总览
cat exercises/README.md

# Windows PowerShell
Get-Content exercises/README.md
```

建议顺序：

1. `01-branch`：创建分支并提交
2. `02-merge`：把分支合并回主线
3. `03-conflict`：制造并解决一次冲突
4. `04-pr`：走一遍 Fork → PR 流程
5. `05-recovery`：练习恢复误操作

## 第四步：开始练习前先建一个自己的分支

```bash
git switch -c practice/你的名字
```

例如：

```bash
git switch -c practice/hudanlu
```

这样即使练习中改乱了文件，也可以随时回到干净的主线：

```bash
git switch main
git branch -D practice/hudanlu
```

## 第五步：随时检查

```bash
python -m gitpractice check
```

它会检查两件事：

- 练习所需的文件是否齐全
- `exercises/` 和 `sandbox/` 中是否还有未解决的冲突标记

检查通过时退出码为 0，失败时为 1，适合放进提交前检查或 CI。

## 常见问题

### `git switch` 不认识

`git switch` 需要 Git 2.23+。先用 `git --version` 查看版本；如果太旧，请升级 Git。临时也可以用：

```bash
git checkout -b practice/你的名字
```

### 中文显示乱码

Windows 终端可以尝试：

```powershell
chcp 65001
$env:PYTHONUTF8="1"
```

### 我把文件改坏了

如果还没有提交：

```bash
git restore .
```

如果已经提交，但想撤销这次提交：

```bash
git revert HEAD
```

不要一开始就用 `git reset --hard`，它会丢弃未提交的修改。更多恢复方法见 [05-recovery.md](05-recovery.md)。

### 我想重新开始

```bash
git switch main
git branch -D practice/你的名字
git switch -c practice/你的名字
```

如果连 `main` 也被改乱了，可以重新克隆一份仓库，这是最干净的复位方式。
