from Python.BackEnd.ROI.Main.Abstract.AbstractPoint import AbstractPoint
from Python.BackEnd.ROI.Main.Cursor.Cursor import Cursor
from Python.BackEnd.ROI.Main.Edit.Abstract import AbstractEdit


class PointEdit(AbstractPoint, AbstractEdit, Cursor):
    px, py = 0, 0

    def __move(self):
        self.x0 = self.px
        self.y0 = self.py

    def mouseMove(self, event, xManipulatorPosition, yManipulatorPosition):
        if self.firstPress:
            odx, ody = self.calculateOffset(xManipulatorPosition, yManipulatorPosition)
            self.rpx, self.rpy = int(event.position().x()), int(event.position().y())
            self.px, self.py = self.rpx + odx, self.rpy + ody
            if self.move:
                self.__move()

        super(PointEdit, self).mouseMove(event, xManipulatorPosition, yManipulatorPosition)

    def mousePositionCheck(self, event, xManipulatorPosition, yManipulatorPosition):
        self.move = False

        dx, dy = self.calculateOffset(xManipulatorPosition, yManipulatorPosition)

        self.px, self.py = int(event.position().x()) + dx, int(event.position().y()) + dy

        self.move = self.isCenter()

    def isCenter(self):
        return self.py + self.pressPrecision > self.y0 > self.py - self.pressPrecision and \
            self.px + self.pressPrecision > self.x0 > self.px - self.pressPrecision
