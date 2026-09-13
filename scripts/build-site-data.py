#!/usr/bin/env python3
"""
Compiles OpenMac canonical data into an optimized JSON file for the web application.
Outputs site-data.json containing projects, categories, and featured apps.
"""

import json
import os
import sys
import yaml

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    categories_path = os.path.join(root_dir, "data", "categories.yml")
    projects_path = os.path.join(root_dir, "data", "projects.yml")
    output_path = os.path.join(root_dir, "site-data.json")

    with open(categories_path, "r", encoding="utf-8") as f:
        categories_data = yaml.safe_load(f).get("categories", [])

    with open(projects_path, "r", encoding="utf-8") as f:
        projects_data = yaml.safe_load(f).get("projects", [])

    # Sort projects by stars descending
    projects_data.sort(key=lambda x: (-x.get("stars", 0), x["name"].lower()))

    # Calculate category project counts
    cat_counts = {}
    for p in projects_data:
        cid = p.get("category")
        cat_counts[cid] = cat_counts.get(cid, 0) + 1

    categories_list = []
    for c in categories_data:
        cid = c["id"]
        categories_list.append({
            "id": cid,
            "name": c["name"],
            "icon": c.get("icon", "📦"),
            "description": c.get("description", ""),
            "count": cat_counts.get(cid, 0)
        })

    # Featured top 10 projects
    featured_list = projects_data[:10]

    payload = {
        "stats": {
            "total_projects": len(projects_data),
            "total_categories": len(categories_list),
            "source_type": "100% Free & Open Source"
        },
        "categories": categories_list,
        "featured": featured_list,
        "projects": projects_data
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, separators=(",", ":"), ensure_ascii=False)

    size_kb = os.path.getsize(output_path) / 1024
    print(f"✓ Compiled {len(projects_data)} projects and {len(categories_list)} categories to {output_path} ({size_kb:.1f} KB)")

if __name__ == "__main__":
    main()

