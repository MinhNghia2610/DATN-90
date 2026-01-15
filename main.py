import threading
from ui.ollie_gui import OLLIEUI
from audio.push_to_talk import PushToTalk
from stt.vosk_stt import VoskSTT
from llm.ollama_client import OllamaClient
from tts.vietnamese_tts import VietnameseTTS
from audio.player import Player

def ollie_loop(ui):
    ptt = PushToTalk()
    stt = VoskSTT()
    llm = OllamaClient()
    tts = VietnameseTTS()
    player = Player()

    ui.ready()

    while True:
        ui.listening()
        ptt.listen()

        text = stt.transcribe()
        if not text:
            ui.log_text("❌ Không nghe rõ")
            continue

        ui.log_text(f"🗣 Bạn: {text}")
        ui.thinking()

        answer = llm.ask(text)
        ui.log_text(f"🤖 OLLIE: {answer}")

        tts.speak(answer)
        ui.speaking()
        player.play("data/output.mp3")

def main():
    ui = OLLIEUI()

    threading.Thread(
        target=ollie_loop,
        args=(ui,),
        daemon=True
    ).start()

    ui.run()

if __name__ == "__main__":
    main()
