#!/usr/bin/env python3
"""Update Jekyll statistics data from GoatCounter aggregate stats."""

from __future__ import annotations

import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


SITE_CODE = os.environ.get("GOATCOUNTER_CODE", "fyimu").strip()
TOKEN = os.environ.get("GOATCOUNTER_TOKEN", "").strip()
API_BASE = f"https://{SITE_CODE}.goatcounter.com/api/v0"
OUTPUT_PATH = "_data/statistics.yml"


def api_get(path: str, params: dict[str, str | int] | None = None) -> dict:
    if not TOKEN:
        raise RuntimeError("GOATCOUNTER_TOKEN is not set.")

    query = f"?{urllib.parse.urlencode(params)}" if params else ""
    request = urllib.request.Request(
        f"{API_BASE}{path}{query}",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN}",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GoatCounter API returned {error.code}: {body}") from error


def iso_hour(value: dt.datetime) -> str:
    return value.replace(minute=0, second=0, microsecond=0).isoformat().replace("+00:00", "Z")


def fetch_locations(params: dict[str, str | int]) -> dict[str, int]:
    countries: dict[str, int] = {}
    offset = 0

    while True:
        data = api_get("/stats/locations", {**params, "limit": 100, "offset": offset})
        for item in data.get("stats", []):
            code = str(item.get("id") or item.get("name") or "").upper()
            count = int(item.get("count") or 0)
            if len(code) == 2 and code.isalpha() and count > 0:
                countries[code] = countries.get(code, 0) + count

        if not data.get("more"):
            break
        offset += 100

    return dict(sorted(countries.items()))


def write_statistics(total_visits: int, countries: dict[str, int]) -> None:
    lines = [
        f"total_visits: {total_visits}",
        "countries:",
    ]

    if countries:
        lines.extend(f"  {code}: {count}" for code, count in countries.items())
    else:
        lines.append("  {}")

    with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
        file.write("\n".join(lines) + "\n")


def main() -> int:
    if not SITE_CODE:
        raise RuntimeError("GOATCOUNTER_CODE is not set.")

    now = dt.datetime.now(dt.timezone.utc)
    params = {
        "start": "2020-01-01T00:00:00Z",
        "end": iso_hour(now),
    }

    total_data = api_get("/stats/total", params)
    total_visits = int(total_data.get("total") or 0)
    countries = fetch_locations(params)
    write_statistics(total_visits, countries)

    print(f"Updated {OUTPUT_PATH}: {total_visits} visits across {len(countries)} countries.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
