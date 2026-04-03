# {{PROJECT_NAME_CN}} 项目指引 (Project Guide)

欢迎加入 **{{PROJECT_NAME_CN}}**！本项目采用 **AI-Native SDLC** 开发模式，通过目录结构映射研发全生命周期的各个环节。

## 1. 核心目录架构

- **`product/` (大脑与入口)**: 所有的需求源头和产品定义。
    - `00_vision/`: 产品的"北极星"，包含愿景、领域模型和非功能性约束。
    - `01_inbox/`: 原始需求池。无论是用户反馈、技术债还是运维建议，先扔进这里。
    - `02_prd/`: 加工后的 PRD。是 Conductor 和研发的直接输入。
- **`conductor/` (指挥官)**: 任务调度与执行计划。管理所有的 Track 和 Plan。
- **`backend/` / `frontend-*/`**: 研发实现层。遵循 TDD 模式。
- **`testbench/`**: 测试与实验工作台。包含设计稿原型和测试脚本。
- **`ops/`**: 运维与部署层。包含 Docker 和 CI/CD 配置。

## 2. AI 协作工作流

### 第一步：需求录入 (Inbox)
将想法或反馈以 Markdown 形式放入 `product/01_inbox/` 对应的子目录。

### 第二步：需求精炼 (PRD)
调用 `Product Manager Agent` 读取 Inbox，结合 `00_vision/` 生成结构化的 PRD 存入 `product/02_prd/`。

### 第三步：任务分发 (Conductor)
调用 `Conductor Agent` 根据 PRD 创建新的 Track，并在 `conductor/tracks/` 下生成 `spec.md` 和 `plan.md`。

### 第四步：研发实现 (Implementation)
研发（或 AI Agent）按照 `plan.md` 执行任务，遵循 **Red-Green-Refactor** (TDD) 流程。

### 第五步：验证与部署 (Ops/Test)
通过 `testbench/` 进行验证，并通过 `ops/` 脚本推送到环境。

## 3. 开发规范摘要

- **TDD**: 强制执行。没有测试的代码是不完整的。
- **Commit**: 遵循约定式提交 (Conventional Commits)。
- **API**: 模块间通信必须通过 `-api` 模块（后端）。
- **语言**: 项目文档和交流默认使用中文。

---
*更多细节请参考各子目录下的 `README.md`。*
