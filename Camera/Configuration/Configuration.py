class Configuration:

    def set(self, width: int = 640, height: int = 480, fps: int = 25):
        self.setWidth(width)
        self.setHight(height)
        self.setFps(fps)
        self.setBritnes(100)

    def setBritnes(self, value: int = 200) -> None:
        self.__setValue(self._BRIGHTNESS.address, value)

    def setWidth(self, width: int) -> None:
        self.__setValue(self._WIDTH.address, width)

    def setHight(self, height: int) -> None:
        self.__setValue(self._HEIGHT.address, height)

    def setFps(self, fps: int) -> None:
        self.__setValue(self._FPS.address, fps)

    def __setValue(self, propertyID: int, value: int) -> None:
        self.device.set(propertyID, value)
