from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from router import route_ticket
from review_queue import add_to_queue, get_queue

app = FastAPI()

# Allows the browser to call this API when index.html is opened directly as a file
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


class TicketRequest(BaseModel):
    text: str


@app.post("/route")
def route(request: TicketRequest):
    result = route_ticket(request.text)
    if result["needs_review"]:
        add_to_queue(result["ticket"], result["confidence"])
    return result


@app.get("/review-queue")
def review_queue():
    return get_queue()
