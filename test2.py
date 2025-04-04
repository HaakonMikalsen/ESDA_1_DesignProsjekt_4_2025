import fourierDataExstractor as FDE
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker 

resistorValues =["1k","100","50"]
fourierFileName = [f"forier rms {name} ohm" for name in resistorValues]




fourierData = [FDE.loadDataFourier(fileName) for fileName in fourierFileName]
rawOutputData = FDE.loadDataFourier("forier rms raw ohm")

# plt.style.use("seaborn-v0_8-dark")

# plt.figure(figsize=(12, 8))

# plt.tight_layout()
for data in zip(fourierData,resistorValues,[1,2,3]):
    f = data[0]["frekvens"]
    differenceAmp = data[0]["amplitude"]/rawOutputData["amplitude"]
    
    plt.style.use("seaborn-v0_8-dark")
    plt.plot(f,data[0]["amplitude"])
    plt.plot(rawOutputData["frekvens"],rawOutputData["amplitude"])
    # plt.plot(f,differenceAmp)
    plt.show()

plt.tight_layout()
plt.show()    