# EEG Measures

This repository contains implementations of various measures for analyzing EEG data, focusing on connectivity and phase relationships between signals. These measures are essential for understanding brain functionality and dynamics.

## Measures Implemented

### 1. Weighted Phase Lag Index (wPLI)
The **Weighted Phase Lag Index (wPLI)** quantifies the phase synchronization between two signals while accounting for zero-lag contributions. This measure helps reduce spurious correlations, providing a more reliable estimate of connectivity in EEG analysis.

### 2. Phase Lag Index (PLI)
The **Phase Lag Index (PLI)** measures the phase relationship between two signals, indicating the direction of phase differences. It is useful for revealing how one signal leads or lags another, helping to identify connectivity patterns in brain activity.

### 3. Directed Phase Lag Index (dPLI)
The **Directed Phase Lag Index (dPLI)** extends the PLI by quantifying the directed influence of one signal on another. This measure helps determine the directionality of interactions between brain regions, providing insights into causal relationships in neural dynamics.

### 4. Coherence
**Coherence** measures the correlation between two signals in the frequency domain, reflecting how well the signals co-vary at specific frequencies. It is useful for identifying shared oscillatory activity between different brain regions and understanding their functional connectivity.

