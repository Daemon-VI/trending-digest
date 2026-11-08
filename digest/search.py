"""Query the GitHub search API for beginner-friendly issues in popular repos."""
import json
import urllib.parse
import urllib.request

API = "https://api.github.com/search/issues"


def build_query(language: str, label: str = "good first issue") -> str:
    return f'label:"{label}" language:{language} state:open type:issue'


def fetch_issues(language: str, limit: int = 10) -> list[dict]:
    params = urllib.parse.urlencode(
        {"q": build_query(language), "sort": "reactions", "per_page": limit}
    )
    req = urllib.request.Request(
        f"{API}?{params}", headers={"Accept": "application/vnd.github+json"}
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.load(resp)["items"]
