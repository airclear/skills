# Skills - AI Agent Skills 库

自用 AI Agent Skills 库，包含各种技能模块和配置文件。

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
| `bmad-core` | Creative | BMad 核心工具：头脑风暴 (BSP)、多代理协作 (Party Mode)、文档切片与审阅。 |
| `bmad-bmm` | Dev | 完整 SDLC 工作流 (BMM)：需求分析、PRD/UX 设计、架构定义、Sprint 故事开发、代码审查。 |
| `bmad-tea` | QA | 企业级测试架构 (TEA)：测试设计、ATDD、自动化测试、CI 流水线配置、质量审计。 |
| `bmad-sync` | Maintenance | 维护工具：一键同步 BMad 源码至各聚合 Skill，确保版本一致性。 |
| `bmad-brainstorming-coach` | Creative | 引导创新工作坊、头脑风暴会议和创意激发的 BMad 专家代理。 |
| `conductor-setup` | Dev | 初始化项目 Conductor 环境，建立产品定义与技术栈标准 (v0.3.1)。 |
| `conductor-newtrack` | Dev | 开启新功能或修复任务 (Track)，引导规格定义与任务规划 (v0.3.1)。 |
| `conductor-implement` | Dev | 执行 Track 计划中的任务，确保代码符合 TDD 与项目规范 (v0.3.1)。 |
| `conductor-status` | Dev | 提供项目进度全景视图，展示所有 Track 的活跃状态与后续步骤 (v0.3.1)。 |
| `conductor-review` | Dev | 担任首席架构师角色，对代码与实现方案进行深度审查 (v0.3.1)。 |
| `conductor-revert` | Dev | 智能撤销 Track/Phase/Task，并同步更新 Conductor 计划与文档 (v0.3.1)。 |
| `conductor-upgrade` | Maintenance | 自动化同步 Conductor 技能套件至最新参考版本 (v0.3.1)。 |


## 🔗 相关资源

- [BMad Method 文档](https://docs.bmad-method.org/)
- [Conductor Repo](https://github.com/gemini-cli-extensions/conductor)
