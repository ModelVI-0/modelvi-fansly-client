# fansly-api-client-example

A minimal, honest example of a **Fansly API** client — showing the classic **auth → fetch → post** pattern in just a few lines of code. Built to run against [fanslyapi.com](https://fanslyapi.com), a managed API gateway for **Fansly automation** workflows.

> **This is an EXAMPLE integration.** The endpoints in the code are placeholders. See **[fanslyapi.com/docs](https://fanslyapi.com/docs)** for the live endpoints and full reference.

---

## What it does

This repo demonstrates the smallest useful shape of a Fansly API client:

- **Auth** — authenticate every request with your fanslyapi.com API key
- **Fetch** — read data (e.g. account/profile info) with a small GET helper
- **Post** — send data (e.g. publish or schedule an update) with a small POST helper

It's intentionally tiny and dependency-light (Python standard library only) so you can read the whole thing in one sitting and adapt it to your own stack.

## Why — the agency use-case

Agencies and teams that manage multiple creator accounts often repeat the same manual work: pulling account data, syncing content calendars, and posting updates on a schedule. A programmatic **Fansly API** turns that manual grind into **Fansly automation** — one integration, many accounts, no copy-paste.

This example is the starting point: wire up auth once, then build your own scheduling, reporting, or CRM sync on top of it.

## Install

```bash
git clone https://github.com/YOUR_ORG/fansly-api-client-example.git
cd fansly-api-client-example
cp .env.example .env   # then add your API key (see below)
```

Requires **Python 3.8+**. No third-party packages — the example uses only the standard library.

## Configuration (`.env`)

Copy `.env.example` to `.env` and fill in your values. Both are placeholders until you drop in the real key and base URL from your fanslyapi.com dashboard:

```dotenv
# Your API key from https://fanslyapi.com  (required)
API_KEY=your_api_key_here

# API base URL — confirm the correct value in the docs
BASE_URL=https://api.fanslyapi.com
```

## Usage

Once your key is in `.env`, run the example:

```bash
python example.py
```

`example.py` authenticates with your API key, runs a sample **fetch**, and shows the shape of a **post** call. The endpoints are clearly marked as placeholders in the code — swap them for the real ones from the docs. Open the file; it's short and heavily commented.

## → Get your API key

This example **requires** a fanslyapi.com API key.

**→ Get your API key at [https://fanslyapi.com](https://fanslyapi.com)**

Sign up, grab a key from the dashboard, drop it into `.env`, and you're ready to build.

## Honest note

This is an **example integration** meant to teach the client pattern — it is not a full SDK. The endpoint paths and any response shapes shown in comments are **illustrative placeholders**, not guaranteed schemas. For the authoritative, live endpoints, request/response formats, rate limits, and authentication details, always refer to the official docs:

**→ [https://fanslyapi.com/docs](https://fanslyapi.com/docs)**

## License

MIT — use it, fork it, build on it.
