[根目录](../../CLAUDE.md) > [skills](../) > **conductor-revert**

---

# conductor-revert

## 模块职责

**通过分析 git 历史回滚工作单元（Tracks、Phases 或 Tasks），并同步 Conductor 计划。**

当用户想要撤销特定更改并确保项目文档反映回滚状态时使用此技能。

---

## 入口与启动

**入口文件:** `SKILL.md`

**元数据:**
```yaml
name: conductor-revert
description: Reverts logical units of work by analyzing git history and synchronizing the Conductor plans...
```

---

## 对外接口

本模块通过以下协议文档定义行为：

| 协议 | 文件 |
|------|------|
| Resolution Protocol | `references/resolution-protocol.md` |
| Revert Protocol | `references/revert-protocol.md` |

---

## 关键依赖与配置

### 工作流程

1. **Target Identification** - 交互式帮助用户选择要回滚的 Track、Phase 或 Task
2. **Git Analysis** - 将 Conductor 工件映射到具体的 Git commit SHAs（实施和计划更新提交）
3. **Plan Presentation** - 向用户展示将要以什么顺序回滚哪些提交
4. **Safe Execution** - 执行回滚，处理冲突，并手动同步 Conductor 工件以匹配回滚后的代码状态

### 强制性约束

- **Double Confirmation** - 在运行 `git revert` 之前，始终确认目标选择和最终执行计划
- **Reverse Order** - 回滚必须按时间倒序执行
- **Plan Sync** - 最后一步必须验证 `plan.md` 或 `tracks.md` 反映回滚后的状态

---

## 数据模型

### Revert 目标结构

```
Revert Target:
├── Track: <track_id>
│   ├── Phase: <phase_name> [checkpoint: <sha>]
│   │   └── Tasks: [<task_commits>]
│   └── Plan Commits: [<plan_update_commits>]
```

### Git Note 格式

回滚提交应附加 Git Note 说明：
- 回滚原因
- 原始提交 SHA
- 影响的 Track/Phase/Task

---

## 测试与质量

**测试文件:** 不直接包含可执行测试

**质量保证:**
- 遵循 Resolution Protocol 定位 Conductor 工件
- 回滚前双重确认
- 回滚后验证文档同步

---

## 常见问题 (FAQ)

**Q: Revert 和 git revert 有什么区别？**
A: Conductor Revert 不仅回滚代码提交，还同步 `plan.md` 和 `tracks.md` 文档，确保文档与代码状态一致。

**Q: 如何选择一个 Track 进行回滚？**
A: 通过交互式菜单，显示所有 Tracks 及其状态，用户选择目标后解析相关 commits。

**Q: 回滚后文档如何同步？**
A: 手动更新 `plan.md` 或 `tracks.md`，将相应任务或阶段标记为未开始或删除。

---

## 相关文件清单

| 文件 | 说明 |
|------|------|
| [`SKILL.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-revert/SKILL.md) | 技能主文件 |
| [`references/resolution-protocol.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-revert/references/resolution-protocol.md) | 文件定位协议 |
| [`references/revert-protocol.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-revert/references/revert-protocol.md) | 回滚协议 |

---

## 变更记录 (Changelog)

### 2026-03-02

- **Update to 0.3.1** - 同步 Conductor 0.3.1 的变更，包括对全 Track 撤回时创建 commit 的处理、Ghost commit 处理、及改进的选择菜单。

### 2026-02-24

- **Initial Module Documentation** - 创建模块级 CLAUDE.md
- 扫描覆盖率：100%（3 个文件）
