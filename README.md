# modelvi-fansly-client — schedule posts to Fansly via the ModelVI API

A minimal **example integration** (Python) that schedules posts to **Fansly** through the [ModelVI](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=modelvi-fansly-client) partner API — one of the 14 creator platforms ModelVI posts to (code `FAN`).

**[▶ Get your API key →](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=modelvi-fansly-client)** · [API docs](https://modelvi.com/agent-api) · [Pricing](https://modelvi.com/pricing)

![example](https://img.shields.io/badge/example-MIT-blue) ![python](https://img.shields.io/badge/python-3.9+-green)

---

> **Honest scope:** ModelVI is an independent posting/automation tool. **Fansly is a third-party platform ModelVI posts _to_** — this is **not** an official Fansly API and isn't affiliated with Fansly. It's a small client that uses ModelVI's partner API to schedule content on a creator's connected Fansly account (platform code `FAN`).

## What this is

An MIT-licensed example that authenticates with a ModelVI partner key (`mvk_<keyId>_<secret>`) and schedules a post to Fansly via `POST /schedule` with `platforms: ["FAN"]`. It talks only to the public ModelVI partner API.

## Quickstart

```bash
pip install requests
export MODELVI_API_KEY="mvk_<keyId>_<secret>"
python example.py
```

`example.py` reads a model id from `GET /model_list`, then sends `POST /schedule` with the caption (`title`), `platforms: ["FAN"]`, `scheduledAt` (ISO-8601 UTC), and `type` (`1`=FREE · `2`=FANS · `3`=PAID). Responses are `{ "success": true, "payload": … }`.

## Use cases / keywords

**fansly posting bot** · postbot fansly · auto post fansly · fansly automation · fansly scheduler · schedule fansly posts · post to Fansly via API · creator posting automation.

## Honest note

Minimal example — no retries/pagination/media upload. Authoritative reference: **[modelvi.com/agent-api](https://modelvi.com/agent-api)** · **[modelvi.com/partner-api-docs](https://modelvi.com/partner-api-docs)**. Public ModelVI partner API only; no proprietary logic here.

**[▶ Get your API key →](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=modelvi-fansly-client)** — see [pricing](https://modelvi.com/pricing). MIT licensed.
