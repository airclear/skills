[根目录](../../CLAUDE.md) > [skills](../) > **conductor-implement**

---

# conductor-implement

## 模块职责

**执行 Track 计划中定义的任务，是 Conductor 框架的"引擎"。**

当用户想要开始或继续实施功能或 Bug 修复时使用此技能。该技能管理任务生命周期，遵循项目工作流，并在完成后同步项目文档。

---

## 入口与启动

**入口文件:** `SKILL.md`

**元数据:**
```yaml
name: conductor-implement
description: Executes the tasks defined in a Conductor track's plan...
```

---

## 对外接口

本模块通过以下协议文档定义行为：

| 协议 | 文件 |
|------|------|
| Resolution Protocol | `references/resolution-protocol.md` |
| Implementation Protocol | `references/implementation-protocol.md` |
| Synchronization Protocol | `references/synchronization.md` |

---

## 关键依赖与配置

### 工作流程

1. **Track Selection** - 识别活动 Track 或下一个待处理的 Track
2. **Context Loading** - 加载 Track 的规格、计划和工作流
3. **Task Execution** - 按顺序执行计划中的任务，每个任务遵循 TDD 流程
4. **Completion & Sync** - 所有任务完成后，同步项目级文档（`product.md`, `tech-stack.md`）
5. **Cleanup** - 提供归档或删除已完成 Track 工件的选项

### 强制性约束

- **Workflow is Law** - `workflow.md` 是任务实施的唯一事实来源
- **Confirmation for Sync** - 未经用户明确批准，绝不更新 `product.md`, `tech-stack.md` 或 `product-guidelines.md`
- **Success Validation** - 验证每个工具调用，失败时停止

### 任务生命周期

```
[ ] 待处理 → [~] 进行中 → [x] 已完成 [+commit_sha]
```

---

## 数据模型

### Plan.md 任务格式

```markdown
- [ ] Task: 实现用户模型
  - [ ] Write tests for user model
  - [ ] Implement user model
  - [ ] Document user model
```

### 同步协议

实施完成后，需要：
1. 检查 `product.md`, `tech-stack.md` 是否需要更新
2. 向用户展示拟议的 diff
3. 获得批准后更新文件
4. 提交更改

---

## 测试与质量

**测试文件:** 不直接包含可执行测试

**质量保证:**
- 遵循 workflow.md 定义的 TDD 流程
- 每个任务完成后更新 `plan.md` 并附加 commit SHA
- 阶段完成时创建 Checkpoint 提交

### Phase Completion Verification

阶段完成后执行：
1. 确定阶段范围（通过 git diff）
2. 验证并创建测试
3. 执行自动化测试
4. 生成手动验证计划
5. 创建 Checkpoint 提交并附加 Git Note

---

## 常见问题 (FAQ)

**Q: 如何处理任务执行中的失败？**
A: 验证工具调用，失败时立即停止并向用户报告。

**Q: 何时同步项目文档？**
A: 在所有任务完成后，但在提交之前，需要用户明确批准拟议的更改。

**Q: Checkpoint 提交的作用是什么？**
A: 标记阶段完成，附加详细的验证报告，便于审计和回滚。

---

## 相关文件清单

| 文件 | 说明 |
|------|------|
| [`SKILL.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-implement/SKILL.md) | 技能主文件 |
| [`references/resolution-protocol.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-implement/references/resolution-protocol.md) | 文件定位协议 |
| [`references/implementation-protocol.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-implement/references/implementation-protocol.md) | 实施协议 |
| [`references/synchronization.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-implement/references/synchronization.md) | 同步协议 |

---

## 变更记录 (Changelog)

### 2026-02-24

- **Initial Module Documentation** - 创建模块级 CLAUDE.md
- 扫描覆盖率：100%（4 个文件）
