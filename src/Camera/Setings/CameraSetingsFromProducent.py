from src.Camera.FromProducent.Abstract import AbstractCameraFromProducent


class CameraSettingsFromProducent(AbstractCameraFromProducent):

    def showProducentSettings(self):
        self.tisgrabber.IC_ShowPropertyDialog(self.handle)

    def setWhiteBalanceAuto(self):
        self.tisgrabber.IC_SetWhiteBalanceAuto(self.handle, 1)