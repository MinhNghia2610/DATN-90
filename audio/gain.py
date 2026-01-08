import numpy as np

def auto_gain(audio, target_rms=0.1):
    rms = np.sqrt(np.mean(audio ** 2))
    if rms < 1e-6:
        return audio
    gain = target_rms / rms
    return audio * gain
