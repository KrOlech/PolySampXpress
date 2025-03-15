from abc import ABC
from functools import cache

from PyQt5.QtCore import QLine, QPoint
from numpy import array, dot
from numpy.linalg import linalg

from Python.BackEnd.ROI.Main.Abstract.Abstract import AbstractR


class AbstractLine(AbstractR, ABC):
    x0, x1, y0, y1 = 0, 0, 0, 0
    x0Label, x1Label, y0Label, y1Label = 0, 0, 0, 0

    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

        self.x0, self.x1, self.y0, self.y1 = self.calculateCords(**kwargs)

    def createMarker(self):
        return QLine(QPoint(self.x0, self.y0), QPoint(self.x1, self.y1))

    def getMarker(self, x, y):
        dx, dy = self.calculateOffset(x, y)
        return QLine(QPoint(self.x0 - dx, self.y0 - dy), QPoint(self.x1 - dx, self.y1 - dy))

    @cache
    def getMarkerMap(self, *args):
        x0mm, y0mm, x1mm, y1mm = self.calculateMapMarker4Cordynats(self, *args)

        return QLine(QPoint(x0mm, y0mm), QPoint(x1mm, y1mm))

    def foundCenter(self) -> (int, int):
        return (self.x1 + self.x0) // 2, (self.y1 + self.y0) // 2

    def foundAbsoluteCenter(self) -> (int, int):
        x0 = self.x0 - self.pixelAbsolutValue[0]
        x1 = self.x1 - self.pixelAbsolutValue[0]
        y0 = self.y0 - self.pixelAbsolutValue[1]
        y1 = self.y1 - self.pixelAbsolutValue[1]
        return (x1 + x0) // 2, (y1 + y0) // 2

    def lineLen(self):
        return (self.x1 + self.x0) // 2 + (self.y1 + self.y0) // 2

    def lineLenMM(self):
        xmm0, ymm0 = self.calculateOffset(self.x0, self.y0)
        xmm1, ymm1 = self.calculateOffset(self.x1, self.y1)

        return round(pow(abs(xmm1 - xmm0) + abs(ymm1 - ymm0), 1 / 2), 2)

    def inROI(self, pos, x, y):
        dx, dy = self.calculateOffset(x, y)
        px, py = pos.x() + dx, pos.y() + dy
        return self.inROIext(px, py)

    def inROIext(self, px, py):
        threshold = 100

        p = array([px, py])
        a = array([self.x0, self.y0])
        b = array([self.x1, self.y1])

        # Vector from a to b
        ab = b - a
        ap = p - a

        # Project point onto the line
        ab_norm = dot(ab, ab)  # Squared length of ab
        if ab_norm == 0:
            return linalg.norm(ap) < threshold  # a and b are the same point

        t = dot(ap, ab) / ab_norm  # Projection factor

        # Clamp t to the segment [0,1]
        t = max(0, min(1, t))

        # Find the closest point on the segment
        closest = a + t * ab

        # Compute distance from the point to the closest point
        distance = linalg.norm(p - closest)

        return distance < threshold
