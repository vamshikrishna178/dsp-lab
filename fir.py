import numpy as np
import matplotlib.pyplot as plt

def compute_h(w, z1):
 
    z = np.exp(1j * w)  
    return 1 - z1 * (1 / z)  
r = float(input("Enter r: "))
w0 = float(input("Enter w0 (in radians): "))
z1 = r * np.exp(1j * w0)
w = np.linspace(-np.pi, np.pi, int(2 * np.pi / 0.0001) + 1)
h_w = compute_h(w, z1)
magnitude = np.abs(h_w)
phase = np.angle(h_w)
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(w, magnitude)
plt.title('Magnitude of h(z)')
plt.xlabel('Frequency (w)')
plt.ylabel('|h(z)|')
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(w, phase)
plt.title('Phase of h(z)')
plt.xlabel('Frequency (w)')
plt.ylabel('Phase (radians)')
plt.grid()
plt.tight_layout()
plt.show()
