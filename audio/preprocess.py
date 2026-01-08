from audio.filter import highpass_filter
from audio.noise_gate import noise_gate
from audio.gain import auto_gain
from audio.normalize import normalize

def preprocess(audio, sr=16000):
    audio = highpass_filter(audio, fs=sr)
    audio = auto_gain(audio)
    audio = normalize(audio)

    if not noise_gate(audio):
        return None

    return audio
