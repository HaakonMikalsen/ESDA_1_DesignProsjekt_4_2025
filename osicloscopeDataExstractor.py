import matplotlib.ticker as mticker 
import codecs
import csv
import numpy as np
import matplotlib.pyplot as plt






def loadDataOscilloscope(fileName):
    dataFile = codecs.open(r"./data/"+fileName+".csv", encoding="utf-8", errors="ignore")


    skipLinesStart = 28
    skipLinesEnd = -1
    t,signal= np.array(list(csv.reader(dataFile.readlines()[skipLinesStart:skipLinesEnd])),dtype=float).T
    dataFile.close()


    def rms(signal):
        N = len(signal)
        return np.sqrt(np.sum(signal**2)/N)
    
    return {
            "signal":signal,
            "tid":t,
            "rms":rms(signal)
        }




if __name__ == "__main__":
    fileName = "signalDobler 50 ohm oscilo"
    data = loadDataOscilloscope(fileName)
    signal = data["signal"]
    t = data["tid"]
    rmsVerdiSignal = data["rms"]
    print(rmsVerdiSignal)

    plt.axhline(y=rmsVerdiSignal)
    plt.plot(t,signal)
    plt.show()