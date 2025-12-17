WAKE_WORDS = [
    "ê quản gia",
    "ê quan gia",
    "này quản gia"
]

def is_wake_word(text: str) -> bool:
    text = text.lower()
    return any(w in text for w in WAKE_WORDS)
