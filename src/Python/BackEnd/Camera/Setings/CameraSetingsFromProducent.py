from src.Python.BackEnd.Camera.FromProducent.Abstract import AbstractCameraFromProducent


class CameraSettingsFromProducent(AbstractCameraFromProducent):

    def showProducentSettings(self):
        self.tisgrabber.IC_ShowPropertyDialog(self.master.camera.handle)
