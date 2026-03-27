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

### 工作流程（4 Phase）

1. **Phase 1: Interactive Target Selection & Confirmation** - 两条路径：Direct Confirmation (Path A) 或 Guided Selection Menu (Path B)；统一层级菜单，最多 4 个选项 + "Other"
2. **Phase 2: Git Reconciliation & Verification** - 映射 Implementation Commits、Ghost Commits、Plan-Update Commits、Track Creation Commit（支持新旧 Track Registry 格式）
3. **Phase 3: Final Execution Plan Confirmation** - 详细执行摘要，Approve/Revise 选择
4. **Phase 4: Execution & Verification** - 按逆序执行 reverts，冲突处理，Plan 状态验证

### 强制性约束

- **Double Confirmation** - 在运行 `git revert` 之前，始终确认目标选择和最终执行计划
- **Reverse Order** - 回滚必须按时间倒序执行
- **Plan Sync** - 最后一步必须验证 `plan.md` 或 `tracks.md` 反映回滚后的状态
- **Tool Call Validation** - 每个工具调用必须验证成功，失败时立即停止并等待指令

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

### 2026-03-27

- **Update to 0.4.1** - 同步 Conductor 0.4.1 的变更：重构为 4 Phase 工作流，改进 Target Selection（Direct/Guided 双路径），增强 Git Reconciliation（Ghost Commits、Plan-Update Commits、Track Creation Commit 新旧格式支持），增加 Execution Plan Approve/Revise 选择，增加 Tool Call Validation 约束。

### 2026-03-02

- **Update to 0.3.1** - 同步 Conductor 0.3.1 的变更，包括对全 Track 撤回时创建 commit 的处理、Ghost commit 处理、及改进的选择菜单。

### 2026-02-24

- **Initial Module Documentation** - 创建模块级 CLAUDE.md
- 扫描覆盖率：100%（3 个文件）
