import fourierMesurmentDataExstractor as fM
import osicloscopeDataExstractor as oD
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

measureFileName = [f"rms mesumernt {name} ohm" for name in ["1k", "100", "50"]]
oscilloscopeFileName = [
    f"signalDobler {name} ohm oscilo" for name in ["1k", "100", "50"]
]


def SDR(dataMeasure, dataOscilloscope):
    VxHatAndre = dataOscilloscope["rms"] ** 2

    frekvens: np.ndarray = dataMeasure["frekvens"]
    frekvensIndex = np.where(frekvens == 2.4)
    VxAndre = dataMeasure["rms"][frekvensIndex] ** 2
    sdr = VxAndre / (VxHatAndre - VxAndre)
    sdrDB = 10 * np.log10(sdr)
    return [sdr, sdrDB,dataMeasure["rms"][frekvensIndex],dataOscilloscope["rms"]]


measureData = [fM.loadDataMeasurements(fileName) for fileName in measureFileName]
oscilloscopeData = [
    oD.loadDataOscilloscope(fileName) for fileName in oscilloscopeFileName
]


def normalize(x):
    return 2 * (x - np.min(x)) / (np.max(x) - np.min(x)) - 1


tableFile = open("tableFiles.txt", mode="w", encoding="utf-8")

def Q(R):
    if R == "1k":
        R = 1000
    R = int(R)
    return np.sqrt(0.1 / (47e-9 * R**2))


plt.style.use("seaborn-v0_8-dark")

plt.figure(figsize=(12, 8))

#   MOtsdand  sdr sdrDB verdi  Q VERDI Vrms vhatrms
# plt.tight_layout()
for data in zip(measureData, oscilloscopeData, ["1k", "100", "50"], [1, 2, 3]):
    SDRVals = SDR(data[0], data[1])
    print(f"R={data[2]} | SDR:{SDRVals[0][0]} | SDRdB:{SDRVals[1][0]}")
    R =data[2]
    if data[2] == "1k":
        R = "1000"
    tableFile.write(f"{int(R)} &  {float(SDRVals[0][0]):.3} &  {float(SDRVals[1][0]):.3} & {float(Q(data[2])):.3} & {float(SDRVals[2]):.3}& {float(SDRVals[3]):.3} \\\\ \n")
    tableFile.write("\\hline \n")

    T = 1 / 2.4e3

    t = data[1]["tid"] - np.min(data[1]["tid"])
    signal = data[1]["signal"]

    tStart = np.where(signal > 0)[0][0]
    tEnd = np.where(t > 2 * T)[0][0]
    # print(tStart)
    t = t[tStart:tEnd]
    signal = signal[tStart:tEnd]

    t -= np.min(t)
    pickPoint = np.where(np.max(signal) == signal)[0][0]
    normalizedSignal = normalize(signal)
    phi = (
        -2 * t[pickPoint] * np.pi * 1 / T
        + 2 * np.pi
        + np.asin(normalizedSignal[pickPoint])
    )
    # print(np.rad2deg( phi))
    plt.subplot(3, 1, data[3])

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)

    plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f mV"))
    plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f ms"))

    plt.xlabel("Tid [ms]", fontsize=12)
    plt.ylabel("Spenning [mV]", fontsize=12)

    plt.title(
        f"SDR = {SDRVals[1][0]:.2f}dB, R={data[2]}Ω", fontsize=14, fontweight="bold"
    )

    plt.plot(
        t * 1000,
        1000 * np.max(signal) * np.sin(t * 2 * np.pi / T + phi),
        linestyle="--",
        linewidth=2,
        color="royalblue",
        label="Ønsket signal",
    )
    plt.plot(
        t * 1000, signal * 1000, linewidth=2, color="crimson", label="Faktisk signal"
    )

    plt.legend(frameon=True, edgecolor="dimgray", facecolor="lavender", fontsize=12)

plt.tight_layout()
tableFile.write("\n---------------------- \n")

tableFile.flush()
tableFile.close()


plt.savefig("./bilder/treSignaler.png")
plt.show()
