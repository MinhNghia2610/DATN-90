import unicodedata

WAKE_WORDS = [
    "quan gia",
    "quản gia",
    "quang gia",
    "quảng gia",
    "qua gia",
    "quả gia",
    "qua gian",
    "quả gian",
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
