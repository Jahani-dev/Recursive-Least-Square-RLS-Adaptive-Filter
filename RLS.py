#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:43:19 2024

@author: Sahar Jahani
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulating noisy signal
np.random.seed(0)
n_samples = 300
t = np.linspace(0, 4 * np.pi, n_samples)
true_signal = 2 * np.sin(t)  # True signal
noise = np.random.normal(0, 1, n_samples) # noise
noisy_signal = true_signal + noise  # noisy signal

# Initialization
M = 5                # Filter length - to capture noise delay
lambdA = 0.9          # Forgetting factor
delta = 0.5           # uncertainty
w = np.zeros(M)       # filter weights
P = (1 / delta) * np.eye(M)  # inverse correlation matrix

y = np.zeros(n_samples)  # Filter output
e = np.zeros(n_samples)  # Error

# RLS loop
for n in range(M, n_samples):
    
    x_vec = noisy_signal[n-M:n][::-1]  # Most recent inputs (reversed)
    d = true_signal[n]                 # Desired output
    k = P @ x_vec / (lambdA + x_vec.T @ P @ x_vec) # Kalman gain calculation
    y[n] = w @ x_vec # Output prediction
    e[n] = d - y[n] # Error
    w = w + k * e[n] # Update weights
    P = (P - np.outer(k, P @ x_vec)) / lambdA # Update P matrix

# Results Visualization
plt.figure(figsize=(12, 5))
plt.plot(t, noisy_signal, label='Noisy Signal', linewidth = 1, color = 'blue', alpha = 0.8)
plt.plot(t, true_signal, label='True Signal', linewidth = 2, color = 'red')
plt.plot(t, y, label='RLS Estimated Signal', linewidth = 2, color = 'green')
plt.xlabel('Time', fontsize = 14, fontweight='bold')
plt.ylabel('Amplitude', fontweight='bold')
plt.title('Recursive Least Squares (RLS) Filter', fontweight='bold')
legend = plt.legend()
for text in legend.get_texts():
    text.set_fontweight('bold')
    text.set_fontsize(12)
plt.show()
