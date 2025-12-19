import os
import json
import sounddevice as sd
import vosk

from .noise_gate import noise_gate



class VoskListener:
    def __init__(self, model_path="model/vosk-model-small-vn-0.4", sample_rate=16000):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"❌ Không tìm thấy Vosk model tại: {model_path}")

        self.sample_rate = sample_rate
        self.model = vosk.Model(model_path)
        self.rec = vosk.KaldiRecognizer(self.model, self.sample_rate)
        self.rec.SetWords(False)

    def listen(self):
        with sd.RawInputStream(
            samplerate=self.sample_rate,
            blocksize=8000,
            dtype="int16",
            channels=1
        ) as stream:

            while True:
                data, _ = stream.read(4000)

                # 🔥 CỰC KỲ QUAN TRỌNG: ép buffer → bytes
                data = bytes(data)

                # 🔇 Noise gate
                if not noise_gate(data):
                    continue

                if self.rec.AcceptWaveform(data):
                    result = json.loads(self.rec.Result())
                    text = result.get("text", "").strip()

                    if text:
                        self.rec.Reset()
                        return text
