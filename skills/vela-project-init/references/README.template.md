# {{PROJECT_NAME_CN}} ({{PROJECT_NAME_EN}})

{{PROJECT_DESCRIPTION}}

---

## 1. 模块介绍

> 请在此处填写各核心模块的职责说明。

---

## 2. 技术栈

### 后端 (Backend)
{{TECH_STACK_BACKEND}}

### 前端 (Frontend)
- **框架**: Vue 3 (Composition API), TypeScript, Vite
- **状态管理**: Pinia
- **样式**: UnoCSS / Sass / Less

### 基础设施 (Infrastructure)
- **容器化**: Docker & Docker Compose
- **持续集成**: Jenkins / GitHub Actions

---

## 3. 项目结构

```text
/
├── product/            # 产品管理大脑 (AI-Native SDLC 需求入口与定义)
├── backend/            # 后端实现
├── frontend-*/         # 前端应用 (按角色分离)
├── ops/                # 运维部署
├── testbench/          # 测试台与 UX 设计稿
├── deploy/             # CI/CD 配置
├── conductor/          # Conductor 任务管理与项目上下文
└── docs/               # 项目文档 (架构, 技术设计)
```

---

## 4. 快速开始

### 前端启动
```bash
cd frontend-{name}
pnpm install
pnpm dev
```

### 后端启动
> 参考各后端模块的 README。

---

## 5. 开发与管理

本项目采用 **AI-Native SDLC** 开发模式，结合 **Conductor** 进行自动化任务管理。

- **核心指引**: 详见 `PROJECT_GUIDE.md`
- **需求入口**: 详见 `product/01_inbox/index.md`
- **任务管理**: 详见 `conductor/index.md`
- **代码规范**: 详见 `conductor/code_styleguides/`

---

© {{CURRENT_YEAR}} All Rights Reserved.
