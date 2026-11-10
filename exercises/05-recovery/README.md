# 练习 05：恢复误删的分支

## 目标

学会用 `git reflog` 找到“消失”的提交，并把误删的分支恢复出来。

## 场景

你完成了一次提交，清理分支时不小心用了 `git branch -D`，把还没合并的工作删掉了。不要慌，提交通常还在。

## 步骤

### 1. 创建一个临时分支并提交

```bash
git switch main
git switch -c practice/recovery-demo
```

编辑 `exercises/05-recovery/recovery-note.md`，写一句“这句话不能丢”，然后：

```bash
git add exercises/05-recovery/recovery-note.md
git commit -m "docs: 恢复练习的重要提交"
```

### 2. 记住提交哈希

```bash
git log --oneline -1
```

输出中类似 `a1b2c3d` 的短哈希就是你的提交。

### 3. 删除分支

```bash
git switch main
git branch -D practice/recovery-demo
```

此时 `git branch` 里已经看不到它，但提交对象还在。

### 4. 用 reflog 找回来

```bash
git reflog -10
```

找到类似下面的一行：

```text
a1b2c3d HEAD@{2}: commit: docs: 恢复练习的重要提交
```

### 5. 恢复分支

```bash
git switch -c rescue/recovery-demo a1b2c3d
```

确认文件内容还在：

```bash
cat exercises/05-recovery/recovery-note.md
git log --oneline -1
```

## 验收标准

- [ ] 真实删除过一个含提交的分支
- [ ] 能用 `git reflog` 找到提交哈希
- [ ] 恢复后的分支包含原来的提交
- [ ] 能说出 `git branch -D` 删除的是什么、没有删除什么

## 提示

- `reflog` 是本地操作记录，不会随仓库推送。
- 如果记不住哈希，可以用 `git reflog` 的时间、提交信息来定位。
- 不要用 `git reset --hard` 做实验，除非你确认没有未提交的修改。
- 恢复后建议把分支合并回 `main`，再删除临时分支。
