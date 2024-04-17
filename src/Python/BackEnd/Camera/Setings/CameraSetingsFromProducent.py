from Python.BackEnd.Camera.FromProducent.Abstract import AbstractCameraFromProducent


class CameraSettingsFromProducent(AbstractCameraFromProducent):

    def showProducentSettings(self):
        self.ic.IC_ShowPropertyDialog(self.master.camera.handle)
