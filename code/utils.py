def clean_text(text: str) -> str:
    """Clean text for Sanskrit processing"""
    return " ".join(text.split())