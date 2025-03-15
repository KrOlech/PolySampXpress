from cv2 import cvtColor, COLOR_BGR2GRAY, moments, threshold, THRESH_BINARY
from matplotlib import pyplot as plt

from Python.BaseClass.Logger.Logger import Loger


class LocateCross(Loger):
    x: int = 0
    y: int = 0

    xCenter: int = 0
    yCenter: int = 0

    areaMinX: int = 0
    areaMaxX: int = 0
    areaMinY: int = 0
    areaMaxY: int = 0

    dataX, dataY = None, None

    SIZE: int = 200

    def __init__(self, master, name=""):
        self.master = master
        self.name = name

    def locateCross(self, negation=False, area=False):
        photo = self.master.camera.getFrame()

        gsc = cvtColor(photo, COLOR_BGR2GRAY)

        _, binary_image_og = threshold(gsc, 127, 255, THRESH_BINARY)

        if area:
            self.xCenter = len(photo) // 2
            self.yCenter = len(photo[0]) // 2

            self.areaMinX = self.xCenter - self.SIZE
            self.areaMaxX = self.xCenter + self.SIZE
            self.areaMinY = self.yCenter - self.SIZE
            self.areaMaxY = self.yCenter + self.SIZE

            binary_image = binary_image_og[self.areaMinX:self.areaMaxX, self.areaMinY:self.areaMaxY]

            tempX, tempY = self.findCenterOfMass(binary_image)
            self.x, self.y = tempX + self.areaMinX, tempY + self.areaMinY

        else:
            self.x, self.y = self.findCenterOfMass(binary_image_og)

        if self.x and self.y:
            self.loger(
                f"position of the marker point: {self.x} px, {self.y}px  for zoom:{self.master.zoom} with name: {self.name}")

            self.__crateAndSaveResults(self.markSpot(binary_image_og, area))

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

    def markSpot(self, photo, area=False):
        for i in range(max(0, self.x - 10), min(self.x + 10, len(photo))):
            for j in range(max(0, self.y - 10), min(self.y + 10, len(photo[0]))):
                self.__markPixel(photo, i, j)

        if area:
            for i in range(self.areaMinX, self.areaMaxX):
                self.__markPixel(photo, i, self.areaMinY)
                self.__markPixel(photo, i, self.areaMaxY)

            for j in range(self.areaMinY, self.areaMaxY):
                self.__markPixel(photo, self.areaMinX, j)
                self.__markPixel(photo, self.areaMaxX, j)

        return photo

    def __markPixel(self, photo, i, j):
        if photo[i][j]:
            photo[i][j] = 0
        else:
            photo[i][j] = 255
        return photo

    def __crateAndSaveResults(self, photo):
        plt.close()
        plt.cla()
        plt.clf()
        # plt.imshow(photo)
        try:
            plt.imsave(f"{self.name}.png", photo, cmap='gray')
        except Exception as e:
            self.logError(e)
