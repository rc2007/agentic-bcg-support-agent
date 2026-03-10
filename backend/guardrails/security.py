def detect_prompt_injection(query: str) -> bool:

    blocked = [
        "ignore previous instructions",
        "reveal system prompt",
        "act as developer",
        "system prompt",
        "bypass safety",
        "jailbreak"
    ]

    query_lower = query.lower()

    for phrase in blocked:
        if phrase in query_lower:
            return True

    return False