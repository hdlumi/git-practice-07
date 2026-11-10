# git-practice-07

> 一个面向 Git 初学者的中文分支练习沙盒：在可复现的小仓库里练习分支、合并、冲突解决和 PR 流程。

**许可证：MIT** · **Python 3.10+** · **Git 2.30+** · **当前版本：v0.1.0**

## 这个项目解决什么问题

很多 Git 初学者看完教程后，仍然不敢在真实项目里创建分支、合并代码或解决冲突，因为担心把仓库弄坏。`git-practice-07` 把常见的协作场景拆成 5 个渐进式练习，每个练习都有清晰的目标、操作步骤和验收标准，可以反复重来。

项目本身也是一个真实的小型开源项目：包含命令行工具、测试、Issue 模板、贡献指南和 MIT 许可证，适合作为学习 Git 工作流的练手仓库。

## 你会练到什么

- 创建、切换、删除分支
- 使用 `git merge` 合并分支，理解快进合并与 `--no-ff`
- 制造并解决一次真实的合并冲突
- 模拟 Fork → Branch → Pull Request 的协作流程
- 使用 `git restore`、`git revert`、`git reflog` 恢复误操作
- 用 `git log --graph` 阅读分支历史

## 快速开始

```bash
git clone https://github.com/hdlumi/git-practice-07.git
cd git-practice-07

# 检查 Python 与 Git 环境
python -m gitpractice doctor

# 检查练习文件和未解决的冲突标记
python -m gitpractice check
```

> 如果 `python` 命令不可用，请尝试 `py -3` 或 `python3`。

## 练习路线

| 编号 | 练习 | 关键命令 | 难度 |
| --- | --- | --- | --- |
| 01 | 创建并切换分支 | `git switch -c` | 入门 |
| 02 | 合并分支 | `git merge` | 入门 |
| 03 | 解决合并冲突 | `git merge` + 手动编辑 | 进阶 |
| 04 | 模拟 Pull Request | `git push` / PR | 进阶 |
| 05 | 恢复误操作 | `git restore` / `revert` / `reflog` | 进阶 |

每个练习的详细步骤见 [`exercises/README.md`](exercises/README.md)。

## 项目结构

```text
git-practice-07/
├─ README.md
├─ LICENSE
├─ CONTRIBUTING.md
├─ CODE_OF_CONDUCT.md
├─ CHANGELOG.md
├─ ROADMAP.md
├─ pyproject.toml
├─ gitpractice/
│  ├─ __init__.py
│  ├─ __main__.py
│  ├─ cli.py
│  └─ checks.py
├─ tests/
├─ docs/
│  ├─ 00-quickstart.md
│  ├─ 01-branch.md
│  ├─ 02-merge.md
│  ├─ 03-conflict.md
│  ├─ 04-pr.md
│  └─ 05-recovery.md
├─ exercises/
│  ├─ 01-branch/
│  ├─ 02-merge/
│  ├─ 03-conflict/
│  ├─ 04-pr/
│  └─ 05-recovery/
└─ .github/
   ├─ ISSUE_TEMPLATE/
   └─ workflows/ci.yml
```

## 命令行工具

```bash
# 查看 Python、Git 和当前仓库状态
python -m gitpractice doctor

# 检查必需文件是否齐全，以及是否存在未解决的冲突标记
python -m gitpractice check
```

`check` 在发现问题时返回非 0 退出码，因此也可以放进 CI 或提交前检查中使用。

## 分支模型

项目采用轻量分支模型：

```text
main       稳定分支，只接受经过验证的合并
└─ dev      集成分支，日常开发在这里汇总
   ├─ feature/xxx   新功能
   ├─ docs/xxx      文档改进
   └─ fix/xxx       缺陷修复
```

提交信息使用 `type: 简短说明` 的形式，例如：

```text
feat: 增加冲突标记检查
docs: 补充 PR 练习步骤
fix: 修复 Windows 下的路径显示
```

## 参与贡献

欢迎提交 Issue 和 Pull Request。开始之前请阅读：

- [贡献指南](CONTRIBUTING.md)
- [行为准则](CODE_OF_CONDUCT.md)
- [路线图](ROADMAP.md)

如果你是第一参与开源，可以从带 `good first issue` 标签的任务开始。

## 许可证

本项目使用 [MIT License](LICENSE)。你可以自由使用、修改和分发，但请保留版权声明和许可证文本。

## 课程背景

本项目最初作为《开源文化运动》课程实践项目创建，项目编号 `07`。项目会持续维护，欢迎把它当作 Git 分支练习的起点。
