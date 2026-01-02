from audio.push_to_talk import PushToTalk
from stt.vosk_stt import VoskSTT
from llm.ollama_client import OllamaClient
from tts.vietnamese_tts import VietnameseTTS
from audio.player import Player
from ui.console_ui import ConsoleUI

def main():
    ui = ConsoleUI()
    ptt = PushToTalk()
    stt = VoskSTT()
    llm = OllamaClient()
    tts = VietnameseTTS()
    player = Player()

    ui.ready()

    while True:
        ptt.listen()

        text = stt.transcribe()
        if not text:
            print("❌ Không nghe rõ")
            continue

        print(f"🗣 Bạn nói: {text}")
        ui.thinking()

        answer = llm.ask(text)
        print(f"🤖 Jarvis: {answer}")

        tts.speak(answer)
        ui.speaking()
        player.play("data/output.mp3")

if __name__ == "__main__":
    main()
