# Sample support tickets for a finance company.
# Each one is a real-sounding ticket paired with the category
# a human agent would have routed it to.

TICKETS = [
    # Fraud Alert
    ("I see a charge on my card from a store I've never been to.", "Fraud Alert"),
    ("Someone used my account to make a purchase in another country.", "Fraud Alert"),
    ("There's a withdrawal I never made showing up on my statement.", "Fraud Alert"),
    ("My card was declined but I never even tried to use it today.", "Fraud Alert"),
    ("I think my account got hacked, there are transactions I don't recognize.", "Fraud Alert"),
    ("Please freeze my card, I lost my wallet and I'm worried someone will use it.", "Fraud Alert"),
    ("I got a text saying my card was used at a gas station across the country.", "Fraud Alert"),
    ("Someone changed my account email without my permission.", "Fraud Alert"),

    # Billing Dispute
    ("I was charged twice for the same monthly subscription fee.", "Billing Dispute"),
    ("This late fee is wrong, I paid before the due date.", "Billing Dispute"),
    ("Why was I charged an annual fee when my card is supposed to be free?", "Billing Dispute"),
    ("I returned the item but the refund never showed up on my statement.", "Billing Dispute"),
    ("My interest charge this month is way higher than usual, can you explain?", "Billing Dispute"),
    ("I was billed for a service I cancelled two months ago.", "Billing Dispute"),
    ("The exchange rate you used for my overseas purchase seems off.", "Billing Dispute"),
    ("I want to dispute a charge from a merchant that never shipped my order.", "Billing Dispute"),

    # Account Access
    ("I can't log into my online banking, it says my password is wrong.", "Account Access"),
    ("The app keeps logging me out every time I open it.", "Account Access"),
    ("I never got the verification code to reset my password.", "Account Access"),
    ("My account is locked after too many failed login attempts.", "Account Access"),
    ("I changed phones and now I can't get past two-factor authentication.", "Account Access"),
    ("How do I add my spouse as an authorized user on my account?", "Account Access"),
    ("I forgot the answers to my security questions, how do I reset them?", "Account Access"),
    ("Can you unlock my account, I'm locked out and need to pay a bill today.", "Account Access"),

    # Loan Inquiry
    ("What's the current interest rate on a 30 year mortgage?", "Loan Inquiry"),
    ("How long does it take to get approved for a personal loan?", "Loan Inquiry"),
    ("Can I refinance my car loan to get a lower monthly payment?", "Loan Inquiry"),
    ("What documents do I need to apply for a small business loan?", "Loan Inquiry"),
    ("Is there a penalty if I pay off my loan early?", "Loan Inquiry"),
    ("I want to know my remaining balance on my student loan.", "Loan Inquiry"),
    ("What credit score do I need to qualify for a home equity loan?", "Loan Inquiry"),
    ("Can I increase my loan amount after it's already been approved?", "Loan Inquiry"),

    # Investment Question
    ("How do I move money from my checking account into my brokerage account?", "Investment Question"),
    ("What's the difference between a Roth IRA and a traditional IRA?", "Investment Question"),
    ("Can you explain how dividends get paid out on my mutual fund?", "Investment Question"),
    ("I want to rebalance my portfolio, how do I do that in the app?", "Investment Question"),
    ("What are the fees for managing my retirement account?", "Investment Question"),
    ("How do I set up automatic contributions to my index fund?", "Investment Question"),
    ("Can I withdraw from my 401k early without a penalty?", "Investment Question"),
    ("What happens to my stocks if the company gets acquired?", "Investment Question"),

    # Compliance / Regulatory
    ("I need a copy of my tax documents for last year.", "Compliance/Regulatory"),
    ("Why do you need my ID again, I already verified my identity last year.", "Compliance/Regulatory"),
    ("Can you explain why my large deposit triggered a review?", "Compliance/Regulatory"),
    ("I got a letter about updating my information for anti money laundering rules.", "Compliance/Regulatory"),
    ("What's your policy on reporting international wire transfers?", "Compliance/Regulatory"),
    ("I need proof that my account complies with FDIC insurance limits.", "Compliance/Regulatory"),
    ("Why is there a hold on my transfer pending compliance review?", "Compliance/Regulatory"),
    ("Can you send me your privacy policy regarding data sharing?", "Compliance/Regulatory"),

    # Technical Issue
    ("The mobile app crashes every time I try to deposit a check.", "Technical Issue"),
    ("Your website keeps timing out when I try to view my statements.", "Technical Issue"),
    ("The transfer button on the app isn't responding at all.", "Technical Issue"),
    ("I can't download my monthly statement, the PDF link is broken.", "Technical Issue"),
    ("Your app shows my balance as zero even though I know that's wrong.", "Technical Issue"),
    ("The fingerprint login stopped working after the last update.", "Technical Issue"),
    ("I keep getting an error page when I try to submit a payment.", "Technical Issue"),
    ("The chart showing my spending history won't load on the dashboard.", "Technical Issue"),
]
