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


T = 1
t = np.linspace(-T * 2, T * 2, 10000)


for n_terms in [1, 2, 3, 5, 10, 20, 50, 100]:
    n_values = np.arange(0, n_terms + 1)
    c_values = np.array([cn(n) * (n == 0) + (n != 0) * cn(n) * 2 for n in n_values])

    plt.stem(n_values, np.abs(c_values))

    plt.show()

    n_values = np.arange(-n_terms, n_terms + 1)
    c_values = np.array([cn(n) for n in n_values])

    x_approx = np.zeros_like(t, dtype=np.complex128)
    for i in range(len(n_values)):
        wK = 2 * np.pi * n_values[i] / T
        x_approx += c_values[i] * np.exp(1j * wK * t)

    x_approx = x_approx.real

    plt.figure(figsize=(8, 4))
    plt.plot(t, x_approx, label=f"Fourier Approx. ({n_terms} terms)", color="blue")
    plt.plot(
        t,
        np.maximum(0, np.sin(2 * np.pi * t / T)),
        label="Original Signal",
        linestyle="dashed",
        color="red",
    )
    plt.xlabel("t")
    plt.ylabel("x(t)")
    plt.legend()
    plt.title(f"Fourier Series Approximation with {n_terms} Terms")
    plt.grid()
    plt.show()
