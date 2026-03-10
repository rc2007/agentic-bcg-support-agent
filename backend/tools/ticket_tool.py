from langchain.tools import tool
import uuid
from datetime import datetime


@tool
def create_support_ticket(query: str):
    """
    Creates a support ticket for unresolved employee queries.
    """

    ticket_id = str(uuid.uuid4())[:8]

    ticket = {
        "ticket_id": ticket_id,
        "issue": query,
        "status": "OPEN",
        "created_at": datetime.utcnow().isoformat()
    }

    print("Ticket created:", ticket)

    return ticket