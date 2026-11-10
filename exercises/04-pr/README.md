# 练习 04：走一遍 Pull Request

## 目标

体验真实的开源协作流程：Fork、创建分支、提交、推送、发起 PR、回应 review。

## 前提

- 已注册 GitHub 账号
- 已经把项目 Fork 到自己的账号下
- 本地配置了 Git 用户名和邮箱

## 步骤

### 1. Fork 并克隆

在 GitHub 打开 `https://github.com/hdlumi/git-practice-07`，点击 **Fork**。然后：

```bash
git clone https://github.com/你的用户名/git-practice-07.git
cd git-practice-07
git remote add upstream https://github.com/hdlumi/git-practice-07.git
```

### 2. 从 dev 创建分支

```bash
git fetch upstream
git switch -c docs/your-name-pr upstream/dev
```

### 3. 完成一个小修改

打开 `exercises/04-pr/contribution.md`，在“我的贡献”下面写一条你真实做过的改进，例如补充一条排错经验、修正一个错别字、增加一个命令示例。

```bash
git diff
git add exercises/04-pr/contribution.md
git commit -m "docs: 补充个人 PR 练习记录"
git push -u origin docs/your-name-pr
```

### 4. 发起 PR

在 GitHub 页面点击 **Compare & pull request**，确认：

- base repository 是 `hdlumi/git-practice-07`
- base 分支是 `dev`
- head 分支是你的 `docs/your-name-pr`
- 标题清楚，描述包含“改了什么、为什么改、怎么验证”

### 5. 关联 Issue

在 PR 描述中写 `Closes #Issue编号`。如果还没有 Issue，可以先在课程 Issue 中说明你想改什么，再提交 PR。

### 6. 回应 review

维护者可能会提出修改建议。继续在同一个分支提交并 push，PR 会自动更新。不要关闭 PR 后重新开一个。

## 验收标准

- [ ] PR 的目标分支是 `dev`
- [ ] 一个 PR 只做一个主题
- [ ] 描述中包含关联 Issue 和验证方式
- [ ] 没有提交 `.venv/`、`__pycache__/` 等无关文件
- [ ] 能解释 Fork 与 clone 的区别
- [ ] 能说出 PR 合并后如何同步本地 `dev`

## 提示

- 不要直接在 `main` 上改，也不要把 `main` 作为 PR 目标。
- 推送前先 `git status`，确认没有把临时文件带进去。
- 如果 push 被拒绝，先 `git pull --rebase`，不要直接 force push。
- PR 不是“提交作业”，描述要让不了解上下文的人也能看懂。
