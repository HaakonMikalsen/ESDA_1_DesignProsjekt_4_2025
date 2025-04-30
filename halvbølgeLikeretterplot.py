import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-dark")



t = np.linspace(0,4*np.pi,1000)
plt.plot(t,np.clip(np.sin(t),0,1) ,color="blue",label="y")
# plt.plot(t,np.sin(t),linestyle="--",color="red",label="x1")
plt.title("Sinussignal igjennom halvbølge likeretter")
plt.legend(frameon=True, edgecolor="dimgray", facecolor="lavender", fontsize=12)
plt.xlabel("Tid")
plt.ylabel("Amplitude")

plt.grid(True, linestyle="--", alpha=0.6)
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.savefig("bilder/halvbølgeLikeretter.png")
plt.show()