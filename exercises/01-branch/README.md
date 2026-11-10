# 练习 01：创建并切换分支

## 目标

学会创建分支、在分支上提交，并观察 `main` 与练习分支的差异。

## 场景

你要为项目补充一条个人学习记录，但不想直接改 `main`。先开一个分支，把修改放在分支上。

## 步骤

1. 确认当前在 `main`，并且工作区干净：

   ```bash
   git switch main
   git status
   ```

2. 创建并切换到个人分支：

   ```bash
   git switch -c practice/your-name
   ```

3. 打开 `exercises/01-branch/note.md`，把占位内容改成你的名字和今天练习的命令。

4. 查看差异：

   ```bash
   git diff
   ```

5. 提交：

   ```bash
   git add exercises/01-branch/note.md
   git commit -m "docs: 完成 01 分支练习"
   ```

6. 查看分支和提交：

   ```bash
   git branch -v
   git log --oneline --graph --all --decorate -8
   ```

## 验收标准

- [ ] `git branch` 中能看到 `practice/your-name`
- [ ] 当前分支前有 `*`
- [ ] 至少有一条自己的提交
- [ ] 切回 `main` 后，`note.md` 恢复为占位内容
- [ ] 能说出“分支只是一个指向提交的指针”是什么意思

## 提示

- 分支名不要用空格；用短横线或斜杠分隔。
- 如果 `git switch` 不可用，用 `git checkout -b practice/your-name`。
- 切换分支前先提交或暂存，否则未提交的修改可能被带到另一个分支。
