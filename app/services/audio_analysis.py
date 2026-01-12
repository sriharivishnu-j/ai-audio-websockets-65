import numpy as np
from scipy.io import wavfile
import io
import logging

logger = logging.getLogger(__name__)

def analyze_audio(audio_bytes: bytes) -> str:
    try:
        rate, data = wavfile.read(io.BytesIO(audio_bytes))
        if data.ndim > 1:
            data = data.mean(axis=1)
        features = extract_features(data, rate)
        logger.info(f"Extracted features: {features}")
        return f"Analysis complete: {features}"
    except Exception as e:
        logger.error(f"Error analyzing audio: {e}")
        return "Error analyzing audio"

def extract_features(data: np.ndarray, rate: int) -> dict:
    duration = len(data) / rate
    mean_amplitude = np.mean(np.abs(data))
    return {
        "duration": duration,
        "mean_amplitude": mean_amplitude
    }