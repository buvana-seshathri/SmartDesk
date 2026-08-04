import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("tickets")

CONFIDENCE_THRESHOLD = 0.48  # tuned after testing against real queries


def route_ticket(ticket_text, top_k=3):
    ticket_text = ticket_text.strip()
    if not ticket_text:
        return {
            "ticket": ticket_text,
            "category": None,
            "top_guess": None,
            "confidence": 0.0,
            "needs_review": True,
            "nearest": [],
        }

    results = collection.query(query_texts=[ticket_text], n_results=top_k)

    matched_texts = results["documents"][0]
    matched_categories = [meta["category"] for meta in results["metadatas"][0]]
    distances = results["distances"][0]

    # Turn distance (lower = more similar) into a 0-1 similarity score
    similarities = [1 / (1 + d) for d in distances]

    top_category = matched_categories[0]
    confidence = similarities[0]
    needs_review = confidence < CONFIDENCE_THRESHOLD

    nearest = [
        {"text": text, "category": category, "similarity": round(sim, 2)}
        for text, category, sim in zip(matched_texts, matched_categories, similarities)
    ]

    return {
        "ticket": ticket_text,
        "category": None if needs_review else top_category,
        "top_guess": top_category,
        "confidence": round(confidence, 2),
        "needs_review": needs_review,
        "nearest": nearest,
    }
