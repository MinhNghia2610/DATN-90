import sounddevice as sd
import soundfile as sf
import numpy as np
from config.setting import SAMPLE_RATE, CHANNELS, INPUT_AUDIO


class Recorder:
    def __init__(self):
        self.frames = []
        self.recording = False
        self.stream = None

    def _callback(self, indata, frames, time, status):
        if status:
            print("⚠️ Audio status:", status)
        if self.recording:
            self.frames.append(indata.copy())

    def start(self):
        print("🎙️ Bắt đầu ghi âm...")
        self.frames = []
        self.recording = True

        self.stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="int16",          # QUAN TRỌNG
            callback=self._callback
        )
        self.stream.start()

    def stop(self):
        print("🛑 Dừng ghi âm...")
        self.recording = False

        if self.stream:
            self.stream.stop()
            self.stream.close()

        if not self.frames:
            print("❌ Không có dữ liệu audio")
            return

        # Ghép các frame thành 1 mảng numpy
        audio = np.concatenate(self.frames, axis=0)

        # Ghi file WAV
        sf.write(
            file=INPUT_AUDIO,
            data=audio,
            samplerate=SAMPLE_RATE,
            subtype="PCM_16"
        )

        print(f"✅ Đã lưu audio: {INPUT_AUDIO}")
