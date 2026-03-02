# SefWorks Skills - AI Agent Skills 库

个人创建的 AI Agent Skills 库，包含各种技能模块和配置文件。

## 📁 项目结构

```
skills/
├── skills/              # Skill 模块目录
│   ├── conductor-*/     # Conductor 系列技能
│   └── ...              # 其他技能模块
├── spec/                # Agent Skills 规范文档
│   └── Agent Skills Spec.md
├── docs/                # 项目文档
├── references/          # 参考资料
└── dist/                # 构建输出目录
```

## 📚 Skills 索引

| Skill 名称 | 分类 | 简介 |
| :--- | :--- | :--- |
| `bmad-brainstorming-coach` | Creative | 引导创新工作坊、头脑风暴会议和创意激发的 BMad 专家代理。 |
| `conductor-setup` | Dev | 初始化项目 Conductor 环境，建立产品定义与技术栈标准。 |
| `conductor-newtrack` | Dev | 开启新功能或修复任务 (Track)，引导规格定义与任务规划。 |
| `conductor-implement` | Dev | 执行 Track 计划中的任务，确保代码符合 TDD 与项目规范。 |
| `conductor-status` | Dev | 提供项目进度全景视图，展示所有 Track 的活跃状态与后续步骤。 |
| `conductor-review` | Dev | 担任首席架构师角色，对代码与实现方案进行深度审查。 |
| `conductor-revert` | Dev | 智能撤销 Track/Phase/Task，并同步更新 Conductor 计划与文档。 |
| `conductor-upgrade` | Dev | 自动化同步 Conductor 技能套件至最新参考版本（v0.3.1）。 |

## 🚀 技能分类

- **Development & Technical** - 开发与技术类技能
- **Creative & Design** - 创意与设计类技能
- **Enterprise & Communication** - 企业协作与沟通技能
- **Document Skills** - 文档处理技能

## 🛠️ 工具集成

- **BMad-Method** - AI 驱动的开发工作流框架 (v6.0.4)
- **Git Worktree** - 多分支并行开发支持
- **Claude Code** - 主要 AI 编程助手

## 📝 常用命令

```bash
# BMad 工作流
/bmad-help
/bmad-bmm-create-product-brief

# Git 操作
/git-commit
/git-worktree add <feature>
/git-cleanBranches --dry-run

# 功能开发
/zcf:feat
```

## 📦 环境配置

项目使用 `.gitignore` 忽略以下目录：
- `.bmad-core/` - BMad 核心文件
- `.bmad/` - BMad 配置目录
- `_bmad-output/` - 构建输出
- `.agents/` - Agent 配置

## 🔗 相关资源

- [BMad Method 文档](https://docs.bmad-method.org/)
- [BMad Discord 社区](https://discord.gg/gk8jAdXWmj)
