---
name: vela-inbox
description: |
  天帆 (Vela) 需求入库 - 将需求录入 product/01_inbox/，自动分配编号、创建目录结构、更新索引。
  触发场景：用户说"入库"、"新增需求"、"记录需求"、"需求入库"、"把这个需求录进去"、"登记需求"、"需求登记"，
  或者用户附带了一个需求文件并说"入库"/"录入"/"记录"。
  即使用户只说"入库"或"把刚才说的需求录进去"也应触发此 Skill。
  注意：用户可能在多轮对话中先描述需求，最后才说"入库"，需要回溯对话提取需求内容。
---

# 天帆 Vela - 需求入库

将需求快速录入 `prd/01_inbox/`，自动分配编号、创建目录、生成 `requirement.md`、更新索引。

## 执行流程

### 第一步：定位 prd 目录

在当前工作目录中找 `prd/01_inbox/`。如果找不到，询问用户路径。

### 第二步：快速获取现状（用脚本，不要手动读文件）

```bash
python3 {SKILL_DIR}/scripts/inbox_state.py {PRD_DIR}
```

输出 JSON，包含 `next_id_str`（下一个编号）和 `entries`（现有条目列表）。

`{SKILL_DIR}` 是本 Skill 的安装路径（通常为 `~/.claude/skills/vela-inbox`）。

### 第三步：提取需求内容

需求来源有两种，按优先级处理：

> **附带文件时的特殊判断**：读取文件后，对照 `inbox_state.py` 返回的 `entries` 列表，检查是否有目录名与文件内容高度相关（如已有 `008_customer_pudao_email_integration`，而文件是该客户的接口文档）。若匹配，询问用户：
> - 选项 1：补充到已有条目（复制文件到 `_resources/`，更新 `requirement.md` 引用）
> - 选项 2：作为新需求独立入库
>
> 确认后再继续执行，不要默认创建新编号。

**A. 附带文件**：用户在消息中提供了文件路径或附件，直接读取文件内容作为需求原文。

**B. 对话描述**：回溯当前对话历史，提取用户描述的需求内容。找到最近一段连续的需求描述（通常在"入库"指令之前）。

### 第四步：推断元数据

根据需求内容自动推断，**不要询问用户**（除非完全无法判断）：

| 字段 | 推断方式 |
|------|----------|
| `title` | 一句话概括需求，中文，10字以内 |
| `source_type` | 根据内容判断：`market`（营销/业务）/ `tech`（技术/工程）/ `ops`（运维/部署）/ `customer`（客户/用户反馈）/ `security`（安全）/ `product`（产品规划） |
| `short_desc` | 英文，2-4个单词，横线连接，如 `wechat-notification` |
| `source_team` | 根据来源推断，如"营销团队"、"技术团队"、"客户需求"，不确定则填"待确认" |

### 第五步：运行入库脚本

```bash
python3 {SKILL_DIR}/scripts/create_entry.py \
  "{PRD_DIR}" \
  "{ID_STR}" \
  "{SOURCE_TYPE}" \
  "{SHORT_DESC}" \
  "{TITLE}" \
  "{SOURCE_TEAM}" \
  ["{ORIGINAL_FILE}"]
```

`ORIGINAL_FILE` 仅在用户提供了原始文件时传入。

### 第六步：补全 requirement.md

脚本创建的 `requirement.md` 包含基本信息表格，**还需要你填写需求描述部分**：

打开生成的 `requirement.md`，在 `## 需求描述` 下写入：

1. **需求摘要**：2-3句话概括核心诉求
2. **背景与动机**：为什么提这个需求
3. **核心功能点**：列出主要功能点（bullet list）
4. **原始内容**：如果来自对话，原文引用（blockquote）；如果来自文件，已在 `_resources/` 中，注明路径

格式示例：
```markdown
## 需求描述

### 摘要
用户希望通过企业微信 Webhook 接收告警通知，减少对邮件的依赖。

### 背景
当前告警只支持邮件，部分团队不常看邮件，导致告警响应慢。

### 核心功能点
- 配置企业微信 Webhook URL
- 告警触发时推送消息到企业微信群
- 支持消息模板自定义

### 原始描述
> 用户原文引用...
```

### 第七步：输出确认

告知用户：
- 创建的目录名（如 `010_tech_wechat-notification`）
- 分配的编号
- 下一步建议（如需要精炼为 PRD，可运行 `/prd-development`）
- 需求完结后归档操作提示：
  ```bash
  mv prd/01_inbox/010_xxx/  prd/archive/inbox/
  mv prd/02_prd/P010_xxx/   prd/archive/prd/    # 如已有对应 PRD
  # 并在 prd/01_inbox/index.md 中将状态改为"已归档"
  ```

## 注意事项

- 全程用**中文**与用户交互
- 脚本已处理 index.md 更新，不要手动修改
- 如果脚本执行失败，回退为手动创建目录 + 写文件 + 编辑 index.md
- 编号严格按脚本返回的 `next_id_str` 使用，不要自己猜
