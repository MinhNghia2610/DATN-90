import sounddevice as sd
import soundfile as sf
from config.setting import SAMPLE_RATE, CHANNELS, INPUT_AUDIO

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
            callback=self._callback
        )
        self.stream.start()

    def stop(self):
        self.recording = False
        self.stream.stop()
        self.stream.close()

        audio = b"".join(frame.tobytes() for frame in self.frames)
        sf.write(INPUT_AUDIO, audio, SAMPLE_RATE, subtype="PCM_16")
