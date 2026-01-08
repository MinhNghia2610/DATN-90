import numpy as np

def normalize(audio):
    peak = np.max(np.abs(audio))
    if peak == 0:
        return audio
    return audio / peak
