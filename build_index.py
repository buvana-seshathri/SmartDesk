import chromadb
from tickets import TICKETS

# Stores the database as files in ./chroma_db so it persists between runs
client = chromadb.PersistentClient(path="./chroma_db")

client.delete_collection("tickets") if "tickets" in [c.name for c in client.list_collections()] else None
collection = client.create_collection("tickets")

texts = [text for text, category in TICKETS]
categories = [category for text, category in TICKETS]
ids = [str(i) for i in range(len(TICKETS))]

# Chroma embeds the text for us automatically using its default model
collection.add(
    documents=texts,
    metadatas=[{"category": c} for c in categories],
    ids=ids,
)

print(f"Indexed {len(TICKETS)} tickets into ChromaDB.")
