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

    # 4. Assert Navigation Anchors & Core Integrity
    print("\n4. Asserting Navigation Anchors & Repository Integrity...")
    required_anchors = [
        "about", "table-of-contents", "featured-projects", "all-categories",
        "selection-criteria", "icon-system", "faq", "contributors",
        "license", "how-to-contribute"
    ]
    for anchor in required_anchors:
        assert_true(f'id="{anchor}"' in readme or f'#{anchor}' in readme, f"Anchor '{anchor}' missing in README.md")
    print(f"  ✓ Verified all {len(required_anchors)} core navigation anchors present in README.md.")

    # 5. Assert Web Application Assets & Data Integrity
    print("\n5. Asserting Web Application Assets & Sync...")
    required_web_files = ["index.html", "styles.css", "app.js", "site-data.json", "vercel.json"]
    for wf in required_web_files:
        assert_true(os.path.isfile(wf), f"Web asset missing: {wf}")
        assert_true(os.path.getsize(wf) > 100, f"Web asset is empty or too small: {wf}")

    import json
    with open("site-data.json", "r", encoding="utf-8") as f:
        site_data = json.load(f)
    assert_true(len(site_data.get("projects", [])) == 1165, f"Expected 1,165 projects in site-data.json, found {len(site_data.get('projects', []))}")
    assert_true(len(site_data.get("categories", [])) == 50, f"Expected 50 categories in site-data.json, found {len(site_data.get('categories', []))}")
    assert_true(len(site_data.get("featured", [])) == 10, f"Expected 10 featured projects in site-data.json, found {len(site_data.get('featured', []))}")
    print(f"  ✓ Validated index.html, styles.css, app.js, vercel.json, and site-data.json (1,165 apps, 50 categories, 10 featured).")

    print("\n==================================================")
    print("    🎉 ALL 5 TEST SUITES PASSED SUCCESSFULLY!     ")
    print("==================================================")

if __name__ == "__main__":
    main()
