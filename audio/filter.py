import numpy as np
from scipy.signal import butter, lfilter

def highpass_filter(data, cutoff=80, fs=16000, order=5):
    nyq = fs * 0.5
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return lfilter(b, a, data)
