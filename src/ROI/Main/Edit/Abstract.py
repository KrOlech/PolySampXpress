from abc import ABCMeta, abstractmethod

from src.utilitis.Abstract import abstractmetod


class AbstractEdit:
    __metaclass__ = ABCMeta

    def updateViue(self):
        self.label.update()

    def delete(self):
        self.master.endEdit()

    def edit(self):
        self.master.editTribe = True
        self.master.editedROI = self

    def mousePress(self, e, x, y):
        self.firstPress = True
        self.mousePositionCheck(e, x, y)
        self.rect = self.createMarker()
        self.updateViue()

    @abstractmethod
    def mousePositionCheck(self, event, xManipulatorPosition, yManipulatorPosition):
        abstractmetod(self)

    @abstractmethod
    def createMarker(self):
        abstractmetod(self)

    @abstractmethod
    def mouseMove(self, event, xManipulatorPosition, yManipulatorPosition):
        self.rect = self.createMarker()
        self.updateViue()

    def mouseRelease(self, e, x, y):
        self.firstPress = False
        dx, dy = self.calculateOffset(x, y)
        self.px1, self.py1 = e.x() + dx, e.y() + dy
        self.rect = self.createMarker()
        self.master.leftMouseButton = False
        self.updateViue()

    def isCenter(self):
        return self.y0 + self.pressPrecision < self.py0 < \
               self.y1 - self.pressPrecision and \
               self.x0 + self.pressPrecision < self.px0 < \
               self.x1 - self.pressPrecision

    def isRight(self):
        return self.x0 - self.pressPrecision < self.px0 < \
               self.x0 + self.pressPrecision and \
               self.y0 - self.pressPrecision < self.py0 < \
               self.y1 + self.pressPrecision

    def isLeft(self):
        return self.x1 - self.pressPrecision < self.px0 < \
               self.x1 + self.pressPrecision and \
               self.y0 - self.pressPrecision < self.py0 < \
               self.y1 + self.pressPrecision

    def isTop(self):
        return self.y0 - self.pressPrecision < self.py0 < \
               self.y0 + self.pressPrecision and \
               self.x0 - self.pressPrecision < self.px0 < \
               self.x1 + self.pressPrecision

    def isBottom(self):
        return self.y1 - self.pressPrecision < self.py0 < \
               self.y1 + self.pressPrecision and \
               self.x0 - self.pressPrecision < self.px0 < \
               self.x1 + self.pressPrecision
