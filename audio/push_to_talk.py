import keyboard
import time
from audio.recorder import Recorder

class PushToTalk:
    def __init__(self):
        self.recorder = Recorder()

    def listen(self):
        print("👉 Giữ SPACE để nói")

        keyboard.wait("space")
        print("🎙️ Listening...")
        self.recorder.start()

        while keyboard.is_pressed("space"):
            time.sleep(0.01)

        self.recorder.stop()
        print("🛑 Stop recording")
