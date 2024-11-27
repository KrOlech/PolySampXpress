from Python.BaseClass.JsonRead.JsonRead import JsonHandling


class CalculateAndSaveResults:

    def __init__(self, fun):
        self.fun = fun

        self.funName = fun.__name__

    def __call__(self, img, *args, **kwargs):
        return self.fun(img)

    def saveResults(self, img, fokus):
        value = self(img)

        with open(JsonHandling.getFileLocation(f"{self.funName}.dat"), "a") as file:
            file.write(f"{fokus},{value}\n")

    def show(self, plt):
        x = []
        y = []
        with open(JsonHandling.getFileLocation(f"{self.funName}.dat"), "r") as file:
            while line := file.readline():
                x.append(float(line[:line.find(",")]))
                y.append(float(line[line.find(",") + 1:]))
        maxY = max(y)

        plt.plot(x, [w / maxY for w in y], label=self.funName)
