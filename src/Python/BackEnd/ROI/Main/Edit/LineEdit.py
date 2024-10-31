from Python.BackEnd.ROI.Main.Abstract.AbstractLine import AbstractLine
from Python.BackEnd.ROI.Main.Cursor.Cursor import Cursor
from Python.BackEnd.ROI.Main.Edit.Abstract import AbstractEdit


class LineEdit(AbstractLine, AbstractEdit, Cursor):
    __0Point = False
    __1Point = False
    __move = False

    px, py = 0, 0

    def mousePositionCheck(self, event, xManipulatorPosition, yManipulatorPosition):
        self.__closerPoint(event.x(), event.y())

        self.move = False

        dx, dy = self.calculateOffset(xManipulatorPosition, yManipulatorPosition)

        self.px, self.py = event.x() + dx, event.y() + dy

        self.move = self.__isCenter()

    def mouseMove(self, event, xManipulatorPosition, yManipulatorPosition):
        if self.firstPress:
            odx, ody = self.calculateOffset(xManipulatorPosition, yManipulatorPosition)
            self.px, self.py = event.x() + odx, event.y() + ody
            if self.move:
                self.__move()

        super(LineEdit, self).mouseMove(event, xManipulatorPosition, yManipulatorPosition)

    def __closerPoint(self, x, y):
        distanceTo0 = abs(x - self.x0) + abs(y - self.y0)
        distanceTo1 = abs(self.x1 - x) + abs(self.y1 - y)
        if distanceTo0 < distanceTo1:
            self.__0Point = True
            self.__1Point = False
        else:
            self.__0Point = False
            self.__1Point = True

    def __isCenter(self):
        if self.__0Point:
            return self.py + self.pressPrecision > self.y0 > self.py - self.pressPrecision and \
                self.px + self.pressPrecision > self.x0 > self.px - self.pressPrecision

        elif self.__1Point:
            return self.py + self.pressPrecision > self.y1 > self.py - self.pressPrecision and \
                self.px + self.pressPrecision > self.x1 > self.px - self.pressPrecision

    def __move(self):
        if self.__0Point:
            self.x0 = self.px
            self.y0 = self.py

        elif self.__1Point:
            self.x1 = self.px
            self.y1 = self.py
