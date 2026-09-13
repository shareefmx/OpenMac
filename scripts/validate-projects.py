#!/usr/bin/env python3
"""
OpenMac Project Validation Suite.
Ensures data integrity, strict open-source licensing, icon existence,
and duplicate prevention across the OpenMac directory.
"""

import os
import re
import sys
import yaml
from urllib.parse import urlparse

# ANSI terminal colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Accepted OSI/FSF open-source licenses
ACCEPTED_LICENSES = {
    "MIT",
    "MIT-0",
    "Apache-2.0",
    "GPL-2.0",
    "GPL-2.0-only",
    "GPL-2.0-or-later",
    "GPL-3.0",
    "GPL-3.0-only",
    "GPL-3.0-or-later",
    "AGPL-3.0",
    "AGPL-3.0-only",
    "AGPL-3.0-or-later",
    "LGPL-2.0",
    "LGPL-2.1",
    "LGPL-2.1-only",
    "LGPL-2.1-or-later",
    "LGPL-3.0",
    "LGPL-3.0-only",
    "LGPL-3.0-or-later",
    "BSD-2-Clause",
    "BSD-3-Clause",
    "BSD-4-Clause",
    "MPL-1.1",
    "MPL-2.0",
    "ISC",
    "EPL-1.0",
    "EPL-2.0",
    "Unlicense",
    "CC0-1.0",
    "CC-BY-4.0",
    "CC-BY-SA-4.0",
    "Vim",
    "Zlib",
    "Artistic-2.0",
    "WTFPL",
    "OpenSSL",
    "PostgreSQL",
    "OFL-1.1",
    "OSI-Approved"
}

ACCEPTED_HOSTS = {
    "github.com",
    "gitlab.com",
    "codeberg.org",
    "bitbucket.org",
    "sourceforge.net",
    "sf.net",
    "mozilla.org",
    "kde.org",
    "googlesource.com",
    "apple.com",
    "blender.org",
    "zx2c4.com",
    "wildfiregames.com"
}

ACCEPTED_STATUSES = {"active", "maintenance", "archived"}

REQUIRED_FIELDS = [
    "id",
    "name",
    "description",
    "github",
    "website",
    "category",
    "license",
    "platform",
    "language",
    "status",
    "icon"
]

def normalize_url(url: str) -> str:
    """Normalizes a URL by stripping trailing slashes and removing .git suffixes."""
    url = url.strip()
    if url.endswith(".git"):
        url = url[:-4]
    return url.rstrip("/").lower()

def validate():
    print(f"{BOLD}{BLUE}=========================================={RESET}")
    print(f"{BOLD}{BLUE}       OpenMac Repository Validator       {RESET}")
    print(f"{BOLD}{BLUE}=========================================={RESET}\n")

    errors = []
    warnings = []

    # 1. Load categories
    categories_path = os.path.join("data", "categories.yml")
    if not os.path.exists(categories_path):
        errors.append(f"Categories file missing: {categories_path}")
        return False, errors, warnings

    try:
        with open(categories_path, "r", encoding="utf-8") as f:
            cat_data = yaml.safe_load(f)
            categories = {c["id"]: c for c in cat_data.get("categories", [])}
    except Exception as e:
        errors.append(f"Failed to parse {categories_path}: {e}")
        return False, errors, warnings

    print(f"Loaded {GREEN}{len(categories)}{RESET} valid categories.")

    # 2. Load projects
    projects_path = os.path.join("data", "projects.yml")
    if not os.path.exists(projects_path):
        errors.append(f"Projects file missing: {projects_path}")
        return False, errors, warnings

    try:
        with open(projects_path, "r", encoding="utf-8") as f:
            proj_data = yaml.safe_load(f)
            projects = proj_data.get("projects", [])
    except Exception as e:
        errors.append(f"Failed to parse {projects_path}: {e}")
        return False, errors, warnings

    print(f"Loaded {GREEN}{len(projects)}{RESET} projects for validation.\n")

    seen_ids = set()
    seen_github_urls = {}
    seen_names = set()

    for idx, p in enumerate(projects, start=1):
        p_name = p.get("name", f"<unnamed project #{idx}>")

        # Check required fields
        for field in REQUIRED_FIELDS:
            if field not in p or p[field] is None or (isinstance(p[field], str) and not p[field].strip()):
                errors.append(f"Project '{p_name}' (entry #{idx}) is missing required field: '{field}'")

        # Validate ID
        pid = p.get("id")
        if pid:
            if not re.match(r"^[a-z0-9-]+$", pid):
                errors.append(f"Project '{p_name}': id '{pid}' must be lowercase alphanumeric and hyphens only.")
            if pid in seen_ids:
                errors.append(f"Duplicate project id: '{pid}' in project '{p_name}'")
            seen_ids.add(pid)

        # Validate name duplication
        if "name" in p:
            name_lower = p["name"].strip().lower()
            if name_lower in seen_names:
                warnings.append(f"Possible duplicate project name detected: '{p['name']}'")
            seen_names.add(name_lower)

        # Validate description
        desc = p.get("description", "")
        if desc:
            if len(desc) < 20:
                errors.append(f"Project '{p_name}': description is too short ({len(desc)} chars). Minimum 20 characters required.")
            if len(desc) > 240:
                warnings.append(f"Project '{p_name}': description is long ({len(desc)} chars). Consider keeping it under 240 chars for table readability.")

        # Validate category
        cat = p.get("category")
        if cat and cat not in categories:
            errors.append(f"Project '{p_name}': category '{cat}' is not defined in data/categories.yml. Valid categories: {list(categories.keys())}")

        # Validate GitHub URL & duplicates
        gh_url = p.get("github")
        if gh_url:
            norm_gh = normalize_url(gh_url)
            parsed = urlparse(gh_url)
            if not parsed.scheme or not parsed.netloc:
                errors.append(f"Project '{p_name}': Invalid GitHub URL '{gh_url}'")
            elif not any(host in parsed.netloc.lower() for host in ACCEPTED_HOSTS):
                errors.append(f"Project '{p_name}': source repository '{gh_url}' must be a hosted public Git repository ({', '.join(sorted(ACCEPTED_HOSTS))}).")
            
            if norm_gh in seen_github_urls:
                errors.append(f"Duplicate GitHub repository URL detected: '{gh_url}' (already used by '{seen_github_urls[norm_gh]}')")
            else:
                seen_github_urls[norm_gh] = p_name

        # Validate Website URL
        website = p.get("website")
        if website:
            parsed_site = urlparse(website)
            if not parsed_site.scheme or not parsed_site.netloc:
                errors.append(f"Project '{p_name}': Invalid website URL '{website}'")

        # Validate License
        lic = p.get("license")
        if lic:
            # Check individual license or dual licenses e.g., "MIT / Apache-2.0"
            parts = [part.strip() for part in re.split(r"[/|]", lic)]
            for part in parts:
                if part not in ACCEPTED_LICENSES:
                    errors.append(f"Project '{p_name}': License '{part}' is not in the list of recognized open-source licenses. "
                                  f"OpenMac strictly accepts genuine open-source projects. If this is a valid OSI license, add it to ACCEPTED_LICENSES.")

        # Validate Status
        status = p.get("status")
        if status and status not in ACCEPTED_STATUSES:
            errors.append(f"Project '{p_name}': Status '{status}' is invalid. Allowed: {list(ACCEPTED_STATUSES)}")

        # Validate Icon
        icon_path = p.get("icon")
        if icon_path:
            if not (icon_path.endswith(".png") or icon_path.endswith(".svg")):
                errors.append(f"Project '{p_name}': Icon '{icon_path}' must have .png or .svg extension.")
            
            # Check file exists on filesystem
            if not os.path.isfile(icon_path):
                errors.append(f"Project '{p_name}': Icon file not found on disk at '{icon_path}'. "
                              f"All project icons must be committed to icons/project-icons/.")

    # Summary
    print(f"Scanned {BOLD}{len(projects)}{RESET} projects.")
    if warnings:
        print(f"\n{YELLOW}Warnings ({len(warnings)}):{RESET}")
        for w in warnings:
            print(f"  {YELLOW}⚠️  {w}{RESET}")

    if errors:
        print(f"\n{RED}Validation Failed with {len(errors)} error(s):{RESET}")
        for err in errors:
            print(f"  {RED}❌ {err}{RESET}")
        return False

    print(f"\n{GREEN}✅ All {len(projects)} projects passed validation successfully!{RESET}\n")
    return True

if __name__ == "__main__":
    success = validate()
    sys.exit(0 if success else 1)

