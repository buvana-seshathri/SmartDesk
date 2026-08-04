import json
import os

STATS_FILE = "stats.json"


def _load():
    if not os.path.exists(STATS_FILE):
        return {"total": 0, "needs_review": 0}
    with open(STATS_FILE, "r") as f:
        content = f.read().strip()
        return json.loads(content) if content else {"total": 0, "needs_review": 0}


def _save(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=2)


def record_result(needs_review):
    stats = _load()
    stats["total"] += 1
    if needs_review:
        stats["needs_review"] += 1
    _save(stats)


def get_stats():
    stats = _load()
    total = stats["total"]
    auto_routed = total - stats["needs_review"]
    rate = round((auto_routed / total) * 100) if total else 0
    return {
        "total": total,
        "auto_routed": auto_routed,
        "needs_review": stats["needs_review"],
        "auto_route_rate": rate,
    }
