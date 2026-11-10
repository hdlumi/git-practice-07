# 练习 03：解决合并冲突

## 目标

亲手制造一次冲突，读懂冲突标记，并提交一个干净的解决结果。

## 场景

两位同学都想修改“学习路线”这一行，而且都认为自己的顺序更好。Git 无法替他们决定，于是产生冲突。

## 步骤

### 1. 准备两个分支

```bash
git switch main
git switch -c exercise/conflict-a
```

打开 `exercises/03-conflict/conflict-demo.md`，把“我选择：待填写”改成：

```text
我选择：先掌握分支与合并
```

提交：

```bash
git add exercises/03-conflict/conflict-demo.md
git commit -m "docs: 冲突练习版本 A"
```

### 2. 创建另一个分支

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

### 3. 合并并触发冲突

```bash
git switch main
git merge --no-ff exercise/conflict-a -m "merge: 合入冲突练习 A"
git merge --no-ff exercise/conflict-b -m "merge: 合入冲突练习 B"
```

第二次合并会失败，这是预期结果。

### 4. 解决冲突

打开 `conflict-demo.md`，你会看到三行特殊标记，分别表示当前分支、分隔线和另一个分支。把整段改成你最终想要的内容，例如：

```text
我选择：先掌握分支与合并，再练习冲突解决
```

确认文件里不再有任何冲突标记，然后：

```bash
git diff --check
python -m gitpractice check
git add exercises/03-conflict/conflict-demo.md
git commit -m "fix: 解决 03 冲突练习"
```

## 验收标准

- [ ] 合并过程中真实出现过冲突
- [ ] 冲突文件里没有任何冲突标记
- [ ] `python -m gitpractice check` 通过
- [ ] `git log --graph` 中能看到解决冲突的合并提交
- [ ] 能说出冲突标记三部分分别代表什么

## 提示

- 冲突标记是“小于号开头、等号分隔、大于号结尾”的三行，必须全部删除。
- 不要保留任何一方原样不动；最终内容应该是你有意识的选择。
- 想放弃：`git merge --abort`，它会回到合并前。
