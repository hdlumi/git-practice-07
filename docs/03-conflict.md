# 冲突：当 Git 无法替你做出选择

## 冲突是怎么发生的

合并两个分支时，如果它们都修改了同一个文件的同一区域，Git 不能猜测你想保留哪一个版本，就会把冲突交给你处理。冲突不是错误，而是 Git 在说：“这里需要人的判断。”

## 先制造一次冲突

在项目根目录：

```bash
git switch main
git switch -c exercise/conflict-a
```

把 `exercises/03-conflict/conflict-demo.md` 中的“我选择：待填写”改成：

```text
我选择：先掌握分支与合并
```

提交：

```bash
git add exercises/03-conflict/conflict-demo.md
git commit -m "docs: 冲突练习版本 A"
```

回到 `main`，从同一个起点创建另一个分支：

```bash
git switch main
git switch -c exercise/conflict-b
```

把同一行改成：

```text
我选择：先掌握冲突解决
```

提交：

```bash
git add exercises/03-conflict/conflict-demo.md
git commit -m "docs: 冲突练习版本 B"
```

合并 A，再合并 B：

```bash
git switch main
git merge --no-ff exercise/conflict-a -m "merge: 合入冲突练习 A"
git merge --no-ff exercise/conflict-b -m "merge: 合入冲突练习 B"
```

第二次合并会停下来，`git status` 会显示 `both modified`。

## 读懂冲突标记

打开冲突文件，会看到类似内容：

```text
<<<<<<< HEAD
我选择：先掌握分支与合并
=======
我选择：先掌握冲突解决
>>>>>>> exercise/conflict-b
```

- `<<<<<<< HEAD` 到 `=======` 之间：当前分支（这里是 `main`）的内容
- `=======` 到 `>>>>>>>` 之间：被合并分支的内容
- 三行标记必须全部删除，只留下你最终想要的内容

## 解决冲突的四个步骤

### 1. 看清双方改了什么

```bash
git status
git diff
git log --oneline --left-right main...exercise/conflict-b
```

### 2. 手动编辑文件

把冲突区域改成最终版本，例如：

```text
我选择：先掌握分支与合并，再练习冲突解决
```

删除 `<<<<<<<`、`=======`、`>>>>>>>` 三行标记。不要保留任何一行。

### 3. 检查是否还有标记

```bash
git diff --check
python -m gitpractice check
```

`git diff --check` 会提示空白错误；`check` 会扫描 `exercises/` 下是否还有冲突标记。

### 4. 标记已解决并提交

```bash
git add exercises/03-conflict/conflict-demo.md
git commit -m "fix: 解决冲突练习中的合并冲突"
```

提交后，`git status` 应该显示工作区干净。

## 想放弃这次合并

```bash
git merge --abort
```

仓库会回到合并前。注意：这会丢弃你为解决冲突所做的未提交修改。

## 常见错误

- **只删了一部分标记**：`<<<<<<<` 和 `>>>>>>>` 还在，文件仍然是坏的。
- **直接 `git add .` 后提交**：没有检查内容，可能把冲突标记带进历史。
- **在冲突未解决时切换分支**：Git 可能拒绝，先解决或 `git merge --abort`。
- **用 `--ours` / `--theirs` 无脑选一边**：能快速通过，但可能丢掉另一边的有效修改。

## 验收标准

- `git status` 不再显示 `both modified`
- 冲突文件中没有任何冲突标记
- `python -m gitpractice check` 通过
- `git log --graph` 能看到解决冲突的合并提交
- 能说出 `HEAD` 和 `exercise/conflict-b` 分别代表哪一边
