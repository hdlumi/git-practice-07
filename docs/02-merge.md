# 合并：把一条分支的工作带回主线

## 合并前先确认三件事

```bash
git status          # 工作区是否干净
git branch --show-current
git log --oneline --graph --all --decorate -10
```

工作区不干净时，先提交或暂存，避免合并过程中出现难以解释的改动。

## 两种常见的合并结果

### 快进合并（fast-forward）

如果目标分支没有新提交，Git 只需要把指针向前移动：

```text
合并前：main ──●        dev ──●──●
合并后：main ──●──●──●
```

```bash
git switch main
git merge dev
```

### 保留合并记录（--no-ff）

即使可以快进，也强制生成一个合并提交，历史更像“一个功能被整体合入”：

```bash
git switch main
git merge --no-ff dev -m "merge: 合入 dev 分支"
```

团队协作中常用 `--no-ff`，因为它保留了分支的边界，方便回溯。

## 发生冲突怎么办

如果两个分支改了同一文件的同一区域，Git 无法自动决定保留哪一个，就会停下来：

```text
Auto-merging exercises/03-conflict/conflict-demo.md
CONFLICT (content): Merge conflict in exercises/03-conflict/conflict-demo.md
Automatic merge failed; fix conflicts and then commit the result.
```

这时不要慌，按 [03-conflict.md](03-conflict.md) 的步骤处理。

## 放弃这次合并

```bash
git merge --abort
```

它会把仓库恢复到合并前的状态。已经提交的合并不能用它撤销，需要用 `git revert`。

## 练习：把练习分支合并回 main

假设你已经完成 `practice/your-name` 的提交：

```bash
git switch main
git merge --no-ff practice/your-name -m "merge: 合入个人分支练习"
git log --oneline --graph --decorate -8
```

## 验收标准

- `git log --graph` 中能看到一个合并提交
- `main` 包含个人分支上的修改
- `git status` 显示工作区干净
- 能解释这次合并是快进还是 `--no-ff`

## 合并后清理

```bash
git branch -d practice/your-name
```

如果这个分支还要继续用，就不要删除。删除分支只删除指针，不会删除已经合并进主线的提交。
