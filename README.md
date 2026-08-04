# SmartDesk

An AI-powered support ticket router for a finance company. Paste in a ticket, and instead of keyword matching, it finds the most *semantically* similar past tickets and routes based on that - with a confidence score, and a human-review fallback when it's not sure.

The UI is intentionally simple. The actual project is what's happening underneath it: an embeddings + vector search pipeline standing in for a human triaging tickets every morning.

## Why this exists

I used to do this job manually - checking my team's ticket queue multiple times a day and routing each one to the right sub-team lead. It works, but it doesn't scale, and busy days meant things sometimes slipped through. Keyword matching is the obvious fix, but it breaks the moment someone phrases things differently than expected ("there's a payment I don't remember approving" has zero words in common with "fraud"). This project is an attempt to fix that with meaning-based matching instead of word-based matching.

## How it works

1. A set of ~100 past tickets (already labeled by category) get embedded and stored in a local vector database (ChromaDB).
2. A new ticket gets embedded the same way, and the database returns its nearest neighbors.
3. The category of the closest match becomes the routing decision - *if* the similarity score clears a confidence threshold.
4. If it doesn't, the ticket goes to a review queue instead of getting auto-routed, where an admin can look at it and decide manually.

This keeps a human in the loop, but only for the cases that actually need one - not every ticket.

## Categories

Fraud Alert · Billing Dispute · Account Access · Loan Inquiry · Investment Question · Compliance/Regulatory · Technical Issue

## Project structure

```
tickets.py          sample ticket dataset (~105 tickets, 15 per category)
build_index.py       embeds tickets.py and stores them in ChromaDB
router.py            core routing logic (embed → search → confidence check)
app.py                FastAPI server: serves the pages + API endpoints
review_queue.py      stores tickets flagged for human review
auto_routed.py       logs tickets that were confidently auto-routed
stats.py              tracks auto-routing rate over time
eval.py                small accuracy check against held-out test tickets
home.html             landing page (User / Admin)
index.html            ticket submission page
review.html           admin dashboard: review queue + auto-routed log
```

## Running it

```bash
pip install chromadb fastapi uvicorn

# builds the vector database from tickets.py - rerun this any time tickets.py changes
python3 build_index.py

# starts the server
uvicorn app:app --reload
```

Then open **http://127.0.0.1:8000/** in your browser.

To check accuracy against held-out test tickets:

```bash
python3 eval.py
```

## API

| Endpoint | Method | Description |
|---|---|---|
| `/route` | POST | Route a ticket. Body: `{"text": "..."}` |
| `/review-queue` | GET | List tickets flagged for human review |
| `/review-queue/{id}` | DELETE | Mark a flagged ticket resolved |
| `/auto-routed` | GET | List confidently auto-routed tickets |
| `/stats` | GET | Auto-routing rate + totals |

## Tech stack

- **Python** - core logic
- **ChromaDB** - vector database, stores ticket embeddings locally
- **FastAPI** - backend API + page serving
- **Vanilla HTML/CSS/JS** - frontend, no framework

## What I learned building this

- Embeddings and semantic search - how meaning-based matching differs from keyword matching
- Vector databases - storing and querying by similarity instead of exact match
- Why confidence thresholds matter, and how to tune one against real data instead of guessing
- Small-dataset effects: going from ~9 to ~15 examples per category took held-out accuracy from inconsistent to 100% on my test set
- Human-in-the-loop system design - automating the easy majority of decisions while keeping a human for the ones the model is unsure about

## Notes

- The dataset is small and self-written (~105 tickets), so this is a proof of concept, not a production-scale system.
- The confidence threshold (0.48) was tuned against manual testing, not a rigorous eval - a larger held-out test set would make that number more trustworthy.
