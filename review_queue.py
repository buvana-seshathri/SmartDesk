import json
import os
import uuid
from datetime import datetime

QUEUE_FILE = "review_queue.json"


def _load():
    if not os.path.exists(QUEUE_FILE):
        return []
    with open(QUEUE_FILE, "r") as f:
        content = f.read().strip()
        return json.loads(content) if content else []


def _save(items):
    with open(QUEUE_FILE, "w") as f:
        json.dump(items, f, indent=2)


def add_to_queue(ticket_text, confidence, top_guess):
    items = _load()
    items.append({
        "id": uuid.uuid4().hex[:8],
        "ticket": ticket_text,
        "confidence": confidence,
        "top_guess": top_guess,
        "flagged_at": datetime.now().isoformat(timespec="seconds"),
    })
    _save(items)


def get_queue():
    return _load()


def resolve_ticket(ticket_id):
    items = _load()
    items = [item for item in items if item["id"] != ticket_id]
    _save(items)
