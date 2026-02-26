[根目录](../../CLAUDE.md) > [skills](../) > **conductor-review**

---

# conductor-review

## 模块职责

**充当首席软件工程师，根据项目标准、技术栈选择和实施计划审查已完成或进行中的工作。**

当用户想要进行质量检查或最终确定 Track 时使用此技能。

---

## 入口与启动

**入口文件:** `SKILL.md`

**元数据:**
```yaml
name: conductor-review
description: Acts as a Principal Software Engineer to review completed or in-progress work...
```

---

## 对外接口

本模块通过以下协议文档定义行为：

| 协议 | 文件 |
|------|------|
| Resolution Protocol | `references/resolution-protocol.md` |
| Review Protocol | `references/review-protocol.md` |

---

## 关键依赖与配置

### 工作流程

1. **Scope Selection** - 识别要审查的 Track 或更改
2. **Context Loading** - 检索指南、风格指南和 Track 计划
3. **Meticulous Analysis** - 深入分析 diff，检查意图、风格、安全性和安全性
4. **Automated Testing** - 运行项目测试套件并报告结果
5. **Reporting** - 生成结构化的审查报告，包含严重性分级的发现
6. **Resolution** - 提供自动应用修复和更新实施计划的选项

### 强制性约束

- **Style is Law** - 违反 `conductor/code_styleguides/*.md` 的问题为 HIGH 严重性
- **Automated Verification** - 始终尝试运行现有测试以验证正确性
- **Plan Integrity** - 如果应用修复，`plan.md` 必须更新以记录审查相关的任务和提交

---

## 数据模型

### Review Report 结构

```markdown
# Review Report

## Track: <track_id>

### Severity Summary
- CRITICAL: X
- HIGH: Y
- MEDIUM: Z
- LOW: W

### Findings

#### [CRITICAL] Security Issue
- **Location:** `path/to/file.py:42`
- **Description:** SQL injection vulnerability
- **Recommendation:** Use parameterized queries

#### [HIGH] Style Violation
- **Location:** `path/to/file.ts:15`
- **Description:** Missing type annotations
- **Recommendation:** Add TypeScript types
```

---

## 测试与质量

**测试文件:** 不直接包含可执行测试

**质量保证:**
- 遵循 Resolution Protocol 定位 Conductor 工件
- 始终运行自动化测试
- 审查报告必须包含严重性分级

### 审查清单

- [ ] 功能符合规格
- [ ] 代码遵循风格指南
- [ ] 测试全面
- [ ] 无安全漏洞
- [ ] 性能可接受
- [ ] 文档完整

---

## 常见问题 (FAQ)

**Q: 何时使用此技能？**
A: 当用户说"审查我的代码"、"这个 Track 准备好了吗？"或"运行代码审查"时，在归档或删除已完成的 Track 之前使用。

**Q: 审查报告如何分级？**
A: 按严重性：CRITICAL（安全/数据丢失）、HIGH（风格违反/主要 bug）、MEDIUM（代码质量）、LOW（建议）。

**Q: 如何应用修复？**
A: 审查后提供自动修复选项，应用修复后更新 `plan.md` 记录审查任务和提交。

---

## 相关文件清单

| 文件 | 说明 |
|------|------|
| [`SKILL.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-review/SKILL.md) | 技能主文件 |
| [`references/resolution-protocol.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-review/references/resolution-protocol.md) | 文件定位协议 |
| [`references/review-protocol.md`](/Users/airclear/works/projects/sefworks/skills/skills/conductor-review/references/review-protocol.md) | 审查协议 |

---

## 变更记录 (Changelog)

### 2026-02-24

- **Initial Module Documentation** - 创建模块级 CLAUDE.md
- 扫描覆盖率：100%（3 个文件）
