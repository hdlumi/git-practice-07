# 练习 02：合并分支

## 目标

把练习 01 的分支合并回 `main`，理解快进合并和 `--no-ff` 的区别。

## 场景

你的个人学习记录已经写好，现在要把它合入主线，让其他人也能看到。

## 步骤

1. 确认练习分支上有提交：

   ```bash
   git switch practice/your-name
   git log --oneline -3
   ```

2. 切回 `main`，确认它没有新的未合并提交：

   ```bash
   git switch main
   git log --oneline -3
   ```

3. 使用 `--no-ff` 合并，保留分支边界：

   ```bash
   git merge --no-ff practice/your-name -m "merge: 合入个人分支练习"
   ```

4. 查看合并后的图：

   ```bash
   git log --oneline --graph --decorate -10
   ```

5. 确认文件已经进入 `main`：

   ```bash
   git status
   cat exercises/01-branch/note.md
   ```

## 验收标准

- [ ] `main` 上能看到合并提交
- [ ] `git log --graph` 中能看到分叉和合流
- [ ] `exercises/01-branch/note.md` 包含你的修改
- [ ] 工作区干净
- [ ] 能解释快进合并与 `--no-ff` 的差别

## 提示

- 如果合并提示冲突，先看 [03-conflict.md](../../docs/03-conflict.md)，不要直接 `git add .`。
- 想放弃这次合并：`git merge --abort`。
- 合并完成后可以删除练习分支：`git branch -d practice/your-name`。
