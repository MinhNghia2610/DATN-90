def route(text):
    text = text.lower()

    if "mở chrome" in text:
        return "chrome"

    if "tắt máy" in text:
        return "shutdown"

    if "mở code" in text:
        return "vscode"

    if "nhạc" in text:
        return "spotify"

    if "thời tiết" in text:
        return "weather"

    return "chat"
