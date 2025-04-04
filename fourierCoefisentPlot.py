import numpy as np
import matplotlib.pyplot as plt


def cn(n, A=1):
    """Compute Fourier coefficients for the half-wave rectified sine wave."""
    if n == 0:
        return A / np.pi
    elif n == 1:
        return A / (4j)
    elif n == -1:
        return -A / (4j)
    elif n % 2 == 0:
        return A / (np.pi * (1 - n**2))
    else:
        return 0


plt.style.use("seaborn-v0_8-dark")

T = 1
t = np.linspace(-T * 2, T * 2, 10000)

n_terms = 10
n_values = np.arange(0, n_terms + 1)
c_values = np.array([cn(n) * (n == 0) + (n != 0) * cn(n) * 2 for n in n_values])

plt.grid(True, linestyle="--", alpha=0.6)
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.stem(n_values, np.abs(c_values))
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.title("Amplituder til fourier koeffisient cn")
plt.savefig("./bilder/fourerKOefisenter.png")
plt.show()