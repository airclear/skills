---
name: vela-project-init
description: |
  天帆 (Vela) AI 原生产研平台 - 项目初始化。当用户想要初始化新项目、创建项目目录结构、搭建 AI-Native SDLC 项目骨架时使用。
  关键词触发：初始化项目、新建项目、vela init、项目骨架、创建项目结构、project init、scaffold project、AI 原生项目。
  即使用户只说"帮我建个新项目"或"按 vela 结构初始化"也应触发此 Skill。
---

# 天帆 Vela - AI 原生产研平台项目初始化

本 Skill 帮助在任意目录中快速搭建符合 Vela AI-Native SDLC 规范的完整项目骨架。

## 目录结构设计

```
{project-root}/
├── .vela/                  # Vela 平台配置（AI 协作上下文、规范文档）
│   ├── AGENTS.md           # AI Agent 入口（含完整项目上下文）
│   ├── PROJECT_GUIDE.md    # 项目指引
│   ├── tech-stack.md       # 技术栈决策记录
│   ├── code_styleguides/   # 代码规范
│   └── conductor/          # Conductor 任务管理（由 /conductor-setup 初始化）
│       └── README.md       # 提示用户运行 /conductor-setup
├── prd/                    # 需求大脑
│   ├── 00_vision/          # 产品愿景与路线图
│   ├── 01_inbox/           # 原始需求池
│   ├── 02_prd/             # 正式 PRD 文档
│   └── prototype/          # UI 原型（按前端分组）
├── src/                    # 源码实现层
│   ├── frontend-{name}/    # 前端应用（按角色，可多个）
│   └── backend/            # 后端服务
├── test/                   # 质量保障层
│   ├── e2e/
│   └── reports/
├── ops/                    # 运维部署层
├── changelog/              # 变更记录
└── docs/                   # 项目文档
    ├── architecture/
    ├── api/
    └── release-artifacts/
```

**设计要点**：
- `.vela/` 收纳所有 AI 协作配置，与业务代码分离
- `src/` 统一承载前后端代码，结构清晰
- `conductor/` 只创建目录 + README，实际初始化由 `/conductor-setup` 完成

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
python {SKILL_DIR}/scripts/init_project.py \
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
   - 运行 `/conductor-setup` 初始化 Conductor 任务管理
   - 运行 `/conductor-newtrack` 创建第一个工作 Track

---

## 注意事项

- 全程用**中文**与用户交互
- 如果脚本执行失败（Python 不可用），回退为手动用 `mkdir -p` + Write 工具逐个创建
- `README.md` 如已存在则**不覆盖**，保留用户原有内容
