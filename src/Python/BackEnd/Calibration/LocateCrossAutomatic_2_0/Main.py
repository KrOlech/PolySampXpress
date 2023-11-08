from cv2 import cvtColor, COLOR_BGR2GRAY
from numpy import array, transpose, linspace

from src.Python.BaseClass.Logger.Logger import Loger
from matplotlib import pyplot as plt


class LocateCross(Loger):
    x, y = 0, 0
    dataX, dataY = None, None

    def __init__(self, master, name=""):
        self.master = master
        self.name = name

    def locateCross(self):
        photo = self.master.camera.getFrame()

        gsc = cvtColor(photo, COLOR_BGR2GRAY)

        self.x, self.dataX = self.analyzePhotoX(gsc)
        self.y, self.dataY = self.analyzePhotoY(gsc)

        self.loger(
            f"position of the marker point: {self.x}, {self.y} for zoom:_ with name: {self.name}")  # todo when Zoom implemented add zoom value

        self.__crateAndSaveResults(self.markSpot(photo))

        return self.x, self.y

    @staticmethod
    def analyzePhotoX(photo):
        return LocateCross.__analyzePhoto(photo)

    @staticmethod
    def analyzePhotoY(photo: array):
        return LocateCross.__analyzePhoto(transpose(photo))

    @staticmethod
    def __analyzePhoto(photo):
        rowValue = [sum(row) for row in photo]
        mValue = max(rowValue)
        return rowValue.index(min(rowValue)), [v / mValue for v in rowValue]

    def markSpot(self, photo):
        for i in range(self.x - 6, self.x + 5):
            for j in range(self.y - 6, self.y + 5):
                photo[i][j] = [1., 0., 0.]
        return photo

    def __crateAndSaveResults(self, photo):
        fig, axs = plt.subplots(2, 2, figsize=(6, 6))

        axs[0, 0].imshow(photo)

        x = len(self.dataX)
        y = len(self.dataY)

        axs[0, 1].plot(self.dataX, linspace(0, x, x))
        axs[1, 0].plot(linspace(0, y, y), self.dataY)

        axs[0, 1].invert_xaxis()
        axs[0, 1].invert_yaxis()

        axs[0, 0].axis('off')
        axs[1, 1].axis('off')

        plt.savefig(f"{self.name}.png")


if __name__ == "__main__":
    from src.Python.BackEnd.Calibration.LocateCrossAutomatic_2_0.dumyCamera import dumyCamera

    main = dumyCamera()
    loc = LocateCross(main)
    loc.locateCross()
