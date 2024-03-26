import numpy as np
import scipy.signal as signal

def wPLI(data1, data2, num_epochs, scaling='spectrum', window='boxcar', fs=2000, nperseg=2000, noverlap=0):
    """
    Compute the weighted Phase Lag Index (wPLI) between two sets of EEG data.

    Args:
        data1 (numpy.ndarray): EEG data for the first set of electrodes.
        data2 (numpy.ndarray): EEG data for the second set of electrodes.
        num_epochs (int): Number of epochs for averaging.
        scaling (str, optional): Scaling method. Defaults to 'spectrum'.
        window (str, optional): Window function. Defaults to 'boxcar'.
        fs (int, optional): Sampling frequency. Defaults to 2000 Hz.
        nperseg (int, optional): Length of each segment. Defaults to 2000.
        noverlap (int, optional): Number of overlapping samples. Defaults to 0.

    Returns:
        tuple: Frequency array, wPLI values, numerator of wPLI, denominator of wPLI.
    """
    # Initializing the scores. These scores will be used to calculate the expected value.
    f, Pxy = signal.csd(data1[0, :], data2[0, :], fs=fs, scaling=scaling,
                        window=window, nperseg=nperseg, noverlap=noverlap, average="mean", detrend='linear')
    scores = np.zeros((2, len(f)))
    
    # Calculate wPLI scores for each epoch
    for epoch in range(num_epochs):
        f, Pxy = signal.csd(data1[epoch, :], data2[epoch, :], fs=fs, scaling=scaling,
                            window=window, nperseg=nperseg, noverlap=noverlap, average="mean", detrend='linear')
        Ixy = np.imag(Pxy)
        scores[0] += Ixy
        scores[1] += np.abs(Ixy)

    # Average the scores across epochs
    num = scores[0] / num_epochs
    den = scores[1] / num_epochs
    # Ensure den is not zero to avoid division by zero
    den[np.where(num == 0.)] = 1.

    return f, (np.abs(num) / den), num, den
