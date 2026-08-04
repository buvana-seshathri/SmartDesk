from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from router import route_ticket

app = FastAPI()

# Allows the browser to call this API when index.html is opened directly as a file
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


class TicketRequest(BaseModel):
    text: str


@app.post("/route")
def route(request: TicketRequest):
    return route_ticket(request.text)
