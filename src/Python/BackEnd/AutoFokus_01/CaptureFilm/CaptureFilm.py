from cv2 import imwrite


class CaptureFilm:

    def __init__(self, manipulatorInterface, camera):
        self.manipulatorInterface = manipulatorInterface
        self.camera = camera

    def run(self):
        for i in range(-10000, 10000, 100):
            self.manipulatorInterface.fokusGoTo(i)
            imwrite(f"{i}_.png", self.camera.getFrame())
