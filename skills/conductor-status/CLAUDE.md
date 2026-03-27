[根目录](../../CLAUDE.md) > [skills](../) > **conductor-status**

---

# conductor-status

## 模块职责

**提供 Conductor 项目的综合状态概览。**

当用户想知道当前进度、活动任务、下一步或项目 Tracks 和计划的整体健康状况时使用此技能。

---

## 入口与启动

**入口文件:** `SKILL.md`

**元数据:**
```yaml
name: conductor-status
description: Provides a comprehensive status overview of the Conductor project...
```

---

## 对外接口

本模块通过以下协议文档定义行为：

| 协议 | 文件 |
|------|------|
| Resolution Protocol | `references/resolution-protocol.md` |
| Status Protocol | `references/status-protocol.md` |

---

## 关键依赖与配置

### 工作流程

1. **Setup Check (Section 1.1)** - 使用 Universal File Resolution Protocol 验证 Tracks Registry, Product Definition, Tech Stack, Workflow。如果任何文件缺失则停止
2. **Read Project Plan (Section 2.1)** - 读取 Tracks Registry 和每个 track 的 Implementation Plan。支持 `- [ ] **Track:` (新) 和 `## [ ] Track:` (legacy) 两种格式
3. **Parse and Summarize (Section 2.2)** - 解析内容，识别状态（COMPLETED, IN PROGRESS, PENDING）。统计总阶段数和任务数
4. **Present Status Overview (Section 2.3)** - 生成结构化报告，包含 Current Date/Time, Project Status, Current Phase and Task, Next Action Needed, Blockers, Phases (total), Tasks (total), Progress

### 强制性约束

- **Accurate Metrics** - 百分比必须基于 `plan.md` 文件中的实际任务计数
- **Legacy Support** - 正确解析新格式 (`- [ ] **Track:`) 和旧格式 (`## [ ] Track:`) 的 Tracks Registry
- **Clear Identification** - 明确说明哪个 Track、阶段和任务当前"进行中"

---

## 数据模型

### 状态报告结构

```markdown
# Project Status Report

## Metrics
- Total Tracks: X
- Completed: Y%
- In Progress: Z

## Active Work
- Track: <track_id>
- Phase: <phase_name>
- Current Task: <task_name>

## Next Steps
1. <next_task_1>
2. <next_task_2>
```

### Tracks Registry 格式

```markdown
# Tracks Registry

| ID | Title | Status | Created |
|----|-------|--------|---------|
| feat-001 | User Auth | in_progress | 2026-02-20 |
| fix-001 | Login Bug | completed | 2026-02-18 |
```

---

## 测试与质量

**测试文件:** 不直接包含可执行测试

**质量保证:**
- 遵循 Resolution Protocol 定位 Conductor 工件
- 指标计算必须准确
- 状态报告必须清晰标识活动工作

---

## 常见问题 (FAQ)

**Q: 如何确定当前活动任务？**
A: 通过解析 `plan.md` 文件，查找状态为 `[~]` 的任务。

**Q: 完成百分比如何计算？**
A: 基于已完成任务数（`[x]`）除以总任务数。

**Q: 如何处理多个活动 Tracks？**
A: 按创建时间排序，优先显示最近活动的 Track。

---

## 相关文件清单

| 文件 | 说明 |
|------|------|
| [`SKILL.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-status/SKILL.md) | 技能主文件 |
| [`references/resolution-protocol.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-status/references/resolution-protocol.md) | 文件定位协议 |
| [`references/status-protocol.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-status/references/status-protocol.md) | 状态报告协议 |

---

## 变更记录 (Changelog)

### 2026-03-27

- **Update to 0.4.1** - 同步 Conductor 0.4.1 的变更：
  - Setup Check 使用 Universal File Resolution Protocol 验证四个核心文件，缺失时立即停止
  - Status Overview Protocol 细化为 2.1 Read Project Plan / 2.2 Parse and Summarize / 2.3 Present Status Overview 三个子步骤
  - 报告格式增加 Phases (total)、Tasks (total)、Progress (tasks_completed/tasks_total, percentage) 字段
  - status-protocol.md 完全重写以对齐 status.toml 0.4.1

### 2026-03-02

- **Update to 0.3.1** - 同步 Conductor 0.3.1 的变更，包括对 Legacy Track Registry 格式的支持。

### 2026-02-24

- **Initial Module Documentation** - 创建模块级 CLAUDE.md
- 扫描覆盖率：100%（3 个文件）
