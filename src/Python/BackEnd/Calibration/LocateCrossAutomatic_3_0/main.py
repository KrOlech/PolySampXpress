from cv2 import cvtColor, COLOR_BGR2GRAY, moments, threshold, THRESH_BINARY
from matplotlib import pyplot as plt

from Python.BaseClass.Logger.Logger import Loger


class LocateCross(Loger):
    x, y = 0, 0
    dataX, dataY = None, None

    def __init__(self, master, name=""):
        self.master = master
        self.name = name

    def locateCross(self, negation=False):
        photo = self.master.camera.getFrame()

        gsc = cvtColor(photo, COLOR_BGR2GRAY)

        _, binary_image = threshold(gsc, 127, 255, THRESH_BINARY)

        self.x, self.y = self.findCenterOfMass(binary_image)

        if self.x and self.y:
            self.loger(
                f"position of the marker point: {self.x} px, {self.y}px  for zoom:{self.master.zoom} with name: {self.name}")

            self.__crateAndSaveResults(self.markSpot(binary_image))

        return self.x, self.y

    def findCenterOfMass(self, gsc):

        M = moments(gsc)

        # Calculate x, y coordinate of the center
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            self.logError("Was not abble to found center")

            return 0, 0

        return cY, cX

    def markSpot(self, photo):
        for i in range(max(0, self.x - 6), min(self.x + 5, len(photo))):
            for j in range(max(0, self.y - 6), min(self.y + 5, len(photo[0]))):
                photo[i][j] = 1

        return photo

    def __crateAndSaveResults(self, photo):
        plt.close()
        plt.cla()
        plt.clf()
        plt.imshow(photo)

        plt.savefig(f"{self.name}.png")
