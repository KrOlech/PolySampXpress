import numpy as np
from matplotlib import image as mpimg


class dumyCamera:
    class Camera:
        WIDTH, HEIGHT = 600, 600

        def getFrame(self):
            return mpimg.imread('crosv2.png')

    camera = Camera()

    zoom = 1



