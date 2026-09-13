#!/usr/bin/env python3
"""
OpenMac Link & URL Health Checker.
Validates the structural integrity and network availability of repository links.
"""

import os
import sys
import yaml
import urllib.request
import urllib.error
from urllib.parse import urlparse
import argparse

TIMEOUT_SECONDS = 6

def validate_link_syntax(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme in ("http", "https"), result.netloc])
    except Exception:
        return False

def check_link_live(url: str) -> tuple[bool, str]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OpenMac-Validator"
    }
    req = urllib.request.Request(url, headers=headers, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            return True, str(resp.status)
    except urllib.error.HTTPError as e:
        # Some servers disallow HEAD requests (403/405), fallback to GET with range
        if e.code in (403, 405):
            try:
                get_req = urllib.request.Request(url, headers=headers, method="GET")
                with urllib.request.urlopen(get_req, timeout=TIMEOUT_SECONDS) as resp:
                    return True, str(resp.status)
            except Exception as e2:
                return False, str(e2)
        return False, str(e)
    except Exception as e:
        return False, str(e)

def main():
    parser = argparse.ArgumentParser(description="Validate URLs in data/projects.yml")
    parser.add_argument("--network", action="store_true", help="Perform live HTTP network checks (slower)")
    args = parser.parse_args()

    projects_path = os.path.join("data", "projects.yml")
    if not os.path.exists(projects_path):
        print(f"Error: {projects_path} not found.")
        sys.exit(1)

    with open(projects_path, "r", encoding="utf-8") as f:
        projects = yaml.safe_load(f).get("projects", [])

    print(f"Checking {len(projects)} projects for link integrity (network={args.network})...\n")

    syntax_errors = []
    live_errors = []

    for p in projects:
        name = p.get("name")
        gh = p.get("github")
        site = p.get("website")

        for url_type, url in [("GitHub", gh), ("Website", site)]:
            if not url:
                continue
            if not validate_link_syntax(url):
                syntax_errors.append(f"Project '{name}': Invalid {url_type} URL format: '{url}'")
            elif args.network:
                ok, msg = check_link_live(url)
                if not ok:
                    live_errors.append(f"Project '{name}': {url_type} unreachable ({msg}): '{url}'")

    if syntax_errors:
        print("❌ URL Syntax Errors found:")
        for err in syntax_errors:
            print(f"  - {err}")
        sys.exit(1)

    if live_errors:
        print("⚠️  Network Warnings found:")
        for err in live_errors:
            print(f"  - {err}")
        # Network warnings do not necessarily fail CI to avoid flakiness from rate limits
        print("\nNote: Some sites block automated requests or require browser verification.")

    print("✅ All project URLs passed syntax validation!")

if __name__ == "__main__":
    main()

