# How the list is built and ranked

## Inclusion (editorial)

A server is listed if it meets the rules in [CONTRIBUTING.md](CONTRIBUTING.md). Inclusion is the only human decision. Order is never hand-tuned.

## Ranking (automatic)

Every server gets a score from 0 to 100:

| Signal | Weight | Source | Notes |
|---|---:|---|---|
| GitHub stars | 85% | GitHub API | `log10(stars + 1)`, divided by the highest value in the list |
| Recent activity | 15% | GitHub API (`pushed_at`) | 1.0 if pushed today, falling to 0 at 90 days |

Adjustments:

- **Bigger projects.** When the MCP server lives inside a larger project (for example a scraping library or browser agent, marked `catalog: true`), the project's stars say little about the server itself, so they count at 25%. These are marked with † in the README.
- **Archived repos** have their score halved and are marked 📦.
- **Closed-source servers** have no repo, so they score zero on both signals. They are still listed, below open-source servers in their category.

Log scaling stops one huge repo from flattening everything else: 10× the stars is worth a fixed step up, not 10× the score.

The weights live in [`scripts/common.py`](scripts/common.py). Any change to them is made in a public PR.

## What we don't do

We don't benchmark servers. Capability tags, hosting options and free tiers come from each server's own README or the vendor's docs and pricing pages. Read a server's docs, and check which tools it exposes, before you connect it to an agent.

## Refresh schedule

A [GitHub Action](.github/workflows/refresh.yml) runs daily. It fetches stars and activity, saves a snapshot to `data/stats/history/`, re-renders the README and commits the result. The snapshots power the weekly star changes shown next to each server.

## Disclosure

The list is curated by [The Web Scraping Insider](https://www.reddit.com/r/WebScrapingInsider/) and supported by [ScrapeOps](https://scrapeops.io/?utm_source=awesome-web-scraping-mcp-servers&utm_medium=github). The ScrapeOps MCP server is listed under exactly the same inclusion and ranking rules as every other vendor.
