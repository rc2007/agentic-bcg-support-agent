def route_query(query: str):

    q = query.lower()

    # HR Leave
    if any(word in q for word in [
        "leave", "vacation", "annual leave", "sick leave", "holiday"
    ]):
        return "hr_leave"

    # HR Work From Home
    if any(word in q for word in [
        "work from home", "wfh", "remote work", "home office"
    ]):
        return "hr_wfh"

    # Finance Expense
    if any(word in q for word in [
        "expense", "reimbursement", "receipt", "expense claim"
    ]):
        return "finance_expense"

    # Finance Travel
    if any(word in q for word in [
        "travel", "flight", "hotel", "business trip", "travel reimbursement"
    ]):
        return "finance_travel"

    # IT Laptop
    if any(word in q for word in [
        "laptop", "device", "computer", "new laptop"
    ]):
        return "it_laptop"

    # IT VPN
    if any(word in q for word in [
        "vpn", "network access", "remote login", "vpn password"
    ]):
        return "it_vpn"

    return "general"