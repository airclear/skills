#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
创建 inbox 条目：目录 + requirement.md + 更新 index.md

用法:
  python create_entry.py <product_dir> <id_str> <source_type> <short_desc> <title> <source_team> [<original_file>]

参数:
  product_dir   - product/ 目录的绝对路径
  id_str        - 三位编号，如 010
  source_type   - 来源类型标签，如 market / tech / ops / customer / security
  short_desc    - 目录名后缀，英文短横线分隔，如 wechat-notification
  title         - 需求标题（中文）
  source_team   - 来源团队（中文）
  original_file - 原始文件路径（可选），会被复制到 _resources/
"""
import json
import os
import re
import shutil
import sys
from datetime import datetime


def update_index(index_path: str, id_str: str, dir_name: str, title: str, source_team: str):
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_row = f"| {id_str} | `{dir_name}` | {title} | {source_team} | 待分析 | - |"

    # 在表格最后一行后插入
    lines = content.splitlines()
    last_table_line = -1
    in_table = False
    for i, line in enumerate(lines):
        if re.match(r"^\|.*\|$", line.strip()):
            in_table = True
            last_table_line = i
        elif in_table and not re.match(r"^\|.*\|$", line.strip()):
            break

    if last_table_line >= 0:
        lines.insert(last_table_line + 1, new_row)
        content = "\n".join(lines) + "\n"
    else:
        content += f"\n{new_row}\n"

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)


def create_entry(product_dir, id_str, source_type, short_desc, title, source_team, original_file=None):
    inbox_dir = os.path.join(product_dir, "01_inbox")
    dir_name = f"{id_str}_{source_type}_{short_desc}"
    entry_dir = os.path.join(inbox_dir, dir_name)

    os.makedirs(entry_dir, exist_ok=True)

    # 处理原始文件
    original_ref = ""
    if original_file and os.path.isfile(original_file):
        resources_dir = os.path.join(entry_dir, "_resources")
        os.makedirs(resources_dir, exist_ok=True)
        dest = os.path.join(resources_dir, os.path.basename(original_file))
        shutil.copy2(original_file, dest)
        rel_path = os.path.relpath(dest, entry_dir)
        original_ref = f"\n## 原始文件\n\n- [{os.path.basename(original_file)}]({rel_path})\n"

    # 写 requirement.md
    req_path = os.path.join(entry_dir, "requirement.md")
    date_str = datetime.now().strftime("%Y-%m-%d")
    content = f"""# {title}

## 基本信息

| 字段 | 内容 |
|------|------|
| 编号 | {id_str} |
| 来源 | {source_team} |
| 录入日期 | {date_str} |
| 状态 | 待分析 |
{original_ref}
## 需求描述

<!-- 需求内容已从对话/文件中提取，见下方 -->

"""
    with open(req_path, "w", encoding="utf-8") as f:
        f.write(content)

    # 更新 index.md
    index_path = os.path.join(inbox_dir, "index.md")
    if os.path.isfile(index_path):
        update_index(index_path, id_str, dir_name, title, source_team)

    return {
        "ok": True,
        "dir": entry_dir,
        "dir_name": dir_name,
        "req_path": req_path,
    }


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 6:
        print(json.dumps({"error": "参数不足"}))
        sys.exit(1)

    product_dir, id_str, source_type, short_desc, title, source_team = args[:6]
    original_file = args[6] if len(args) > 6 else None

    result = create_entry(product_dir, id_str, source_type, short_desc, title, source_team, original_file)
    print(json.dumps(result, ensure_ascii=False, indent=2))
