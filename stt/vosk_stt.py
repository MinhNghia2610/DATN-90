import wave
import json
from vosk import Model, KaldiRecognizer
from config.setting import VOSK_MODEL_PATH, INPUT_AUDIO, SAMPLE_RATE

class VoskSTT:
    def __init__(self):
        self.model = Model(VOSK_MODEL_PATH)
        self.rec = KaldiRecognizer(self.model, SAMPLE_RATE)

    def transcribe(self):
        wf = wave.open(INPUT_AUDIO, "rb")
        result_text = ""

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if self.rec.AcceptWaveform(data):
                res = json.loads(self.rec.Result())
                result_text += res.get("text", "") + " "

        final = json.loads(self.rec.FinalResult())
        result_text += final.get("text", "")
        return result_text.strip()
