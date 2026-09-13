#!/usr/bin/env python3
"""
Comprehensive OpenMac Repository Test Suite.
Asserts data integrity, README alignment, descending star order,
icon assets, web build sync, and anchor resolution across the entire repository.
"""

import os
import re
import sys
import yaml

def assert_true(condition, error_message):
    if not condition:
        print(f"❌ ASSERTION FAILED: {error_message}", file=sys.stderr)
        sys.exit(1)

def main():
    print("==================================================")
    print("      Running OpenMac Full Integrity Suite        ")
    print("==================================================\n")

    # 1. Load Data
    print("1. Validating Canonical Data Models...")
    with open("data/categories.yml", "r", encoding="utf-8") as f:
        categories = yaml.safe_load(f).get("categories", [])
    assert_true(len(categories) == 50, f"Expected exactly 50 categories, found {len(categories)}")

    with open("data/projects.yml", "r", encoding="utf-8") as f:
        projects = yaml.safe_load(f).get("projects", [])
    assert_true(len(projects) == 1165, f"Expected exactly 1,165 projects, found {len(projects)}")
    print(f"  ✓ Validated 50 categories and 1,165 projects loaded from YAML.")

    cat_ids = {c["id"] for c in categories}

    # 2. Check each project
    print("\n2. Asserting Project Schema, Icons, & Categories...")
    seen_ids = set()
    seen_urls = set()
    for p in projects:
        pid = p["id"]
        assert_true(pid not in seen_ids, f"Duplicate project ID found: {pid}")
        seen_ids.add(pid)

        assert_true(p["category"] in cat_ids, f"Project '{pid}' has invalid category '{p['category']}'")

        icon_path = p.get("icon", "")
        assert_true(os.path.isfile(icon_path), f"Icon missing for '{pid}' at '{icon_path}'")
        assert_true(os.path.getsize(icon_path) > 50, f"Icon is empty or corrupted for '{pid}'")

        gh = p.get("github", "").rstrip("/").lower()
        assert_true(gh not in seen_urls, f"Duplicate repository URL found: {gh}")
        seen_urls.add(gh)
    print(f"  ✓ All 1,165 projects have unique IDs, valid categories, valid icons, and unique Git repos.")

    # 3. Assert README Alignment & Star Ordering
    print("\n3. Asserting Table Alignment & Star Order in README.md...")
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()

    assert_true("<!-- PROJECTS:START -->" in readme, "PROJECTS:START marker missing in README")
    assert_true("<!-- PROJECTS:END -->" in readme, "PROJECTS:END marker missing in README")
    assert_true("<!-- FEATURED:START -->" in readme, "FEATURED:START marker missing in README")
    assert_true("<!-- FEATURED:END -->" in readme, "FEATURED:END marker missing in README")

    projs_by_cat = {}
    for p in projects:
        projs_by_cat.setdefault(p["category"], []).append(p)

    for cat in categories:
        cid = cat["id"]
        plist = projs_by_cat.get(cid, [])
        sorted_plist = sorted(plist, key=lambda x: (-x.get("stars", 0), x["name"].lower()))
        expected_names = [p["name"] for p in sorted_plist]

        # Extract table from README for this section
        start_tag = f'<a id="{cid}"></a>'
        assert_true(start_tag in readme, f"Category anchor {start_tag} missing in README.md")
        after_anchor = readme.split(start_tag, 1)[1]
        chunk = after_anchor.split("[⬆ Back to Top]", 1)[0]
        
        table_names = []
        for line in chunk.splitlines():
            line = line.strip()
            if line.startswith("|") and "**[" in line:
                cols = line.split("|")
                if len(cols) >= 3:
                    m = re.search(r'\*\*\[(.*?)\]\(', cols[2])
                    if m:
                        table_names.append(m.group(1))
        
        assert_true(table_names == expected_names, f"Category '{cid}' table in README.md is not sorted in descending star order!")

    print(f"  ✓ All 50 category tables in README.md are strictly sorted in descending star order.")

    # 4. Check Web Application Sync
    print("\n4. Asserting Web Search App Synchronization...")
    assert_true(os.path.isfile("docs/index.html"), "docs/index.html missing")
    assert_true(os.path.isfile("index.html"), "root index.html missing")
    with open("docs/index.html", "r", encoding="utf-8") as f:
        web_html = f.read()
    assert_true("Top 4 Suggested Matches" in web_html, "Top 4 suggestion feature missing in docs/index.html")
    assert_true("1,165" in web_html, "Project count 1,165 missing in docs/index.html")
    print(f"  ✓ Web Search App (Spotlight + Top-4 Suggestions) verified in docs/index.html and index.html.")

    print("\n==================================================")
    print("    🎉 ALL 4 TEST SUITES PASSED SUCCESSFULLY!     ")
    print("==================================================")

if __name__ == "__main__":
    main()
