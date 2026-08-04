from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from router import route_ticket
from review_queue import add_to_queue, get_queue, resolve_ticket

app = FastAPI()

# Only needed if you ever open the HTML files directly instead of through this server
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


class TicketRequest(BaseModel):
    text: str


# --- Pages ---

@app.get("/")
def home():
    return FileResponse("home.html")


@app.get("/user")
def user_page():
    return FileResponse("index.html")


@app.get("/admin")
def admin_page():
    return FileResponse("review.html")


# --- API ---

@app.post("/route")
def route(request: TicketRequest):
    result = route_ticket(request.text)
    if result["needs_review"]:
        add_to_queue(result["ticket"], result["confidence"], result["top_guess"])
    return result


@app.get("/review-queue")
def review_queue():
    return get_queue()


@app.delete("/review-queue/{ticket_id}")
def resolve(ticket_id: str):
    resolve_ticket(ticket_id)
    return {"resolved": ticket_id}
