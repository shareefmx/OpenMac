#!/usr/bin/env python3
"""
OpenMac Easy Project Submission Helper.
Guides contributors through adding a new open-source macOS app or tool,
validates inputs, manages the icon, and automatically regenerates README.md.
"""

import os
import re
import shutil
import sys
import yaml

GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

FALLBACK_SVG_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
  <defs>
    <linearGradient id="appBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A84FF"/>
      <stop offset="100%" stop-color="#5E5CE6"/>
    </linearGradient>
  </defs>
  <rect x="8" y="8" width="112" height="112" rx="26" fill="url(#appBg)" stroke="#38BDF8" stroke-width="3"/>
  <text x="64" y="76" font-family="-apple-system, BlinkMacSystemFont, 'SF Pro Display', sans-serif" font-size="44" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{initial}</text>
</svg>
"""

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

def main():
    print(f"\n{BOLD}{BLUE}======================================================{RESET}")
    print(f"{BOLD}{BLUE}       OpenMac — Add New Project (Easy Wizard)       {RESET}")
    print(f"{BOLD}{BLUE}======================================================{RESET}\n")

    # Load categories
    cat_file = os.path.join("data", "categories.yml")
    proj_file = os.path.join("data", "projects.yml")

    with open(cat_file, "r", encoding="utf-8") as f:
        categories = yaml.safe_load(f).get("categories", [])

    with open(proj_file, "r", encoding="utf-8") as f:
        proj_data = yaml.safe_load(f) or {}
        projects = proj_data.get("projects", [])

    existing_ids = {p["id"] for p in projects}
    existing_urls = {p.get("github", "").rstrip("/").lower() for p in projects}

    # 1. Project Name
    while True:
        name = input(f"{BOLD}1. Project Name (e.g. Zed, Maccy):{RESET} ").strip()
        if not name:
            print(f"{RED}Project name cannot be empty.{RESET}")
            continue
        pid = slugify(name)
        if pid in existing_ids:
            print(f"{YELLOW}Warning: A project with ID '{pid}' already exists.{RESET}")
            override = input("Enter a unique slug identifier: ").strip()
            if override:
                pid = slugify(override)
        break

    # 2. GitHub URL
    while True:
        github = input(f"{BOLD}2. GitHub / Source Code URL:{RESET} ").strip()
        if not (github.startswith("https://github.com/") or github.startswith("https://gitlab.com/") or github.startswith("https://codeberg.org/")):
            print(f"{RED}Please enter a valid public Git URL (e.g. https://github.com/organization/repo){RESET}")
            continue
        if github.rstrip("/").lower() in existing_urls:
            print(f"{RED}This repository is already listed in OpenMac!{RESET}")
            return
        break

    # 3. Official Website
    website = input(f"{BOLD}3. Official Website (press Enter to use GitHub URL):{RESET} ").strip()
    if not website:
        website = github

    # 4. Description
    while True:
        desc = input(f"{BOLD}4. Short Description (20 to 200 characters):{RESET} ").strip()
        if len(desc) < 20:
            print(f"{RED}Description too short ({len(desc)} characters). Minimum 20 characters required.{RESET}")
            continue
        if not desc.endswith("."):
            desc += "."
        break

    # 5. Category Selection
    print(f"\n{BOLD}5. Select Category:{RESET}")
    for idx, c in enumerate(categories, start=1):
        print(f"   [{idx:2d}] {c.get('icon', '📦')} {c['name']}")

    while True:
        try:
            choice = int(input(f"Enter choice (1-{len(categories)}): ").strip())
            if 1 <= choice <= len(categories):
                selected_cat = categories[choice - 1]["id"]
                break
        except ValueError:
            pass
        print(f"{RED}Invalid selection. Choose between 1 and {len(categories)}.{RESET}")

    # 6. License
    print(f"\n{BOLD}6. Open-Source License:{RESET}")
    print("   Common: MIT | Apache-2.0 | GPL-3.0 | GPL-2.0 | AGPL-3.0 | BSD-3-Clause | ISC")
    license_input = input("Enter License [default: MIT]: ").strip() or "MIT"

    # 7. Language
    lang_input = input(f"{BOLD}7. Primary Language / Tech Stack (e.g. Swift, Rust, TypeScript):{RESET} ").strip() or "Swift"

    # 8. Icon Handling
    icon_dest = f"icons/project-icons/{pid}.svg"
    icon_src = input(f"{BOLD}8. Path to icon file (SVG or PNG, or press Enter to auto-generate icon):{RESET} ").strip()

    if icon_src and os.path.isfile(icon_src):
        ext = os.path.splitext(icon_src)[1].lower()
        if ext in (".svg", ".png"):
            icon_dest = f"icons/project-icons/{pid}{ext}"
            shutil.copyfile(icon_src, icon_dest)
            print(f"{GREEN}✓ Copied icon to {icon_dest}{RESET}")
        else:
            print(f"{YELLOW}Unsupported icon format. Auto-generating SVG placeholder instead.{RESET}")
            with open(icon_dest, "w", encoding="utf-8") as f:
                f.write(FALLBACK_SVG_TEMPLATE.format(initial=name[0].upper()))
    else:
        with open(icon_dest, "w", encoding="utf-8") as f:
            f.write(FALLBACK_SVG_TEMPLATE.format(initial=name[0].upper()))
        print(f"{GREEN}✓ Created clean vector icon at {icon_dest}{RESET}")

    # Build entry
    new_entry = {
        "id": pid,
        "name": name,
        "description": desc,
        "github": github,
        "website": website,
        "category": selected_cat,
        "license": license_input,
        "platform": "macOS 12.0+",
        "language": lang_input,
        "status": "active",
        "icon": icon_dest,
        "stars": 0
    }

    # Append to projects
    projects.append(new_entry)
    proj_data["projects"] = projects

    with open(proj_file, "w", encoding="utf-8") as f:
        yaml.dump(proj_data, f, sort_keys=False, allow_unicode=True)

    print(f"\n{GREEN}✓ Appended '{name}' to {proj_file}!{RESET}")

    # Run validation & regeneration
    print("\nRunning automated validation and updating README.md & web search app...")
    os.system("python3 scripts/validate-projects.py")
    os.system("python3 scripts/generate-readme.py")
    os.system("python3 scripts/build_web.py")

    print(f"\n{BOLD}{GREEN}🎉 Project successfully added!{RESET}")
    print(f"To submit your changes to GitHub, run:\n")
    print(f"  {BLUE}git checkout -b add/{pid}{RESET}")
    print(f"  {BLUE}git add data/projects.yml {icon_dest} README.md{RESET}")
    print(f"  {BLUE}git commit -m \"Add {name} to {selected_cat}\"{RESET}")
    print(f"  {BLUE}git push origin add/{pid}{RESET}\n")

if __name__ == "__main__":
    main()

