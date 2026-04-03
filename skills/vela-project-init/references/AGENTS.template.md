# {{PROJECT_NAME_CN}} ({{PROJECT_NAME_EN}})

{{PROJECT_DESCRIPTION}}

## 核心模块

> 请在此处填写各模块的定位与职责。

## 数据链路与业务闭环

> 请描述系统的核心数据流转路径。

## 项目结构

```
{{PROJECT_NAME_EN}}/
├── product/                # 产品管理大脑 (Submodule): AI-Native SDLC 需求入口与定义
│   ├── 00_vision/          # 全局设定（愿景、路线图）
│   ├── 01_inbox/           # 原始需求池
│   ├── 02_prd/             # 已精炼的 PRD 文档
│   ├── prototype/          # UI 原型（按前端项目组织）
│   └── definition/         # 产品定义知识库
├── backend/                # 后端项目
├── frontend-*/             # 前端应用（按角色分离）
├── ops/                    # 运维中心：自动化部署工具 (Submodule)
├── testbench/              # 测试台与设计稿
├── deploy/                 # 部署配置
├── conductor/              # Conductor 任务管理与项目上下文
└── docs/                   # 项目文档
```

## 开发规范与流程

### 0. 产品与需求管理 (AI-Native SDLC)
1. **Inbox**: 所有需求源头通过 `product/01_inbox/` 录入并索引。
2. **Refine**: 通过 AI PM 精炼为 `product/02_prd/` 下的 PRD。
3. **Dispatch**: 通过 `conductor/` 将 PRD 转化为可执行的 Track 与 Plan。

### 1. 任务管理 (Conductor)
- `/conductor-newtrack` - 创建新的 Track（工作单元）
- `/conductor-status` - 查看当前项目状态
- `/conductor-implement` - 执行 Track 中定义的任务
- `/conductor-review` - 审查已完成或进行中的工作
- `/conductor-revert` - 回滚逻辑工作单元

### 2. 后端开发规范
- **分层架构**: 严格遵循 `Controller -> Service -> DAL` 分层。
- **模块依赖**: 始终通过 `api` 模块进行模块间通信，禁止直接依赖业务实现模块。

### 3. 测试规范
- **TDD**: 新功能开发强制执行 Red-Green-Refactor 流程。
- **覆盖率**: 目标 >80%。

### 4. 前端开发规范
- **代码风格**: 使用 Vue 3 `<script setup>` 语法。
- **类型检查**: 使用 `vue-tsc` 进行静态类型检查。

## 重要提醒
- **语言**: 本项目默认使用**中文**进行交流和文档编写。
- **模块依赖**: 始终通过 `api` 模块进行模块间通信。
