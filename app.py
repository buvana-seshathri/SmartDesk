from fastapi import FastAPI
from pydantic import BaseModel
from router import route_ticket

app = FastAPI()


class TicketRequest(BaseModel):
    text: str


@app.post("/route")
def route(request: TicketRequest):
    return route_ticket(request.text)
