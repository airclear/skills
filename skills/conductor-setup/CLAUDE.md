[根目录](../../CLAUDE.md) > [skills](../) > **conductor-setup**

---

# conductor-setup

## 模块职责

**Scaffolds 项目并设置 Conductor 环境，用于上下文驱动开发（Context-Driven Development）。**

当开始新项目或在现有（Brownfield）项目中初始化 Conductor 工作流时使用此技能。该技能引导用户完成项目发现、产品定义、技术栈配置和初始 Track 规划。

---

## 入口与启动

**入口文件:** `SKILL.md`

**元数据:**
```yaml
name: conductor-setup
description: Scaffolds the project and sets up the Conductor environment for Context-Driven Development...
```

---

## 对外接口

本模块不直接提供 API 接口，而是通过以下协议文档定义行为：

| 协议 | 文件 |
|------|------|
| Resolution Protocol | `references/resolution-protocol.md` |
| Project Discovery | `references/project-discovery.md` |
| Product Setup | `references/product-setup.md` |
| Configuration | `references/configuration.md` |
| Track Generation | `references/track-generation.md` |

---

## 关键依赖与配置

### 工作流程阶段

1. **Project Discovery** - 判断项目是新建（Greenfield）还是现有（Brownfield）
2. **Product Definition** - 协作创建 `product.md` 和 `product-guidelines.md`
3. **Tech Stack** - 在 `tech-stack.md` 中定义技术基础
4. **Configuration** - 选择代码风格指南和自定义 `workflow.md`
5. **Track Generation** - 创建第一个工作单元（Track）的 `spec.md` 和 `plan.md`

### 状态管理

Conductor 在 `conductor/setup_state.json` 中跟踪进度。如果会话中断，必须检查此文件从 `last_successful_step` 恢复：

| 状态值 | 恢复点 |
|--------|--------|
| `2.1_product_guide` | 产品指南 |
| `2.2_product_guidelines` | Tech Stack |
| `2.3_tech_stack` | 代码风格指南 |
| `2.4_code_styleguides` | 工作流 |
| `2.5_workflow` | 初始 Track 生成 |
| `3.3_initial_track_generated` | 设置完成 |

### 资源目录

**Templates:** `assets/templates/`
- `workflow.md` - 基础开发工作流
- `code_styleguides/` - 语言特定的代码风格指南（Python, TypeScript, Go 等）

---

## 数据模型

无直接数据模型。通过 Resolution Protocol 解析以下 Conductor 工件：

- `conductor/product.md` - 产品定义
- `conductor/tech-stack.md` - 技术栈
- `conductor/workflow.md` - 工作流
- `conductor/tracks.md` - Tracks Registry

---

## 测试与质量

**测试文件:** 不直接包含可执行测试

**质量保证:**
- 遵循 Universal File Resolution Protocol 定位文件
- TDD 集成：生成 `plan.md` 时必须遵循 `workflow.md` 中定义的 TDD 原则
- Git 清理：Setup 完成后提交所有 `conductor/` 文件

---

## 常见问题 (FAQ)

**Q: 如何恢复中断的设置会话？**
A: 检查 `conductor/setup_state.json` 文件，从 `last_successful_step` 指定的步骤继续。

**Q: Brownfield 和 Greenfield 项目有什么区别？**
A: Greenfield 是全新项目，Brownfield 是现有项目。Project Discovery 阶段会检测项目类型并采用不同的初始化策略。

**Q: Setup 完成后会产生哪些文件？**
A: `conductor/` 目录下包含 `product.md`, `tech-stack.md`, `workflow.md`, `product-guidelines.md`, `tracks.md`，以及第一个 Track 的 `spec.md` 和 `plan.md`。

---

## 相关文件清单

| 文件 | 说明 |
|------|------|
| [`SKILL.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-setup/SKILL.md) | 技能主文件 |
| [`references/resolution-protocol.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-setup/references/resolution-protocol.md) | 文件定位协议 |
| [`references/project-discovery.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-setup/references/project-discovery.md) | 项目发现逻辑 |
| [`references/product-setup.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-setup/references/product-setup.md) | 产品文档创建 |
| [`references/configuration.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-setup/references/configuration.md) | 配置和模板复制 |
| [`references/track-generation.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-setup/references/track-generation.md) | Track 生成 |
| [`assets/templates/workflow.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-setup/assets/templates/workflow.md) | 工作流模板 |
| [`assets/templates/code_styleguides/`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-setup/assets/templates/code_styleguides/) | 代码风格指南模板 |

---

## 变更记录 (Changelog)

### 2026-02-24

- **Initial Module Documentation** - 创建模块级 CLAUDE.md
- 扫描覆盖率：100%（17 个文件）
