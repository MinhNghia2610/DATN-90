import numpy as np

def auto_gain(audio, target_rms=0.1):
    rms = np.sqrt(np.mean(audio**2))
    if rms > 0:
        audio = audio * (target_rms / rms)
    return audio
