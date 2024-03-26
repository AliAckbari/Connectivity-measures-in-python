import numpy as np
from scipy.signal import welch, csd

def coherence(signal_x, signal_y, sampling_frequency=2500, segment_length_seconds=1, segment_overlap_fraction=0.5):
    """
    Calculate the coherence between two LFP signals.

    Parameters
    ----------
    signal_x : 1D array
        LFP signal from different channels with dimensions (channels X samples)
    sampling_frequency : int, optional
        Sampling frequency, defaults to 2500 Hz
    segment_length_seconds : float, optional
        Length of the segments for which the spectral density is calculated in seconds, defaults to 1 second
    segment_overlap_fraction : float, optional
        Fraction of overlap between the segments represented as a float number between 0 (no overlap) and 1 (complete overlap), defaults to 0.5

    Returns
    ----------
    frequencies : 1D array
        Frequencies for which the coherence is calculated
    coherence_values : 1D array
        Coherence takes a value between 0 and 1, with 0 or 1 representing no or perfect coherence, respectively
    phase_lags : 1D array
        Estimate of phase lag in radians between the input time series for each frequency

    """

    # Transform segment from seconds to samples
    segment_samples = int(sampling_frequency * segment_length_seconds)
    overlap_samples = int(segment_overlap_fraction * segment_samples)

    # Calculate coherence
    frequencies, power_x = welch(signal_x, fs=sampling_frequency, nperseg=segment_samples, noverlap=overlap_samples)
    _, power_y = welch(signal_y, fs=sampling_frequency, nperseg=segment_samples, noverlap=overlap_samples)
    _, cross_power = csd(signal_x, signal_y, fs=sampling_frequency, nperseg=segment_samples, noverlap=overlap_samples)
    
    # Calculate coherence and phase lag
    coherence_values = np.abs(cross_power) ** 2 / (power_x * power_y)
    phase_lags = np.angle(cross_power)

    return frequencies, coherence_values, phase_lags
