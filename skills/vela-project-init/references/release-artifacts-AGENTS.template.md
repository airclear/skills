# Release Artifacts 管理规范

本目录存放每个 Track 交付时产生的发布物，确保上线所需的变更材料齐备可追溯。

## 目录结构

```
release-artifacts/
├── AGENTS.md       # 本文件：规范说明
└── {version}/      # 按版本号组织
    ├── ddl/        # 数据库结构变更 (CREATE/ALTER)
    ├── dml/        # 数据初始化脚本 (INSERT/UPDATE)
    └── config/     # 配置变更说明
```

## 录入规范

每个需要数据库或配置变更的 Track 完成后，必须在对应版本目录下创建变更文件：

1. **DDL 文件**: `ddl/{YYYYMMDD}_{描述}.sql`
2. **DML 文件**: `dml/{YYYYMMDD}_{描述}.sql`
3. **配置变更**: `config/{YYYYMMDD}_{描述}.md`

## 重要提醒

- SQL 文件必须包含幂等性保护（`IF NOT EXISTS`、`IF EXISTS` 等）
- 每个 SQL 语句末尾加分号
- 破坏性变更（DROP、TRUNCATE）需额外注释说明风险
