import cv2

from Camera.GetFrame.main import GetFrame
from src.Camera.ComonNames.ComonNames import CommonNames
from src.BaseClass.JsonRead.JsonRead import JsonHandling


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
