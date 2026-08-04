from router import route_ticket

# Held-out tickets, written in the same style as tickets.py but never indexed.
# This is our tiny "test set" — a rough gut check on real-world accuracy.
TEST_TICKETS = [
    ("I noticed a $500 withdrawal I never made from an ATM out of state.", "Fraud Alert"),
    ("My subscription fee was taken out twice this month.", "Billing Dispute"),
    ("I keep getting logged out of the app every few minutes.", "Account Access"),
    ("What's the interest rate on your 15 year mortgage right now?", "Loan Inquiry"),
    ("How do dividends get taxed in a regular brokerage account?", "Investment Question"),
    ("I need proof of my account history for a loan application I'm doing elsewhere.", "Compliance/Regulatory"),
    ("The check deposit feature keeps failing halfway through.", "Technical Issue"),
    ("Why do I see a fee for a wire transfer I never sent?", "Billing Dispute"),
    ("Someone tried logging into my account from a browser I don't recognize.", "Fraud Alert"),
    ("Can I set up biometric login on a new phone?", "Account Access"),
]


def run_eval():
    correct = 0
    for ticket_text, expected_category in TEST_TICKETS:
        result = route_ticket(ticket_text)
        got = result["top_guess"]
        is_correct = got == expected_category
        correct += is_correct

        status = "correct" if is_correct else "WRONG"
        print(f"[{status}] expected={expected_category} got={got} conf={result['confidence']}")
        print(f"  \"{ticket_text}\"")

    accuracy = round((correct / len(TEST_TICKETS)) * 100)
    print(f"\nAccuracy: {correct}/{len(TEST_TICKETS)} ({accuracy}%)")


if __name__ == "__main__":
    run_eval()
