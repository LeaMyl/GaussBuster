import numpy as np
import os
import librosa
import soundfile as sf
from scipy.signal import butter, lfilter, sosfiltfilt
from pesq import pesq
from pystoi import stoi
import tempfile
import warnings


def butter_lowpass_filter(y, cutoff=8000, sr=16000, order=5):
    """
    Apply a low-pass Butterworth filter to reduce high-frequency noise.
    This creates a slightly cleaner reference signal.
    """
    nyq = 0.5 * sr

    if cutoff <= 0:
        raise ValueError("cutoff must be > 0")

    # Compute normalized cutoff and clamp strictly inside (0,1)
    normal_cutoff = float(cutoff / nyq)
    normal_cutoff_clamped = max(min(normal_cutoff, 1.0 - 1e-9), 1e-9)

    if normal_cutoff != normal_cutoff_clamped:
        warnings.warn(
            f"Normalized cutoff {normal_cutoff:.9g} out of (0,1). Clamped to {normal_cutoff_clamped:.9g}.",
            UserWarning,
        )
        normal_cutoff = normal_cutoff_clamped

    try:
        # Prefer stable SOS + filtfilt (zero-phase). Falls back to lfilter if necessary.
        sos = butter(order, normal_cutoff, btype='low', output='sos')
        y_filtered = sosfiltfilt(sos, y)
        return y_filtered
    except Exception as e:
        warnings.warn(f"SOS filtering failed: {e}. Falling back to single-section filter.", UserWarning)
        try:
            b, a = butter(order, normal_cutoff, btype='low', analog=False)
            return lfilter(b, a, y)
        except Exception as e2:
            warnings.warn(f"Fallback lfilter failed: {e2}. Returning original signal.", UserWarning)
            return y

def compute_snr(clean, noisy):
    """
    Compute Signal-to-Noise Ratio in dB.
    SNR = 10 * log10(P_signal / P_noise)
    
    Args:
        clean: clean reference signal
        noisy: noisy signal
    
    Returns:
        float: SNR in dB
    """
    # Align signals
    min_len = min(len(clean), len(noisy))
    clean = clean[:min_len]
    noisy = noisy[:min_len]
    
    noise = noisy - clean
    signal_power = np.mean(clean ** 2)
    noise_power = np.mean(noise ** 2)
    snr = 10 * np.log10(signal_power / (noise_power + 1e-10))
    return float(snr)

def compute_psnr(clean, noisy, max_val=1.0):
    """
    Compute Peak Signal-to-Noise Ratio in dB.
    
    Args:
        clean: clean reference signal
        noisy: noisy signal
        max_val: maximum possible value of the signal
    
    Returns:
        float: PSNR in dB
    """
    # Align signals
    min_len = min(len(clean), len(noisy))
    clean = clean[:min_len]
    noisy = noisy[:min_len]

    # Calculate PSNR
    mse = np.mean((clean - noisy) ** 2)
    if mse == 0:
        return 100.0  # Perfect match, PSNR is infinite
    psnr = 20 * np.log10(max_val / np.sqrt(mse))
    return float(psnr)

def compute_mse(clean, noisy):
    """
    Compute Mean Squared Error.
    
    Args:
        clean: clean reference signal
        noisy: noisy signal
    
    Returns:
        float: MSE value
    """
    min_len = min(len(clean), len(noisy))
    clean = clean[:min_len]
    noisy = noisy[:min_len]
    
    mse = np.mean((clean - noisy) ** 2)
    return float(mse)

def compute_pesq(clean, noisy, sr=16000):
    """
    Compute PESQ score.
    
    Args:
        clean: clean reference signal
        noisy: noisy signal
        sr: sampling rate (must be 8000 or 16000)
    
    Returns:
        float: PESQ score
    """
    min_len = min(len(clean), len(noisy))
    clean = clean[:min_len]
    noisy = noisy[:min_len]
    
    if sr == 16000:
        pesq_score = pesq(sr, clean, noisy, 'wb')
    elif sr == 8000:
        pesq_score = pesq(sr, clean, noisy, 'nb')
    else:
        # Resample to 16000 Hz
        clean_resampled = librosa.resample(clean, orig_sr=sr, target_sr=16000)
        noisy_resampled = librosa.resample(noisy, orig_sr=sr, target_sr=16000)
        pesq_score = pesq(16000, clean_resampled, noisy_resampled, 'wb')
    return float(pesq_score)

def compute_stoi(clean, noisy, sr=16000):
    """
    Compute STOI score.
    
    Args:
        clean: clean reference signal
        noisy: noisy signal
        sr: sampling rate
    
    Returns:
        float: STOI score
    """
    min_len = min(len(clean), len(noisy))
    clean = clean[:min_len]
    noisy = noisy[:min_len]
    
    stoi_score = stoi(clean, noisy, sr, extended=False)
    return float(stoi_score)


