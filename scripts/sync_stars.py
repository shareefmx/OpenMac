#!/usr/bin/env python3
"""
Syncs real-time star counts for all projects in data/projects.yml using
the GitHub GraphQL API in parallel/batched queries, and updates data/projects.yml.
"""

import os
import re
import sys
import json
import subprocess
import urllib.request
import urllib.parse
import yaml

PROJECTS_FILE = "data/projects.yml"
BATCH_SIZE = 40

def parse_gh_repo(url: str):
    m = re.search(r"github\.com/([^/]+)/([^/#?]+)", url)
    if m:
        owner = m.group(1)
        repo = m.group(2)
        if repo.endswith(".git"):
            repo = repo[:-4]
        return owner, repo
    return None

def fetch_stars_batch(batch):
    """
    batch is a list of tuples: (project_id, owner, repo)
    Returns a dict of project_id -> star_count
    """
    fields = []
    for idx, (_, owner, repo) in enumerate(batch):
        # Sanitize GraphQL field names
        fields.append(f'  r{idx}: repository(owner: "{owner}", name: "{repo}") {{ stargazerCount }}')
    
    query = "query {\n" + "\n".join(fields) + "\n}"
    
    try:
        res = subprocess.run(
            ["gh", "api", "graphql", "-f", f"query={query}"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if not res.stdout.strip():
            return {}
        
        data = json.loads(res.stdout)
        data_dict = data.get("data") or {}
        
        results = {}
        for idx, (pid, _, _) in enumerate(batch):
            repo_data = data_dict.get(f"r{idx}")
            if repo_data and "stargazerCount" in repo_data:
                results[pid] = repo_data["stargazerCount"]
            else:
                results[pid] = 0
        return results
    except Exception as e:
        print(f"Error in batch query: {e}", file=sys.stderr)
        return {}

def fetch_gitlab_stars(url: str) -> int:
    m = re.search(r"gitlab\.com/([^/]+(?:/[^/#?]+)*)", url)
    if m:
        path = m.group(1).rstrip("/").replace("/-/tree/master", "")
        encoded = urllib.parse.quote(path, safe="")
        try:
            api_url = f"https://gitlab.com/api/v4/projects/{encoded}"
            req = urllib.request.Request(api_url, headers={"User-Agent": "OpenMac"})
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data.get("star_count", 0)
        except Exception:
            pass
    return 0

def main():
    if not os.path.exists(PROJECTS_FILE):
        print(f"Error: {PROJECTS_FILE} not found.")
        sys.exit(1)

    with open(PROJECTS_FILE, "r", encoding="utf-8") as f:
        catalog = yaml.safe_load(f)
        projects = catalog.get("projects", [])

    print(f"Loaded {len(projects)} projects from {PROJECTS_FILE}.")

    # Collect GitHub repos
    gh_batches = []
    current_batch = []
    pid_to_index = {}

    for idx, p in enumerate(projects):
        pid = p["id"]
        pid_to_index[pid] = idx
        gh_url = p.get("github", "")
        parsed = parse_gh_repo(gh_url)
        if parsed:
            owner, repo = parsed
            current_batch.append((pid, owner, repo))
            if len(current_batch) >= BATCH_SIZE:
                gh_batches.append(current_batch)
                current_batch = []
        elif "gitlab.com" in gh_url:
            stars = fetch_gitlab_stars(gh_url)
            p["stars"] = stars
            print(f"GitLab repo {pid}: {stars} stars")
        else:
            # Non-GitHub/GitLab
            if "stars" not in p:
                p["stars"] = 0

    if current_batch:
        gh_batches.append(current_batch)

    print(f"Querying GitHub GraphQL API for {len(projects)} projects across {len(gh_batches)} batches...")
    
    total_fetched = 0
    for b_idx, batch in enumerate(gh_batches):
        print(f"Processing batch {b_idx + 1}/{len(gh_batches)} ({len(batch)} repos)...")
        results = fetch_stars_batch(batch)
        for pid, stars in results.items():
            p_idx = pid_to_index[pid]
            projects[p_idx]["stars"] = stars
            total_fetched += 1

    print(f"Successfully fetched stars for {total_fetched} GitHub repositories.")

    # Sort all projects descending by stars to identify global top 10
    sorted_all = sorted(projects, key=lambda x: x.get("stars", 0), reverse=True)
    top_10_ids = {p["id"] for p in sorted_all[:10]}
    
    print("\nTop 10 Starred Projects in OpenMac:")
    for rank, p in enumerate(sorted_all[:10], start=1):
        print(f"  {rank}. {p['name']} ({p['id']}) - {p.get('stars', 0):,} stars")

    # Update featured flags
    for p in projects:
        if p["id"] in top_10_ids:
            p["featured"] = True
        elif "featured" in p:
            del p["featured"]

    # Write back to projects.yml
    catalog["projects"] = projects
    with open(PROJECTS_FILE, "w", encoding="utf-8") as f:
        yaml.dump(catalog, f, sort_keys=False, allow_unicode=True, width=1000)

    print(f"\nSaved updated star counts to {PROJECTS_FILE}.")

if __name__ == "__main__":
    main()
