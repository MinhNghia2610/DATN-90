import sounddevice as sd
import soundfile as sf
import numpy as np

from config.setting import SAMPLE_RATE, CHANNELS, INPUT_AUDIO
from audio.noise_gate import noise_gate
from audio.filter import bandpass_filter
from audio.gain import auto_gain

class Recorder:
    def __init__(self):
        self.frames = []
        self.recording = False

    def _callback(self, indata, frames, time, status):
        if self.recording:
            self.frames.append(indata.copy())

    def start(self):
        self.frames = []
        self.recording = True

        self.stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="float32",
            callback=self._callback
        )
        self.stream.start()

    def stop(self):
        self.recording = False
        self.stream.stop()
        self.stream.close()

        audio = np.concatenate(self.frames, axis=0)
        audio = audio.flatten()

        # 🎧 AUDIO PROCESSING
        audio = noise_gate(audio)
        audio = bandpass_filter(audio)
        audio = auto_gain(audio)

        sf.write(INPUT_AUDIO, audio, SAMPLE_RATE, subtype="PCM_16")
