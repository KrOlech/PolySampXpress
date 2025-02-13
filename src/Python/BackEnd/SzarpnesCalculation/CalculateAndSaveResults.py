import os

from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from Python.BaseClass.Logger.Logger import Loger


class CalculateAndSaveResults(Loger):
    value = None

    def __init__(self, fun):
        self.fun = fun

        self.funName = fun.__name__

    def __call__(self, img, *args, **kwargs):
        self.value = self.fun(img)
        return self.fun(img)

    def cleanFiles(self):
        if os.path.exists(JsonHandling.getFileLocation(f"{self.funName}.dat")):
            os.remove(JsonHandling.getFileLocation(f"{self.funName}.dat"))
        else:
            self.loger(f"The previous file for {self.funName} do not exist")

    def saveResults(self, img, fokus, fokusReal=None, file_localisation=None):
        value = self(img)

        if file_localisation:
            self.path = file_localisation + f"{self.funName}.dat"
        else:
            self.path = JsonHandling.getFileLocation(f"{self.funName}.dat")

        with open(self.path, "a") as file:
            file.write(f"{fokus},{value},{fokusReal}\n")
            self.loger(f"{self.funName} - Fokus position:{fokus}, Value: {value}, fokusReal: {fokusReal}")

    def logResults(self, img, fokus):
        self.loger(f"{self.funName} - Fokus position:{fokus}, Value: {self(img)}")

    def show(self, plt): #todo better Name is plpting no showing
        x = []
        y = []
        z = []
        with open(self.path, "r") as file:
            while line := file.readline():
                x.append(float(line[:line.find(",")]))
                y.append(float(line[line.find(",") + 1:line.rfind(",")]))
                z.append(float(line[line.rfind(",") + 1:]))

        maxY = max(y)
        try:
            if all(z) and False:
                plt.plot(z, [w / maxY for w in y], label=self.funName)
            else:
                plt.plot(x, [w / maxY for w in y], label=self.funName)
        except ZeroDivisionError:
            self.logError("Max focus is 0")
