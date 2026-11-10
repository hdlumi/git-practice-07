# 分支：让不同的工作互不打扰

## 分支到底是什么

Git 的分支不是复制一份完整目录，而是一个指向某次提交的可移动指针。`HEAD` 指向你当前所在的分支，提交时这个分支指针向前移动。

```text
main ──●──●──●
             ↑
           HEAD

dev  ──●──●
          ↑
        HEAD（切换后）
```

创建分支的成本很低，所以可以放心为每个任务开一个分支。

## 常用命令

```bash
# 查看本地分支；带 * 的是当前分支
git branch

# 创建并切换到新分支
git switch -c feature/my-first-branch

# 切换已有分支
git switch main

# 查看当前状态
git status

# 查看分支最后一条提交
git branch -v
```

旧版 Git 使用：

```bash
git checkout -b feature/my-first-branch
git checkout main
```

## 命名建议

| 前缀 | 用途 | 示例 |
| --- | --- | --- |
| `feature/` | 新功能 | `feature/check-command` |
| `fix/` | 修缺陷 | `fix/windows-path` |
| `docs/` | 文档 | `docs/quickstart` |
| `practice/` | 个人练习 | `practice/hudanlu` |

名字用短横线分隔，避免空格和中文路径带来的终端兼容问题。

## 练习：创建你的第一个分支

在项目根目录执行：

```bash
git switch -c practice/your-name
```

然后编辑 `exercises/01-branch/note.md`，把“我的名字”改成你的名字，并写一句你今天想练习的 Git 命令。

```bash
git status
git diff
git add exercises/01-branch/note.md
git commit -m "docs: 完成分支练习记录"
```

## 验收标准

- `git branch` 能看到你的 `practice/your-name` 分支
- 当前分支前面有 `*`
- `git log --oneline -3` 能看到你的提交
- 切回 `main` 后，刚才的修改不在工作区（因为提交在另一个分支上）

## 小实验：观察指针移动

```bash
git switch main
git log --oneline --graph --all --decorate -10
```

你会看到 `main` 和 `practice/your-name` 指向不同的提交。理解这一点，后面的合并和冲突就会容易很多。

## 删除分支

合并完成后可以删除已经没用的分支：

```bash
git branch -d practice/your-name
```

如果 Git 提示分支还没有合并，说明它的提交还没进入当前分支。确认不需要后，才使用大写的 `-D` 强制删除。
