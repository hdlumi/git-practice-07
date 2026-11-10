# 练习总览

这里把 Git 协作中最重要的几个动作拆成 5 个练习。每个练习都可以在 10–20 分钟内完成，建议按顺序做。

## 练习前

```bash
# 确认环境和仓库状态
python -m gitpractice doctor
git status

# 从 main 创建自己的练习分支
git switch main
git switch -c practice/你的名字
```

## 练习列表

| 编号 | 主题 | 你会做什么 | 对应文档 |
| --- | --- | --- | --- |
| 01 | 创建分支 | 创建个人分支，修改并提交 | [01-branch.md](../docs/01-branch.md) |
| 02 | 合并分支 | 把个人分支合并回 main | [02-merge.md](../docs/02-merge.md) |
| 03 | 解决冲突 | 让两个分支改同一行，再手动解决 | [03-conflict.md](../docs/03-conflict.md) |
| 04 | Pull Request | 走一遍 Fork → PR 流程 | [04-pr.md](../docs/04-pr.md) |
| 05 | 恢复 | 用 reflog 救回误删的分支 | [05-recovery.md](../docs/05-recovery.md) |

## 规则

1. 每个练习从 `main` 创建一个独立分支。
2. 一次提交只做一件事，提交信息写清楚。
3. 改完先看 `git diff`，再 `git add`。
4. 遇到冲突不要 `git add .` 一把梭，先打开文件确认。
5. 练习完成后，用 `python -m gitpractice check` 自检。

## 提交信息参考

```text
docs: 完成 01 分支练习
docs: 完成 02 合并练习
fix: 解决 03 冲突练习
docs: 完成 04 PR 练习
chore: 完成 05 恢复练习
```

## 卡住了怎么办

- 先看 `git status`：它会告诉你当前在哪个分支、哪些文件有变化。
- 看 `git log --oneline --graph --all --decorate -10`：确认提交在哪里。
- 想放弃当前操作：`git merge --abort` 或 `git restore .`。
- 实在乱了：重新克隆一份仓库，从干净状态开始。

## 练习完成后

可以把自己的分支合并回 `main`，也可以保留分支作为学习记录。课程作业中，建议保留至少一个功能分支、一个合并提交和一次冲突解决记录，方便截图说明。
