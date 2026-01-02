from gtts import gTTS
from config.setting import OUTPUT_AUDIO

class VietnameseTTS:
    def speak(self, text):
        tts = gTTS(text=text, lang="vi")
        tts.save(OUTPUT_AUDIO)
