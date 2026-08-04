import json
import os
from datetime import datetime

QUEUE_FILE = "review_queue.json"


def _load():
    if not os.path.exists(QUEUE_FILE):
        return []
    with open(QUEUE_FILE, "r") as f:
        return json.load(f)


def _save(items):
    with open(QUEUE_FILE, "w") as f:
        json.dump(items, f, indent=2)


def add_to_queue(ticket_text, confidence):
    items = _load()
    items.append({
        "ticket": ticket_text,
        "confidence": confidence,
        "flagged_at": datetime.now().isoformat(timespec="seconds"),
    })
    _save(items)


def get_queue():
    return _load()
