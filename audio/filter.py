import numpy as np

def noise_gate(audio, threshold=0.01):
    audio[np.abs(audio) < threshold] = 0
    return audio
