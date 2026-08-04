import json
import os
from datetime import datetime

LOG_FILE = "auto_routed.json"


def _load():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        content = f.read().strip()
        return json.loads(content) if content else []


def _save(items):
    with open(LOG_FILE, "w") as f:
        json.dump(items, f, indent=2)


def log_auto_routed(ticket_text, category, confidence):
    items = _load()
    items.append({
        "ticket": ticket_text,
        "category": category,
        "confidence": confidence,
        "routed_at": datetime.now().isoformat(timespec="seconds"),
    })
    _save(items)


def get_auto_routed():
    return _load()
