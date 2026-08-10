"""
fansly-api-client-example
A minimal example client for the Fansly API: auth, fetch, post.

Runs against fanslyapi.com — a managed API gateway for Fansly automation.
  Get your API key at:            https://fanslyapi.com
  Live endpoints & reference:     https://fanslyapi.com/docs

IMPORTANT: The endpoint paths below are PLACEHOLDERS. This is an EXAMPLE
integration. Replace every path (and confirm the auth header) with the real
values from https://fanslyapi.com/docs before using this for anything real.

Standard library only — no third-party packages required (Python 3.8+).
"""

import os
import sys
import json
import urllib.request
import urllib.error


def load_dotenv(path=".env"):
    """Tiny .env loader (stdlib only) so the example runs without extra packages.
    Real projects may prefer python-dotenv or their framework's config layer."""
    if not os.path.exists(path):
        return
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())


class FanslyApiClient:
    """A tiny client demonstrating the auth -> fetch -> post pattern."""

    def __init__(self, api_key, base_url):
        # --- auth: an API key is required. Funnel: get one at fanslyapi.com ---
        if not api_key:
            raise ValueError(
                "Missing API key. Get one at https://fanslyapi.com "
                "and set API_KEY in your .env file."
            )
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def _headers(self):
        """Every request is authenticated with your fanslyapi.com API key.
        NOTE: the header name/scheme here is illustrative — confirm the real
        one at https://fanslyapi.com/docs."""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def _request(self, method, path, payload=None):
        url = f"{self.base_url}{path}"
        data = json.dumps(payload).encode("utf-8") if payload is not None else None
        req = urllib.request.Request(
            url, data=data, method=method, headers=self._headers()
        )
        try:
            with urllib.request.urlopen(req) as resp:
                body = resp.read().decode("utf-8")
                return json.loads(body) if body else {}
        except urllib.error.HTTPError as e:
            print(f"[error] {method} {path} -> HTTP {e.code}: {e.reason}", file=sys.stderr)
            print("        Check your API key and endpoint at "
                  "https://fanslyapi.com/docs", file=sys.stderr)
            raise

    # --- FETCH (read) --------------------------------------------------------
    def get_account(self):
        """Example FETCH. PLACEHOLDER endpoint — replace '/v1/account' with the
        real endpoint from https://fanslyapi.com/docs. The response shape is not
        defined here on purpose; the docs are the source of truth."""
        return self._request("GET", "/v1/account")

    # --- POST (write) --------------------------------------------------------
    def create_post(self, text):
        """Example POST. PLACEHOLDER endpoint + body — replace '/v1/posts' and the
        payload shape with the real ones from https://fanslyapi.com/docs."""
        payload = {"text": text}
        return self._request("POST", "/v1/posts", payload)


def main():
    load_dotenv()

    api_key = os.environ.get("API_KEY")
    # BASE_URL is a placeholder default — confirm the correct value in the docs.
    base_url = os.environ.get("BASE_URL", "https://api.fanslyapi.com")

    client = FanslyApiClient(api_key=api_key, base_url=base_url)

    # 1) FETCH — read account data (placeholder endpoint)
    print("Fetching account (placeholder endpoint)...")
    account = client.get_account()
    # The printed structure is whatever the live API returns — see the docs.
    print(json.dumps(account, indent=2))

    # 2) POST — send an update (placeholder endpoint)
    print("Creating a post (placeholder endpoint)...")
    result = client.create_post("Hello from the fansly-api-client-example.")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
