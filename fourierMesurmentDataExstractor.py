import matplotlib.ticker as mticker 
import codecs
import csv
import numpy as np
import matplotlib.pyplot as plt






def loadDataMeasurements(fileName):
    dataFile = codecs.open(r"./data/"+fileName+".csv", encoding="utf-8", errors="ignore")


    skipLinesStart = 9
    skipLinesEnd = -1
    kanal,navn,rms,f= np.array(list(csv.reader(dataFile.readlines()[skipLinesStart:skipLinesEnd]))).T
    dataFile.close()

    f = np.array([element.replace(" kHz","") for element in f],dtype=float)
    rms = np.array([element.replace(" Ṽ","").replace(" mṼ","e-3") for element in rms],dtype=float)
    
    return {
            "rms":rms,
            "frekvens":f,
        }




if __name__ == "__main__":
    fileName = "rms mesumernt 1k ohm"
    data = loadDataMeasurements(fileName)

    rms = data["rms"]
    f = data["frekvens"]

    for f,rms in zip(f,rms):
        print(f"{f}:{rms}")