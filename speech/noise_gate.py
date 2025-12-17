import numpy as np

def noise_gate(audio_data, threshold=500):
    """
    audio_data: bytes (int16)
    threshold: độ lớn âm thanh tối thiểu
    """
    audio_np = np.frombuffer(audio_data, dtype=np.int16)
    volume = np.abs(audio_np).mean()

    return volume > threshold
