#!/usr/bin/env python3
"""
modelvi-fansly-client

Schedule a post to Fansly via the public ModelVI partner API.

Honest scope: ModelVI is an independent posting tool; Fansly is a third-party
platform ModelVI posts TO. This is NOT an official Fansly API. It uses ModelVI's
partner API with platform code "FAN".

  Get an API key:  https://modelvi.com/sign-up
  API reference:   https://modelvi.com/agent-api

Minimal EXAMPLE (no retries/pagination/media upload).

  export MODELVI_API_KEY="mvk_<keyId>_<secret>"
  python example.py
"""

import os
import sys
from datetime import datetime, timezone, timedelta

import requests  # pip install requests

BASE_URL = os.environ.get("MODELVI_API_BASE", "https://modelvi.com/api/partner/v1")
API_KEY = os.environ.get("MODELVI_API_KEY")
SIGNUP_URL = "https://modelvi.com/sign-up"
PLATFORM = "FAN"  # Fansly platform code


def _headers():
    if not API_KEY:
        sys.exit(f"Missing MODELVI_API_KEY. Get a key at {SIGNUP_URL} and export it.")
    return {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}


def _payload(resp):
    if resp.status_code == 401:
        sys.exit(f"Unauthorized (401). Get a valid key at {SIGNUP_URL}")
    resp.raise_for_status()
    body = resp.json()
    return body.get("payload", body)


def main():
    models = _payload(requests.get(f"{BASE_URL}/model_list", headers=_headers(), timeout=30))
    if not models:
        sys.exit("No models on this account yet — add one in your ModelVI dashboard.")
    model = models[0] if isinstance(models, list) else models.get("items", [{}])[0]
    model_id = model.get("id") or model.get("model")

    when = datetime.now(timezone.utc) + timedelta(minutes=5)
    body = {
        "model": model_id,
        "platforms": [PLATFORM],
        "title": "New drop is live ✨",          # the caption field is `title`
        "scheduledAt": when.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "type": 1,                                # 1=FREE, 2=FANS, 3=PAID
    }
    print(f"POST {BASE_URL}/schedule → {PLATFORM}")
    print("Scheduled:", _payload(requests.post(f"{BASE_URL}/schedule", json=body,
                                               headers=_headers(), timeout=30)))


if __name__ == "__main__":
    main()
