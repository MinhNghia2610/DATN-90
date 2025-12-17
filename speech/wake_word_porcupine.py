import pvporcupine
import sounddevice as sd
import struct

class WakeWordDetector:
    def __init__(self, access_key):
        self.porcupine = pvporcupine.create(
            access_key=access_key,
            keywords=["jarvis"]
        )

    def listen(self):
        with sd.RawInputStream(
            samplerate=self.porcupine.sample_rate,
            blocksize=self.porcupine.frame_length,
            dtype="int16",
            channels=1
        ) as stream:

            while True:
                pcm = stream.read(self.porcupine.frame_length)[0]
                pcm = struct.unpack_from(
                    "h" * self.porcupine.frame_length, pcm
                )

                if self.porcupine.process(pcm) >= 0:
                    return True
