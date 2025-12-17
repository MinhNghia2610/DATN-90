import sounddevice as sd
import vosk
import json
import os

from speech.noise_gate import noise_gate


class VoskListener:
    def __init__(
        self,
        model_path="model/vosk-model-small-vn-0.4",
        sample_rate=16000,
        device=None
    ):
        self.sample_rate = sample_rate
        self.device = device

        # ✅ Kiểm tra model tồn tại
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"❌ Không tìm thấy Vosk model tại: {model_path}")

        print("🔄 Đang load Vosk model...")
        self.model = vosk.Model(model_path)
        self.rec = vosk.KaldiRecognizer(self.model, self.sample_rate)
        self.rec.SetWords(False)
        print("✅ Vosk sẵn sàng")

    def listen(self) -> str:
        """
        Lắng nghe cho tới khi nhận được 1 câu nói hợp lệ
        """
        with sd.RawInputStream(
            samplerate=self.sample_rate,
            blocksize=8000,
            dtype="int16",
            channels=1,
            device=self.device
        ) as stream:

            while True:
                data, _ = stream.read(4000)

                # 🔇 Noise gate – bỏ qua nếu chỉ có nhiễu
                if not noise_gate(data):
                    continue

                # ✅ Khi nhận đủ 1 câu
                if self.rec.AcceptWaveform(data):
                    result = json.loads(self.rec.Result())
                    text = result.get("text", "").strip()

                    # 🔁 Reset recognizer để chuẩn bị cho câu sau
                    self.rec.Reset()

                    if text:
                        return text
