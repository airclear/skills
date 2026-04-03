# 产品管理大脑 (Product Management Brain)

本模块作为产品的核心"大脑"，管理从原始想法到正式 PRD 的完整生命周期。

## 目录结构

```
product/
├── 00_vision/              # 全局设定
│   ├── vision.md           # 产品愿景
│   └── roadmap.md          # 演进路线图
│
├── 01_inbox/               # 原始需求池
│   ├── index.md            # 需求索引与状态跟踪
│   └── xxx_topic/          # 按需求组织的目录
│
├── 02_prd/                 # 已精炼的 PRD 文档
│   ├── index.md            # PRD 索引与状态跟踪
│   └── Pxx_topic/          # 正式 PRD 目录
│
├── prototype/              # UI 原型（按前端项目组织）
│
├── definition/             # 产品定义知识库（可选）
│
└── README.md               # 本文件
```

## 需求流转

```
01_inbox (原始需求) → 分析评审 → 02_prd (正式PRD) → 开发执行
```

| 阶段 | 目录 | 状态流转 |
|------|------|----------|
| 需求录入 | `01_inbox/` | 待分析 → 分析中 → 已转化为PRD / 已拒绝 |
| PRD 交付 | `02_prd/` | 草稿 → 评审中 → 已批准 → 开发中 → 已发布 |

## 命名规范

### Inbox 目录
- **格式**: `[三位编号]_[来源类型]_[简短描述]`
- **示例**: `001_market_features`, `002_user_feedback`

### PRD 目录
- **格式**: `P[三位编号]_[特性简称]`
- **示例**: `P001_user_auth`, `P002_data_export`

## AI 协作指引

1. **提交需求**: 在 `01_inbox/` 创建目录，放入需求文档，更新 `index.md`
2. **需求分析**: 读取 `01_inbox/index.md` 定位待分析需求
3. **生成 PRD**: 结合 `00_vision/` 将需求转化为 `02_prd/Pxx/prd.md`
4. **触发开发**: 将 PRD 移交 Conductor 执行

## 相关文档

- [产品愿景](./00_vision/vision.md)
- [迭代路线图](./00_vision/roadmap.md)
- [需求索引](./01_inbox/index.md)
- [PRD 索引](./02_prd/index.md)
