# 恢复：把误操作救回来

Git 的大多数操作都可以恢复，前提是不要急着执行会覆盖历史的命令。先看清状态，再动手。

## 先记住三个命令

```bash
git status          # 现在处于什么状态
git log --oneline --graph --all --decorate -10
git reflog          # HEAD 最近移动过的地方
```

`reflog` 是本地操作日志，能帮你找到“消失”的提交。它默认保留一段时间，但不是永久备份。

## 场景一：改了文件，还没提交

```bash
# 撤销工作区中某个文件的修改
git restore 文件名

# 撤销所有未暂存的修改
git restore .

# 把已暂存的文件退回未暂存
git restore --staged 文件名
```

`git restore` 会丢弃工作区修改，执行前确认这个文件没有你想保留的内容。

## 场景二：提交了，但想改提交信息

```bash
git commit --amend -m "新的提交信息"
```

如果提交已经推送到远程，`amend` 会改写历史，需要 force push。多人协作的分支上慎用。

## 场景三：想撤销最近一次提交

### 保留修改，只撤销提交

```bash
git reset --soft HEAD~1
```

提交回到暂存区，文件内容不变。

### 保留修改，取消暂存

```bash
git reset HEAD~1
```

提交回到工作区，文件内容不变。

### 丢弃提交和修改

```bash
git reset --hard HEAD~1
```

这会永久丢弃这次提交和工作区修改。执行前先确认没有需要保留的内容。

## 场景四：已经推送的提交要撤销

不要对共享分支执行 `reset --hard` 后强推。更安全的做法是生成一个反向提交：

```bash
git revert HEAD
git push
```

`revert` 不会删除历史，而是新增一次“撤销某次提交”的提交，适合多人协作。

## 场景五：分支被删了

先找提交哈希：

```bash
git reflog
```

找到类似 `abc1234 HEAD@{3}: commit: ...` 的记录后：

```bash
git switch -c recovered-branch abc1234
```

如果提交还在，就能把分支恢复出来。

## 场景六：合并到一半想放弃

```bash
git merge --abort
```

如果已经提交了合并，使用 `git revert -m 1 合并提交哈希` 撤销，而不是 `reset`。

## 一张表看懂 reset 的三种模式

| 命令 | 提交 | 暂存区 | 工作区 |
| --- | --- | --- | --- |
| `git reset --soft HEAD~1` | 撤销 | 保留 | 保留 |
| `git reset HEAD~1` | 撤销 | 撤销 | 保留 |
| `git reset --hard HEAD~1` | 撤销 | 撤销 | 丢弃 |

## 练习：救回一次误删

1. 在一个练习分支上提交一个文件。
2. 用 `git branch -D` 删除这个分支。
3. 用 `git reflog` 找到提交哈希。
4. 用 `git switch -c rescue/我的分支 <哈希>` 恢复。
5. 确认文件回来了。

## 安全习惯

- 执行 `reset --hard`、`clean -fd`、force push 前，先运行 `git status` 和 `git log`。
- 重要工作先提交，再实验。
- 不确定时，先创建一个备份分支：`git branch backup/before-experiment`。
- 不要把“恢复”当成常规操作；能提前提交和开分支，成本更低。
