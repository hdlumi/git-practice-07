# 贡献指南

感谢你愿意改进 `git-practice-07`。这个项目的目标不是堆很多功能，而是把 Git 学习路径做得清楚、可复现、对新手友好。

## 开始之前

- 请先阅读 [README](README.md) 和 [行为准则](CODE_OF_CONDUCT.md)。
- 如果你要修一个较大的问题，建议先开 Issue 说明想法，避免重复劳动。
- 所有参与者都应遵守行为准则。

## 本地开发

```bash
git clone https://github.com/hdlumi/git-practice-07.git
cd git-practice-07

# 检查环境
python -m gitpractice doctor

# 运行测试
python -m unittest discover -s tests -v

# 检查练习文件
python -m gitpractice check
```

项目没有第三方运行时依赖，只需要 Python 3.10+ 和 Git。

## 分支命名

从最新的 `dev` 分支创建：

| 类型 | 命名示例 | 用途 |
| --- | --- | --- |
| 功能 | `feature/check-command` | 新功能 |
| 文档 | `docs/quickstart` | 文档改进 |
| 修复 | `fix/windows-path` | 缺陷修复 |
| 练习 | `exercise/conflict-a` | 课程练习 |

不要直接向 `main` 提交。`main` 只接受经过验证的合并。

## 提交信息

使用 `type: 简短说明`：

```text
feat: 增加冲突标记检查
fix: 修复 Windows 下的路径显示
docs: 补充 PR 练习步骤
test: 增加缺少文件时的测试
chore: 更新忽略规则
```

一次提交只做一件事。提交前请运行测试和 `check`。

## Pull Request

1. Fork 仓库并从 `dev` 创建分支。
2. 完成修改，补充或更新测试。
3. 运行 `python -m unittest discover -s tests -v`。
4. 运行 `python -m gitpractice check`。
5. 提交 PR，写清楚“改了什么、为什么改、怎么验证”。
6. 等待维护者 review；根据意见继续提交。

PR 描述可以参考 `.github/PULL_REQUEST_TEMPLATE.md`。

## 文档风格

- 使用简体中文，命令和代码使用英文。
- 命令块注明操作系统差异时，优先给出 Windows 和 macOS/Linux 两种写法。
- 不写“显然”“很简单”等会让新手有压力的表达。
- 新增练习时，必须包含：目标、步骤、验收标准、常见问题。

## 许可证

提交贡献即表示你同意以 [MIT License](LICENSE) 发布你的贡献。
