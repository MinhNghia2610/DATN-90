import numpy as np

def noise_gate(audio, threshold=0.01):
    rms = np.sqrt(np.mean(audio ** 2))
    return rms > threshold
