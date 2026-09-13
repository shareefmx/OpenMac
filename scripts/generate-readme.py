#!/usr/bin/env python3
"""
OpenMac README Generator.
Renders canonical data from data/projects.yml and data/categories.yml
into clean, accessible Markdown tables within README.md between
<!-- PROJECTS:START --> and <!-- PROJECTS:END --> tags.
"""

import os
import sys
import yaml
import argparse

README_PATH = "README.md"
START_MARKER = "<!-- PROJECTS:START -->"
END_MARKER = "<!-- PROJECTS:END -->"
FEATURED_START_MARKER = "<!-- FEATURED:START -->"
FEATURED_END_MARKER = "<!-- FEATURED:END -->"
TOC_START_MARKER = "<!-- TOC:START -->"
TOC_END_MARKER = "<!-- TOC:END -->"
STATS_START_MARKER = "<!-- STATS:START -->"
STATS_END_MARKER = "<!-- STATS:END -->"

def load_data():
    with open(os.path.join("data", "categories.yml"), "r", encoding="utf-8") as f:
        categories = yaml.safe_load(f).get("categories", [])

    with open(os.path.join("data", "projects.yml"), "r", encoding="utf-8") as f:
        projects = yaml.safe_load(f).get("projects", [])

    return categories, projects

def generate_stats_badge(categories, projects):
    total_projects = len(projects)
    total_categories = len(categories)
    return (
        f"[![Total Projects](https://img.shields.io/badge/Projects-{total_projects}-blue.svg?style=flat-square)](#all-categories) "
        f"[![Categories](https://img.shields.io/badge/Categories-{total_categories}-indigo.svg?style=flat-square)](#table-of-contents) "
        f"[![100% Open Source](https://img.shields.io/badge/Source-100%25%20Open%20Source-emerald.svg?style=flat-square)](#selection-criteria) "
        f"[![macOS Compatible](https://img.shields.io/badge/Platform-macOS-000000.svg?logo=apple&style=flat-square)](#selection-criteria)"
    )

def generate_toc(categories, projects_by_cat):
    lines = ["| Category | Focus Area | Projects |", "| :--- | :--- | :---: |"]
    for cat in categories:
        cid = cat["id"]
        cname = cat["name"]
        cicon = cat.get("icon", "📦")
        cdesc = cat.get("description", "")
        count = len(projects_by_cat.get(cid, []))
        # Anchor links directly to the explicit anchor ID
        lines.append(f"| {cicon} [**{cname}**](#{cid}) | {cdesc} | [`{count} apps`](#{cid}) |")
    return "\n".join(lines)

def get_stars_badge(gh_url: str) -> str:
    """Generates a real-time live GitHub/GitLab stars badge."""
    gh_clean = gh_url.strip().rstrip("/")
    if "github.com/" in gh_clean:
        parts = gh_clean.split("github.com/")[-1].split("/")
        if len(parts) >= 2:
            owner, repo = parts[0], parts[1]
            return f"[![Stars](https://img.shields.io/github/stars/{owner}/{repo}?style=flat-square&label=%E2%AD%90)](https://github.com/{owner}/{repo}/stargazers)"
    elif "gitlab.com/" in gh_clean:
        parts = gh_clean.split("gitlab.com/")[-1].split("/")
        if len(parts) >= 2:
            owner, repo = parts[0], parts[1]
            return f"[![Stars](https://img.shields.io/gitlab/stars/{owner}/{repo}?style=flat-square&label=%E2%AD%90)](https://gitlab.com/{owner}/{repo})"
    
    return f"[![Source](https://img.shields.io/badge/%E2%AD%90-Source-blue?style=flat-square)]({gh_url})"

def generate_featured_table(featured_projects):
    lines = [
        "| Icon | Project | Description | Stack | Stars | Links | License |",
        "| :---: | :--- | :--- | :---: | :---: | :---: | :---: |"
    ]
    for p in featured_projects:
        icon_path = p.get("icon", "icons/default.svg")
        name = p["name"]
        site = p.get("website") or p["github"]
        gh = p["github"]
        desc = p["description"]
        lang = p.get("language", "Native")
        lic = p.get("license", "OSI")
        stars_badge = get_stars_badge(gh)
        
        name_md = f"**[{name}]({site})**"
        icon_md = f'<a href="{site}"><img src="./{icon_path}" width="32" height="32" alt="{name}"></a>'
        links_md = f"[Source]({gh})"
        if site != gh:
            links_md = f"[Website]({site}) • [Source]({gh})"
        
        lines.append(f"| {icon_md} | {name_md} | {desc} | `{lang}` | {stars_badge} | {links_md} | `{lic}` |")

    return "\n".join(lines)

def generate_projects_markdown(categories, projects_by_cat):
    sections = []

    for cat in categories:
        cid = cat["id"]
        cname = cat["name"]
        cicon = cat.get("icon", "📦")
        cdesc = cat.get("description", "")
        projs = projects_by_cat.get(cid, [])
        projs.sort(key=lambda x: x["name"].lower())

        slug_name = cname.lower().replace(' ', '-').replace('&', '').replace('--', '-')

        section = []
        # Provide multiple explicit HTML anchors to guarantee matching regardless of link style:
        # e.g., #development, #terminal-shell, #terminal
        section.append(f'<a id="{cid}"></a>')
        if slug_name != cid:
            section.append(f'<a id="{slug_name}"></a>')
        if cid == "ios-macos":
            section.append('<a id="ios--macos"></a>')
        if cid == "vpn-proxy":
            section.append('<a id="vpn--proxy"></a>')
        section.append(f"### {cicon} {cname}\n")
        section.append(f"> {cdesc}\n")

        if not projs:
            section.append("*No projects currently listed in this category. Contributions welcome!*\n")
        else:
            table = [
                "| Icon | Project | Description | Stack | Stars | Links | License |",
                "| :---: | :--- | :--- | :---: | :---: | :---: | :---: |"
            ]
            for p in projs:
                icon_path = p.get("icon", "icons/default.svg")
                name = p["name"]
                site = p.get("website") or p["github"]
                gh = p["github"]
                desc = p["description"]
                lang = p.get("language", "Native")
                lic = p.get("license", "OSI")
                stars_badge = get_stars_badge(gh)
                
                name_md = f"**[{name}]({site})**"
                icon_md = f'<a href="{site}"><img src="./{icon_path}" width="32" height="32" alt="{name}"></a>'
                if site != gh:
                    links_md = f"[Website]({site}) • [Source]({gh})"
                else:
                    links_md = f"[Source]({gh})"

                table.append(f"| {icon_md} | {name_md} | {desc} | `{lang}` | {stars_badge} | {links_md} | `{lic}` |")

            section.append("\n".join(table))
            section.append("\n[⬆ Back to Top](#table-of-contents)\n")

        sections.append("\n".join(section))

    return "\n\n".join(sections)

def replace_marker(content, start_marker, end_marker, replacement):
    if start_marker not in content or end_marker not in content:
        raise ValueError(f"Markers {start_marker} and/or {end_marker} not found in {README_PATH}")

    prefix = content.split(start_marker)[0] + start_marker + "\n"
    suffix = "\n" + end_marker + content.split(end_marker)[1]
    return prefix + replacement.strip() + suffix

def generate(check_mode=False):
    if not os.path.exists(README_PATH):
        print(f"Error: {README_PATH} not found.")
        sys.exit(1)

    categories, projects = load_data()

    # Group projects by category
    projects_by_cat = {}
    featured_projects = []
    for p in projects:
        cid = p["category"]
        projects_by_cat.setdefault(cid, []).append(p)
        if p.get("featured"):
            featured_projects.append(p)

    # Top 10 Featured Projects sorted by stars descending
    featured_projects.sort(key=lambda x: x.get("stars", 0), reverse=True)
    featured_projects = featured_projects[:10]

    with open(README_PATH, "r", encoding="utf-8") as f:
        current_content = f.read()

    # Generate sections
    stats_md = generate_stats_badge(categories, projects)
    toc_md = generate_toc(categories, projects_by_cat)
    featured_md = generate_featured_table(featured_projects)
    projects_md = generate_projects_markdown(categories, projects_by_cat)

    new_content = current_content
    if STATS_START_MARKER in new_content:
        new_content = replace_marker(new_content, STATS_START_MARKER, STATS_END_MARKER, stats_md)
    if TOC_START_MARKER in new_content:
        new_content = replace_marker(new_content, TOC_START_MARKER, TOC_END_MARKER, toc_md)
    if FEATURED_START_MARKER in new_content:
        new_content = replace_marker(new_content, FEATURED_START_MARKER, FEATURED_END_MARKER, featured_md)
    new_content = replace_marker(new_content, START_MARKER, END_MARKER, projects_md)

    if check_mode:
        if new_content == current_content:
            print("README.md is up to date with project data.")
            sys.exit(0)
        else:
            print("README.md is out of sync with data/projects.yml! Run 'python3 scripts/generate-readme.py' to update.")
            sys.exit(1)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Successfully generated README.md tables for {len(projects)} projects across {len(categories)} categories.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate OpenMac README from canonical YAML.")
    parser.add_argument("--check", action="store_true", help="Check if README.md is in sync without modifying.")
    args = parser.parse_args()
    generate(check_mode=args.check)
