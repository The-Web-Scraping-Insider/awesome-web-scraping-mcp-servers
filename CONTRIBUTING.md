# Contributing

Thanks for helping keep this list useful. There are two ways to add a server.

## 1. Use the form (easiest)

[Open a "Submit an MCP server" issue](https://github.com/The-Web-Scraping-Insider/awesome-web-scraping-mcp-servers/issues/new?template=submit-server.yml). A maintainer adds it to the data file.

## 2. Open a pull request

The README is **generated**, so never edit it directly. Instead:

1. Add an entry to [`data/servers.yaml`](data/servers.yaml). Copy an existing entry and follow the field notes at the top of the file.
2. For a new vendor's official server, also add the vendor to [`data/vendors.yaml`](data/vendors.yaml).
3. Run the checks locally:

   ```bash
   pip install -r requirements.txt
   python scripts/validate.py
   python scripts/render.py   # optional: preview the README
   ```

4. Open the PR. A bot refreshes stars and the README after it's merged.

## What gets in

- The server is about **getting data from the web**: scraping, crawling, browser automation, unblocking, search or extraction. Website-specific servers (one site only) are welcome if the site is widely used.
- It works and is maintained, or is new enough to be given the benefit of the doubt.
- Closed-source servers with a public, documented endpoint are fine; they just have no stars to rank on.
- The description is one plain sentence about what it does. "Best", "#1", "ultimate" and similar words are rejected by the validator.
- Free tiers must be quoted from the vendor's own docs or pricing page.

## Official vs community

- **Official**: published by the company or open-source project behind the tool the server uses.
- **Community**: everything else, including servers that wrap a vendor's API but aren't published by that vendor.

## Vendors

Vendors are welcome to add and update their own servers. Please say in the PR that you work for the vendor. Placement is decided by the automatic ranking ([METHODOLOGY.md](METHODOLOGY.md)), never by who submitted the entry.

## Removing or correcting an entry

Open an issue or PR. If you maintain a listed server and want it removed, we'll remove it.
