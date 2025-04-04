import matplotlib.ticker as mticker 
import codecs
import csv
import numpy as np
import matplotlib.pyplot as plt


def loadDataFourier(fileName):
    dataFile = codecs.open(r"./data/"+fileName+".csv", encoding="utf-8", errors="ignore")

    skipLinesStart = 40
    skipLinesEnd = -1
    f,amplitude,forskyv= np.array(list(csv.reader(dataFile.readlines()[skipLinesStart:skipLinesEnd])),dtype=float).T
    dataFile.close()

    return {
        "frekvens":f,
        "amplitude":amplitude,
        "forskyvning":forskyv,
    }



if __name__ == "__main__":
    fileName = "forier rms 1k ohm"
    data = loadDataOscilloscope(fileName)
    f = data["frekvens"]
    amplitude = data["amplitude"]
    deg = data["forskyvning"]
    plt.plot(f,amplitude)
    plt.show()
    plt.plot(f,deg)
    plt.show()
