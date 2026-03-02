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

1. **Setup Check** - 确保所有核心 Conductor 上下文文件存在
2. **Registry Parsing** - 读取 `tracks.md` 文件查找所有活动 Tracks
3. **Plan Analysis** - 遍历每个 Track 的 `plan.md` 计算完成百分比并识别活动任务
4. **Summary Generation** - 将数据综合成可读报告，包括指标、活动工作和下一步

### 强制性约束

- **Accurate Metrics** - 百分比必须基于 `plan.md` 文件中的实际任务计数
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

### 2026-03-02

- **Update to 0.3.1** - 同步 Conductor 0.3.1 的变更，包括对 Legacy Track Registry 格式的支持。

### 2026-02-24

- **Initial Module Documentation** - 创建模块级 CLAUDE.md
- 扫描覆盖率：100%（3 个文件）
