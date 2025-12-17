from speech.vosk_listener import VoskListener
from speech.wake_word import is_wake_word
from speech.speak import speak

from ai.ollama_client import ask_ollama
from ai.router import route

from skills.spotify import play_music
from skills.weather import get_weather

from ui.terminal_ui import show


def handle_command(command: str) -> str:
    """
    Xử lý lệnh sau khi wake word
    """
    action = route(command)

    if action == "spotify":
        return play_music()

    if action == "weather":
        return get_weather()

    return ask_ollama(command)


def main():
    listener = VoskListener()

    print("🤖 Quản gia đang chạy nền... (Gọi: Ê quản gia)")

    while True:
        # 1️⃣ Nghe nền (wake word)
        text = listener.listen()
        show(f"Nghe được: {text}")

        if not is_wake_word(text):
            continue

        # 2️⃣ Phản hồi wake word
        wake_reply = "Tôi đây, bạn cần gì?"
        show(wake_reply)
        speak(wake_reply)

        # 3️⃣ Nghe lệnh
        command = listener.listen()
        if not command:
            continue

        show(f"Lệnh: {command}")

        # 4️⃣ Xử lý lệnh
        reply = handle_command(command)

        # 5️⃣ Trả lời
        show(reply)
        speak(reply)


if __name__ == "__main__":
    main()
