def evaluate_answer(query: str, answer: str, docs: list):

    query_lower = query.lower()

    # If no docs retrieved
    if docs is None or len(docs) == 0:
        return 0.2

    # Detect problem / incident queries
    support_keywords = [
        "rejected",
        "not working",
        "crash",
        "failed",
        "issue",
        "problem",
        "cannot",
        "can't",
        "error"
    ]

    for word in support_keywords:
        if word in query_lower:
            return 0.4

    # Uncertainty in answer
    uncertainty_phrases = [
        "i don't know",
        "not sure",
        "cannot find",
        "no information"
    ]

    for phrase in uncertainty_phrases:
        if phrase in answer.lower():
            return 0.3

    # Short answers
    if len(answer.split()) < 10:
        return 0.4

    return 0.9