#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速获取 inbox 现状，避免 LLM 解析 markdown 表格。
输出 JSON，供 skill 直接使用。

用法:
  python inbox_state.py <product_dir>
"""
import json
import os
import re
import sys


def get_state(product_dir: str) -> dict:
    inbox_dir = os.path.join(product_dir, "01_inbox")
    if not os.path.isdir(inbox_dir):
        return {"error": f"inbox 目录不存在: {inbox_dir}"}

    entries = []
    max_id = 0

    for name in sorted(os.listdir(inbox_dir)):
        if name.startswith(".") or name == "index.md":
            continue
        m = re.match(r"^(\d{3})_(.+)$", name)
        if not m:
            continue
        num = int(m.group(1))
        max_id = max(max_id, num)
        entries.append({"id": num, "dir": name})

    next_id = max_id + 1

    return {
        "inbox_dir": inbox_dir,
        "next_id": next_id,
        "next_id_str": f"{next_id:03d}",
        "existing_count": len(entries),
        "entries": entries,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "用法: inbox_state.py <product_dir>"}))
        sys.exit(1)
    result = get_state(sys.argv[1])
    print(json.dumps(result, ensure_ascii=False, indent=2))
