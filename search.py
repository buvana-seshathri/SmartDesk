from router import route_ticket

if __name__ == "__main__":
    print("SmartDesk ticket router. Type a ticket and press enter (or 'quit' to exit).")
    while True:
        ticket_text = input("\n> ")
        if ticket_text.lower() == "quit":
            break

        result = route_ticket(ticket_text)

        if result["needs_review"]:
            print(f"Needs human review  (confidence too low: {result['confidence']})")
        else:
            print(f"Routed to: {result['category']}  (confidence: {result['confidence']})")

        print("Nearest past tickets:")
        for match in result["nearest"]:
            print(f"  [{match['similarity']}] ({match['category']}) {match['text']}")
