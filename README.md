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

## 🚀 技能分类

- **Development & Technical** - 开发与技术类技能
- **Creative & Design** - 创意与设计类技能
- **Enterprise & Communication** - 企业协作与沟通技能
- **Document Skills** - 文档处理技能

## 🛠️ 工具集成

- **BMad-Method** - AI 驱动的开发工作流框架 (v6.0.3)
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
