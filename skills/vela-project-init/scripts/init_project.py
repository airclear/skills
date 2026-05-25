#!/usr/bin/env python3
"""
Vela Project Initializer
天帆 AI 原生产研平台 - 项目骨架初始化脚本

Usage:
    python init_project.py \
        --name-cn "项目中文名" \
        --name-en "ProjectEN" \
        --desc "一句话描述" \
        --dir /path/to/project \
        --frontends "frontend-desktop,frontend-web" \
        --backend "Java/Spring Boot"
"""

import argparse
import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

# ── 模板内容 ────────────────────────────────────────────────────────────────

TEMPLATES = {

".gitignore": """\
# OS
.DS_Store
Thumbs.db

# IDE
.idea/
.vscode/
*.swp
*.swo

# Node / Frontend
node_modules/
dist/
.pnpm-store/
.yarn/cache/

# Rust / Tauri
target/

# Java / Backend
*.class
*.jar
*.war

# Logs
*.log
logs/

# Environment
.env
.env.local
.env.*.local

# Build artifacts
build/
out/

# Test coverage
coverage/
.nyc_output/

# AI tooling state
.omc/state/
.omc/sessions/
.claude/worktrees/
""",

"README.md": """\
# {name_cn} ({name_en})

> {desc}

---

## 项目结构

```text
/
├── .vela/              # Vela 平台配置（AI 协作上下文、SDD 规格）
├── prd/                # 产品管理大脑 (AI-Native SDLC 需求入口)
├── src/                # 源码实现层
│   ├── frontend-*/     # 前端应用（按角色分离）
│   └── backend/        # 后端服务
├── tests/              # 质量保障层
├── sre/                # 运维部署层
├── changelog/          # 变更记录
└── docs/               # 项目文档（架构、技术设计）
```

---
**核心工作流**: `01_inbox → 02_prd → .vela/specs/ → plan.md → src/`

---

## 快速开始

### 前端
```bash
cd src/frontend-xxx
pnpm install && pnpm dev
```

### 后端
> 参考 `src/backend/` 下各模块的 README。

---

## 开发与管理

- **核心指引**: `.vela/PROJECT_GUIDE.md`
- **需求入口**: `prd/01_inbox/index.md`
- **任务管理**: 使用 AI Skills 管理研发任务
- **代码规范**: `.vela/code_styleguides/`

---

© {year} All Rights Reserved.
""",

".vela/PROJECT_GUIDE.md": """\
# {name_cn} ({name_en}) 项目指引

欢迎加入 **{name_cn}**！本项目采用 **AI-Native SDLC** 开发模式。

## 核心目录

| 目录 | 职责 |
|------|------|
| `prd/` | 需求大脑：Inbox → PRD 全生命周期 |
| `src/` | 研发实现：前端 + 后端代码 |
| `tests/` | 质量保障：测试策略与执行 |
| `sre/` | 运维部署：IaC、CI/CD |
| `.vela/` | 平台上下文：AI 协作配置 |

## AI 协作工作流

```
01_inbox → 02_prd → .vela/specs/ → plan.md → src/
(需求录入)  (需求精炼)  (SDD技术规格)  (实施计划)  (研发实现)
```

1. **需求录入** → `prd/01_inbox/` 创建需求目录，参考 `_example/` 格式
2. **需求精炼** → AI PM 评审后生成 PRD 到 `prd/02_prd/`
3. **SDD 规格** → 技术规格写入 `.vela/specs/`，细化到可实现的颗粒度
4. **实施计划** → 基于 Specs 生成 `plan.md`，拆分为可执行步骤
5. **研发实现** → TDD 流程，`tests/` 验证 → `sre/` 部署

## 开发规范

- **TDD**: 强制执行，红绿重构三步走
- **Commit**: Conventional Commits 规范
- **技术栈变更**: 先更新 `.vela/tech-stack.md`，再动代码
- **语言**: 项目文档默认中文

## AI 协作任务管理

> 本项目使用 AI Skills 管理研发任务，任务状态与执行计划随代码一起版本管理。
""",

".vela/AGENTS.md": """\
# {name_cn} ({name_en})

> {desc}

## 项目概述

本项目采用 **Vela AI-Native SDLC** 规范，所有产研要素统一纳入 Git Monorepo 目录管理。

## 目录结构

```
/
├── .vela/              # Vela 平台配置（本目录）
│   ├── AGENTS.md       # 本文件（AI Agent 入口）
│   ├── PROJECT_GUIDE.md
│   └── specs/           # SDD 技术规格
├── prd/                # 需求大脑
│   ├── 00_vision/      # 产品愿景与路线图
│   ├── 01_inbox/       # 原始需求池（唯一入口，含状态看板）
│   ├── 02_prd/         # 正式 PRD 文档
│   ├── archive/        # 已完结归档
│   │   ├── inbox/
│   │   └── prd/
│   └── prototype/      # UI 原型
├── src/                # 源码实现
{src_list}
├── tests/              # 测试
├── sre/                # 运维部署
├── changelog/          # 变更记录
└── docs/               # 文档
```

## 开发规范摘要

- **TDD**: 强制执行，没有测试的代码是不完整的
- **Commit**: 遵循约定式提交 (Conventional Commits)
- **模块间通信**: 通过 api 层，禁止跨模块直接依赖
- **语言**: 项目文档和交流默认使用中文
""",


"prd/README.md": """\
# 产品管理大脑 (Product Management Brain)

## 目录结构

```
prd/
├── 00_vision/          # 全局设定（愿景、路线图）
├── 01_inbox/           # 原始需求池（唯一入口，含状态看板）
│   └── index.md        # 需求索引（含 PRD 链接列）
├── 02_prd/             # 已精炼的 PRD
│   └── index.md        # PRD 索引
├── archive/            # 已完结归档
│   ├── inbox/          # 归档的原始需求
│   └── prd/            # 归档的 PRD
└── prototype/          # UI 原型（按前端分组）
```

## 需求流转

```
01_inbox → 02_prd → .vela/specs/ → plan.md → src/ → archive/
```

## 命名规范

- **Inbox**: `[三位编号]_[来源]_[描述]`，如 `001_market_auth`
- **PRD**: `P[三位编号]_[特性]`，如 `P001_user_onboarding`

## 归档规范

需求完结后同步操作：
1. `mv prd/01_inbox/001_xxx/  prd/archive/inbox/`
2. `mv prd/02_prd/P001_xxx/   prd/archive/prd/`
3. 在 `01_inbox/index.md` 中将状态改为"已归档"
""",

"prd/00_vision/vision.md": """\
# 产品愿景: {name_cn}

## 一句话愿景

{desc}

## 核心定位

> 请在此处描述产品的核心价值主张（3 个核心维度）。

## 目标用户

> 描述主要使用场景和用户群体。

## 成功指标

> 定义可量化的关键指标 (OKR/KPI)。
""",

"prd/00_vision/roadmap.md": """\
# 演进路线图 (Roadmap): {name_cn}

## 当前阶段

> 描述当前所处的里程碑阶段。

## 近期目标 (本季度)

- [ ] ...

## 中期目标 (下季度)

- [ ] ...

## 长期愿景

> 描述 12-18 个月的战略方向。

---
*更新日期: {year}*
""",

"prd/01_inbox/index.md": """\
# 01_inbox - 原始需求池

> 所有需求的唯一入口，在此维护需求全生命周期状态。

## 需求索引

| ID | 目录 | 标题 | 来源 | 状态 | PRD |
|----|------|------|------|------|-----|
| - | - | - | - | - | - |

## 状态说明

- **待分析**: 原始需求，尚未分析
- **分析中**: 正在调研与设计
- **已转化为PRD**: 已生成 PRD，见 `02_prd/`（PRD 列填写链接）
- **已归档**: 已完结，移入 `archive/`
- **已拒绝**: 需求被否决，保留记录

## 录入规范

1. 目录命名: `[三位编号]_[来源]_[描述]`
2. 必含文件: `requirement.md`
3. 附件目录: `_resources/`
4. 录入后更新本索引
5. 需求完结后：将目录移至 `archive/inbox/`，状态改为"已归档"
""",

"prd/02_prd/index.md": """\
# 02_prd - PRD 文档库

## PRD 索引

| ID | 目录 | 标题 | 状态 | 关联 Inbox |
|----|------|------|------|-----------|
| - | - | - | - | - |

## 状态: 草稿 → 评审中 → 已批准 → 开发中 → 已发布 → 已归档

## 命名规范: `P[三位编号]_[特性]`，如 `P001_user_auth`

## 归档说明

需求完结后，将对应目录移至 `archive/prd/`，并在 `01_inbox/index.md` 中将状态更新为"已归档"。
""",

"prd/archive/README.md": """\
# archive - 已完结需求归档

存放已完结（已发布或已关闭）的需求与 PRD，保持 `01_inbox/` 和 `02_prd/` 目录清爽。

## 目录结构

```
archive/
├── inbox/    # 已归档的原始需求（从 01_inbox/ 移入）
└── prd/      # 已归档的 PRD（从 02_prd/ 移入）
```

## 归档操作

```bash
# 归档一条需求（inbox + prd 同步操作）
mv prd/01_inbox/001_xxx/  prd/archive/inbox/001_xxx/
mv prd/02_prd/P001_xxx/   prd/archive/prd/P001_xxx/
```

归档后在 `01_inbox/index.md` 中将对应行状态改为"已归档"。
""",

".vela/specs/README.md": """\
# SDD 技术规格 (Spec-Driven Development)

将 PRD 转化为可实现的技术规格，确保研发有明确的技术输入。

## 规格文件命名

`{feature-name}.md`，如 `user-auth.md`、`payment-flow.md`

## 规格文档模板

每个 Spec 文件应包含：

1. **概述** — 一句话描述本规格覆盖的功能范围
2. **技术方案** — 架构设计、技术选型决策
3. **接口定义** — API 端点、数据模型、协议
4. **关键流程** — 核心业务逻辑的伪代码或流程图描述
5. **边界条件** — 异常处理、降级策略、性能指标
6. **测试要点** — 关键测试场景与验收标准

## 示例

参见 `prd/02_prd/_example/` 中从 PRD 到 Spec 的对照示例。
""",

"prd/01_inbox/_example/requirement.md": """\
# 示例需求: 用户身份认证

## 需求来源

- **提出人**: 产品团队
- **日期**: {year}-{month}
- **优先级**: P0 (核心)

## 需求描述

用户需要通过邮箱+密码方式注册并登录系统，支持密码重置。

## 目标用户

所有使用本产品的终端用户。

## 预期效果

- 用户可自主注册账号
- 登录后访问受保护资源
- 忘记密码时可自助重置

## 验收标准

1. 新用户填写邮箱、密码后可成功注册
2. 已注册用户使用正确凭据可登录
3. 错误凭据显示友好提示，不暴露具体原因
4. 密码重置邮件 5 分钟内送达

## 附件

> 相关截图、文档等放入 `_resources/` 目录
""",

"prd/02_prd/_example/prd.md": """\
# P000: 用户身份认证 PRD (示例)

> 状态: 示例 | 关联 Inbox: `_example/`

## 背景

用户身份认证是所有业务功能的前置条件，需在第一阶段完成。

## 用户故事

- 作为新用户，我希望通过邮箱注册账号，以便使用产品功能
- 作为已注册用户，我希望登录系统，以便访问个人数据
- 作为忘记密码的用户，我希望重置密码，以便恢复账号访问

## 功能范围

### 本期包含
- 邮箱 + 密码注册
- 登录 / 登出
- 密码重置（邮件验证码）
- Session 管理

### 后续规划
- OAuth 第三方登录
- MFA 多因素认证

## 技术约束

- 密码加密: bcrypt
- Session: JWT (Access + Refresh Token)
- 邮件服务: 待定

## 验收标准

见 `.vela/specs/user-auth.md` 对应技术规格。
""",

"tests/README.md": """\
# 质量保障层 (Testing)

## 目录结构

```
tests/
├── e2e/        # 端到端测试
├── unit/       # 单元测试（各模块自带，此处放跨模块）
└── reports/    # 测试报告
```

## 测试规范

- **TDD**: 先写测试，再写实现
- **覆盖率目标**: >80%
- **运行**: `CI=true` 防止 watch 模式阻塞
""",

"docs/release-artifacts/AGENTS.md": """\
# Release Artifacts 管理规范

每次交付时，需在此目录记录发布物，确保变更材料可追溯。

## 目录结构

```
release-artifacts/
├── AGENTS.md
└── {version}/
    ├── ddl/     # 数据库结构变更
    ├── dml/     # 数据初始化脚本
    └── config/  # 配置变更说明
```

## 规范

- SQL 文件须含幂等保护（IF NOT EXISTS 等）
- 破坏性变更（DROP/TRUNCATE）须额外注释风险
""",

}

# ── 主逻辑 ──────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description="Vela 项目骨架初始化")
    p.add_argument("--name-cn",   required=True, help="项目中文名，如：天帆")
    p.add_argument("--name-en",   required=True, help="项目英文代号，如：Vela")
    p.add_argument("--desc",      required=True, help="一句话描述")
    p.add_argument("--dir",       required=True, help="目标目录（绝对路径）")
    p.add_argument("--frontends", default="",    help="前端列表，逗号分隔，如：frontend-desktop,frontend-web")
    p.add_argument("--backend",   default="",    help="后端占位目录名，如：backend（仅用于创建 src/backend 目录）")
    p.add_argument("--git-init",  action="store_true", default=True, help="是否 git init（默认 true）")
    p.add_argument("--no-git",    action="store_true", help="跳过 git init")
    return p.parse_args()


def render(template: str, ctx: dict) -> str:
    result = template
    for k, v in ctx.items():
        result = result.replace("{" + k + "}", v)
    return result


def write_file(path: Path, content: str, dry_run=False):
    if path.exists():
        print(f"  ⚠ 跳过（已存在）: {path}")
        return
    if dry_run:
        print(f"  [dry] 写入: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  ✓ 写入: {path}")


def main():
    args = parse_args()
    root = Path(args.dir).expanduser().resolve()

    frontends = [f.strip() for f in args.frontends.split(",") if f.strip()]
    now = datetime.now()
    year = str(now.year)
    month = f"{now.month:02d}"

    # src_list for AGENTS.md
    src_items = []
    for fe in frontends:
        src_items.append(f"│   ├── {fe}/")
    if args.backend:
        src_items.append("│   └── backend/")
    src_list = "\n".join(src_items) if src_items else "│   └── (待创建)"

    ctx = {
        "name_cn":  args.name_cn,
        "name_en":  args.name_en,
        "desc":     args.desc,
        "year":     year,
        "month":    month,
        "src_list": src_list,
    }

    print(f"\n🚀 Vela 项目初始化: {args.name_cn} ({args.name_en})")
    print(f"   目标目录: {root}\n")

    # ── 1. 创建目录 ──────────────────────────────────────────────
    dirs = [
        ".vela/specs",
        "prd/00_vision",
        "prd/01_inbox",
        "prd/02_prd",
        "prd/archive/inbox",
        "prd/archive/prd",
        "prd/prototype",
        "tests/e2e",
        "tests/reports",
        "sre",
        "changelog",
        "docs/architecture",
        "docs/api",
        "docs/release-artifacts",
    ]
    for fe in frontends:
        dirs.append(f"src/{fe}")
    if args.backend:
        dirs.append("src/backend")

    for d in dirs:
        target = root / d
        target.mkdir(parents=True, exist_ok=True)
        print(f"  📁 {d}/")

    print()

    # ── 2. 写入模板文件 ───────────────────────────────────────────
    for rel_path, template in TEMPLATES.items():
        content = render(template, ctx)
        write_file(root / rel_path, content)

    # prototype 子目录 (仅创建，不写文件)
    for fe in frontends:
        (root / "prd" / "prototype" / fe).mkdir(parents=True, exist_ok=True)

    print()

    # ── 3. Git init ───────────────────────────────────────────────
    do_git = args.git_init and not args.no_git
    if do_git:
        is_git = (root / ".git").exists()
        if is_git:
            print("  ℹ Git 仓库已存在，跳过 git init")
        else:
            subprocess.run(["git", "init"], cwd=root, check=True, capture_output=True)
            subprocess.run(["git", "add", "."], cwd=root, check=True, capture_output=True)
            msg = f"chore: 🚀 vela project init - {args.name_en}"
            subprocess.run(["git", "commit", "-m", msg], cwd=root, check=True, capture_output=True)
            print(f"  ✓ git init & initial commit: {msg}")

    # ── 4. 完成摘要 ───────────────────────────────────────────────
    print(f"""
✅ 初始化完成！

{root}/
├── .vela/               ← Vela 平台配置（AGENTS.md、specs/ 等）
│   └── specs/            ← SDD 技术规格（需求 → 代码的关键桥梁）
├── prd/                 ← 需求大脑
│   ├── 00_vision/
│   ├── 01_inbox/         ← 唯一入口 + 状态看板（含 _example/）
│   ├── 02_prd/           ← 正式 PRD（含 _example/）
│   ├── archive/          ← 完结归档（inbox/ + prd/）
│   └── prototype/
├── src/                 ← 源码实现
{chr(10).join(f"│   ├── {fe}/" for fe in frontends)}{"" if not frontends else ""}
│   └── backend/
├── tests/
├── sre/
├── changelog/
└── docs/

核心工作流: 01_inbox → 02_prd → .vela/specs/ → plan.md → src/

下一步建议：
  1. 填写 prd/00_vision/vision.md（产品愿景）
  2. 参照 prd/01_inbox/_example/ 格式录入需求
  3. 需求评审后生成 PRD 和 `.vela/specs/` 技术规格
""")


if __name__ == "__main__":
    main()
