"""Refresh GitHub stars for every listed repo.

Writes data/stats/latest.json and a dated copy in data/stats/history/.
Any value that can't be fetched keeps its previous value, so a flaky run
never wipes data. Set GITHUB_TOKEN to avoid the 60-requests/hour limit.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import date

import requests

from common import STATS, load_stats, load_yaml

UA = "awesome-web-scraping-mcp-stats/1.0 (+https://github.com/The-Web-Scraping-Insider/awesome-web-scraping-mcp-servers)"


def gh_repo(session: requests.Session, repo: str) -> dict | None:
    r = session.get(f"https://api.github.com/repos/{repo}", timeout=20)
    if r.status_code != 200:
        print(f"  ! {repo}: GitHub {r.status_code}", file=sys.stderr)
        return None
    j = r.json()
    return {
        "stars": j.get("stargazers_count"),
        "pushed_at": j.get("pushed_at"),
        "archived": j.get("archived", False),
        "license": (j.get("license") or {}).get("spdx_id"),
    }


def main() -> None:
    skills = load_yaml("servers.yaml")
    prev = load_stats()
    repos = dict(prev.get("repos", {}))

    gh = requests.Session()
    gh.headers.update({"Accept": "application/vnd.github+json", "User-Agent": UA})
    if os.environ.get("GITHUB_TOKEN"):
        gh.headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"

    for repo in sorted({s["repo"] for s in skills if s.get("repo")}):
        info = gh_repo(gh, repo)
        if info:
            repos[repo] = {**repos.get(repo, {}), **{k: v for k, v in info.items() if v is not None}}
            print(f"  {repo}: ⭐ {info['stars']}")


    today = date.today().isoformat()
    out = {"updated": today, "repos": repos}
    STATS.mkdir(parents=True, exist_ok=True)
    (STATS / "history").mkdir(exist_ok=True)
    payload = json.dumps(out, indent=2, sort_keys=True) + "\n"
    (STATS / "latest.json").write_text(payload, encoding="utf-8")
    (STATS / "history" / f"{today}.json").write_text(payload, encoding="utf-8")
    print(f"Saved stats for {len(repos)} repos.")


if __name__ == "__main__":
    main()
