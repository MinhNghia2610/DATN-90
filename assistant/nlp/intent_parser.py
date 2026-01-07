def parse_intent(text: str):
    text = text.lower()

    if "spotify" in text or "nhạc" in text:
        if "bật" in text or "mở" in text or "play" in text:
            return ("spotify_play", None)
        if "tạm dừng" in text or "pause" in text:
            return ("spotify_pause", None)

    if "thời tiết" in text:
        return ("weather", None)

    return ("unknown", None)
