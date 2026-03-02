[根目录](../../CLAUDE.md) > [skills](../) > **conductor-newtrack**

---

# conductor-newtrack

## 模块职责

**启动新的工作单元 (Track)，用于交互式规格构建和实施计划生成。**

当用户想要开始新功能、修复 Bug 或执行维护任务时使用此技能。该技能引导用户完成交互式规格说明构建和详细的实施规划。

---

## 入口与启动

**入口文件:** `SKILL.md`

**元数据:**
```yaml
name: conductor-newtrack
description: Initiates a new unit of work (Track) in a Conductor-managed project...
```

---

## 对外接口

本模块通过以下协议文档定义行为：

| 协议 | 文件 |
|------|------|
| Resolution Protocol | `references/resolution-protocol.md` |
| Track Planning Protocol | `references/track-planning.md` |

---

## 关键依赖与配置

### 工作流程

1. **Context Check** - 验证 Conductor 已设置并加载项目上下文
2. **Interactive Spec** - 提出针对性问题定义成功标准
3. **Plan Generation** - 基于规格和项目 `workflow.md` 创建分阶段任务列表
4. **Artifact Scaffolding** - 创建 Track 目录并初始化 index, metadata, spec, plan 文件
5. **Registry Registration** - 将 Track 添加到项目的 `tracks.md`

### 强制性约束

- **One Question at a Time** - 在交互式阶段必须逐个提问
- **Workflow Alignment** - 计划必须包含 TDD 任务（Write Tests -> Implement）
- **Unique IDs** - 确保 Track ID 在项目内唯一

---

## 数据模型

### Track 结构

```
conductor/tracks/<track_id>/
├── index.md           # Track 索引
├── metadata.json      # 元数据
├── spec.md            # 规格说明
└── plan.md            # 实施计划
```

### metadata.json 示例

```json
{
  "track_id": "feature-xxx",
  "created_at": "2026-02-24",
  "status": "pending"
}
```

---

## 测试与质量

**测试文件:** 不直接包含可执行测试

**质量保证:**
- 遵循 Resolution Protocol 验证 Conductor 工件
- 计划必须与项目 `workflow.md` 对齐
- Track ID 唯一性验证

---

## 常见问题 (FAQ)

**Q: 何时使用此技能？**
A: 当用户说"开始新功能"、"修复 Bug"或"我有新任务"时，在任何实施代码编写之前使用。

**Q: Track 计划包含哪些内容？**
A: 分阶段的任务列表，每个任务包含 TDD 步骤（Red/Green/Refactor），以及验收标准。

**Q: 如何确保 Track 的独特性？**
A: 通过检查 `tracks.md` 中已注册的 Track ID，确保新 ID 不重复。

---

## 相关文件清单

| 文件 | 说明 |
|------|------|
| [`SKILL.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-newtrack/SKILL.md) | 技能主文件 |
| [`references/resolution-protocol.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-newtrack/references/resolution-protocol.md) | 文件定位协议 |
| [`references/track-planning.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-newtrack/references/track-planning.md) | Track 规划协议 |

---

## 变更记录 (Changelog)

### 2026-03-02

- **Update to 0.3.1** - 同步 Conductor 0.3.1 的变更，包括问题分批（batching）和阶段完成 meta-tasks。

### 2026-02-24

- **Initial Module Documentation** - 创建模块级 CLAUDE.md
- 扫描覆盖率：100%（3 个文件）
