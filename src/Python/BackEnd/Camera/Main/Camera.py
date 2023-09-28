from src.Python.BackEnd.Camera.GetFrame.main import GetFrame
from src.Python.BackEnd.Camera.ComonNames.ComonNames import CommonNames
from src.Python.BaseClass.JsonRead.JsonRead import JsonHandling


class Camera(CommonNames, GetFrame):
    '''
    Class allowing communication with camera and adjusting her settings
    '''

    WIDTH, HEIGHT, FPS = JsonHandling.loadNativeCameraResolutionJson()

    def __init__(self, windowSize):
        self.windowSize = windowSize

        CommonNames.__init__(self)
        GetFrame.__init__(self)
        super().__init__()
