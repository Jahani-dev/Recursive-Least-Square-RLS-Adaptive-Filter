# RLS Adaptive Filter — Noise Cancellation Demo

A Python educational example demonstrating how an M-tap Recursive Least Squares (RLS) filter can estimate a clean signal from noisy observations.

## Recursive-Least-Square-RLS-Adaptive-Filter

This repo contains a single Python script that demonstrates Recursive Least Squares (RLS) adaptive filtering.
It builds a clean sine wave, adds Gaussian noise, and uses an M-tap RLS filter to estimate the clean signal back from the noisy observation.

## Overview

This project shows how the **RLS adaptive filter** can recover a clean signal from noisy data.  
- Generates a **true sine-wave signal**, adds **Gaussian noise**, then uses an **M-tap RLS filter** to estimate the original signal.
- Includes a plot comparing the **noisy input**, **true signal**, and **RLS output**.

## Problem Statement

- **True Signal**: A clean sine wave (`2 * sin(t)`)  
- **Noise**: White Gaussian noise added to the true signal  
- **Objective**: Recover the original signal using RLS adaptive filtering


## Algorithm Explanation

The RLS filter minimizes the exponential‐weighted sum of squared errors. Each iteration performs:

1. Form the input vector:  
   `x_vec = [x[n], x[n-1], ..., x[n-M+1]]^T`

2. Predict output:  
   `y_hat[n] = w^T x_vec`

3. Compute error:  
   `e[n] = d[n] - y_hat[n]`

4. Compute gain vector:  
   `k = (P x_vec) / (λ + x_vec^T P x_vec)`

5. Update weights:  
   `w = w + k e[n]`

6. Update inverse covariance P:  
   `P = (P - k x_vec^T P) / λ`

## Parameters:

- **M**: Filter length (number of taps), which gives the filter memory.
- **λ**: Forgetting factor (0 < λ ≤ 1).
- **δ**: Initialization constant for `P = (1/δ) I`.


## Results Visualization

The plot below shows the noisy signal (blue), the true clean signal (red), and the RLS-estimated signal (green):

![RLS Noise Removal](RLS_Noise_Removal.png)


### Possible extensions

- Simulate delayed/noisy references and auto-select M via cross-correlation
- Compare RLS to LMS/NLMS variants
- Extend to real biomedical noise scenarios (EEG, ECG, etc.)


## Author

Sahar Jahani  
[GitHub Profile](https://github.com/Jahani-dev)
