import unicodedata

WAKE_WORDS = [
    "ê ollie cho tôi hỏi",
    "e ollie cho toi hoi",
    "ê oli cho tôi hỏi",
    "ee oli cho toi hỏi",
    "ê ollie cho tôi hoi",
    "ee ollie cho tooi hoir"
]

def normalize(text: str) -> str:
    """
    Chuẩn hóa tiếng Việt:
    - lowercase
    - bỏ dấu
    """
    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return text

def is_wake_word(text: str) -> bool:
    text_norm = normalize(text)

    for w in WAKE_WORDS:
        if normalize(w) in text_norm:
            return True

    return False
