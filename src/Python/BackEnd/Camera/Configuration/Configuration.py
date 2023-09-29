import cv2


class Configuration:

    def configurationSetUp(self, width: int = 640, height: int = 480, fps: int = 25) -> None:
        self.setWidth(width)
        self.setHight(height)
        self.setFps(fps)

    def setBritnes(self, value: int = 200) -> None:
        self.__setValue(self.brightness.address, value)

    def setWidth(self, width: int) -> None:
        self.__setValue(self.width.address, width)

    def setHight(self, height: int) -> None:
        self.__setValue(self.height.address, height)

    def setFps(self, fps: int) -> None:
        self.__setValue(self.fps.address, fps)

    def __setValue(self, propertyID: int, value: int) -> None:
        self.device.set(propertyID, value)
