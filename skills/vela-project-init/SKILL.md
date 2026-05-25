---
name: vela-project-init
description: |
  天帆 (Vela) AI 原生产研平台 - 项目初始化。当用户想要初始化新项目、创建项目目录结构、搭建 AI-Native SDLC 项目骨架时使用。
  关键词触发：初始化项目、新建项目、vela init、项目骨架、创建项目结构、project init、scaffold project、AI 原生项目。
  即使用户只说"帮我建个新项目"或"按 vela 结构初始化"也应触发此 Skill。
---

# 天帆 Vela - AI 原生产研平台项目初始化

本 Skill 帮助在任意目录中快速搭建符合 Vela AI-Native SDLC 规范的完整项目骨架。

**关键原则：骨架 ≠ 实现。** 本 Skill 只创建目录结构和模板文档（README、AGENTS、PRD 模板等），绝不生成业务代码、应用框架代码（如 Spring Boot / React 脚手架）、CI/CD 配置、Dockerfile、Terraform、K8s 清单等。这些属于后续研发阶段的工作，不在项目初始化的职责范围内。

## 目录结构设计

```
{project-root}/
├── .vela/                  # Vela 平台配置（AI 协作上下文、规范文档）
│   ├── AGENTS.md           # AI Agent 入口（含完整项目上下文）
│   ├── PROJECT_GUIDE.md    # 项目指引
│   ├── tech-stack.md       # 技术栈决策记录
│   ├── code-styleguides/   # 代码规范
│   └── specs/              # SDD 技术规格（Spec-Driven Development）
├── prd/                    # 需求大脑
│   ├── 00_vision/          # 产品愿景与路线图
│   ├── 01_inbox/           # 原始需求池（唯一入口，含状态看板）
│   ├── 02_prd/             # 正式 PRD 文档
│   ├── archive/            # 已完结归档
│   │   ├── inbox/          # 归档的原始需求
│   │   └── prd/            # 归档的 PRD
│   └── prototype/          # UI 原型（按前端分组）
├── src/                    # 源码实现层
│   ├── frontend-{name}/    # 前端应用（按角色，可多个）
│   └── backend/            # 后端服务
├── tests/                  # 质量保障层
│   ├── e2e/
│   └── reports/
├── sre/                    # 运维部署层
├── changelog/              # 变更记录
└── docs/                   # 项目文档
    ├── architecture/
    ├── api/
    └── release-artifacts/
```

**设计要点**：
- `.vela/` 收纳所有 AI 协作配置，与业务代码分离
- `src/` 统一承载前后端代码，结构清晰
- **不包含 `conductor/` 目录**（Conductor 任务管理已移除，由 `.vela/specs/` + `plan.md` 替代）
- 初始化只做骨架，不做实现：`src/` 下仅创建空目录，不生成任何业务代码或框架脚手架

**核心工作流**：
```
01_inbox → 02_prd → .vela/specs/ → plan.md → src/
(需求录入)  (需求精炼)  (SDD技术规格)  (实施计划)  (研发实现)
```

---

## 执行步骤

### 第一步：收集项目信息

向用户询问以下信息（已在对话中提供则跳过）：

1. **项目名称**（中文全称 + 英文代号）
2. **项目简介**（一句话描述）
3. **目标目录**（绝对路径）
4. **前端应用列表**（如 `frontend-desktop,frontend-web`，没有则跳过）
5. **后端技术栈**（如 `Java/Spring Boot`，未定则填"待定"）

整理成确认列表给用户确认，**不要反复追问**，确认后立刻执行。

### 第二步：运行初始化脚本

直接调用 `scripts/init_project.py`，路径为本 Skill 目录下的 `scripts/init_project.py`：

```bash
python3 {SKILL_DIR}/scripts/init_project.py \
  --name-cn "{PROJECT_NAME_CN}" \
  --name-en "{PROJECT_NAME_EN}" \
  --desc "{PROJECT_DESCRIPTION}" \
  --dir "{TARGET_DIR}" \
  --frontends "{FRONTEND_LIST}" \
  --backend "{BACKEND_TECH}"
```

`{SKILL_DIR}` 是本 Skill 的安装路径（通常为 `~/.claude/skills/vela-project-init`）。

脚本会自动完成：目录创建 → 模板文件写入 → git init & initial commit。

**幂等性**：已存在的文件会跳过，不覆盖。

### 第三步：输出完成摘要

脚本执行完毕后，告知用户：

1. 已创建的结构概览
2. 下一步建议：
   - 填写 `prd/00_vision/vision.md` 产品愿景
   - 需求录入 `prd/01_inbox/`，参考 `_example/` 示例格式
   - 需求精炼到 `prd/02_prd/`，SDD 技术规格写入 `.vela/specs/`

---

## 注意事项

- 全程用**中文**与用户交互
- 如果脚本执行失败（Python 不可用），回退为手动用 `mkdir -p` + Write 工具逐个创建
- `README.md` 如已存在则**不覆盖**，保留用户原有内容
