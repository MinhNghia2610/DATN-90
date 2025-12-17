import sounddevice as sd
import vosk
import json

MODEL_PATH = "speech/model"
SAMPLE_RATE = 16000

model = vosk.Model(MODEL_PATH)

def listen():
    rec = vosk.KaldiRecognizer(model, SAMPLE_RATE)
    rec.SetWords(False)

    with sd.RawInputStream(
        samplerate=SAMPLE_RATE,
        blocksize=8000,
        dtype="int16",
        channels=1
    ) as stream:

        print("🎤 Đang nghe...")

        while True:
            data = stream.read(4000)[0]
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").strip()
                if text:
                    return text
