from Python.BackEnd.ROI.Main.Abstract.AbstractLine import AbstractLine
from Python.BackEnd.ROI.Main.Cursor.Cursor import Cursor
from Python.BackEnd.ROI.Main.Edit.Abstract import AbstractEdit


class LineEdit(AbstractLine, AbstractEdit, Cursor):
    __0Point = False
    __1Point = False

    px0, py0 = 0, 0
    px1, py1 = 0, 0

    def mousePositionCheck(self, event, xManipulatorPosition, yManipulatorPosition):
        self.__closerPoint(event.x(), event.y())

        dx, dy = self.calculateOffset(xManipulatorPosition, yManipulatorPosition)

        self.px0, self.py0 = event.x() + dx, event.y() + dy

        self.move = self.__isCenter()

    def mouseMove(self, event, xManipulatorPosition, yManipulatorPosition):
        if self.firstPress:
            odx, ody = self.calculateOffset(xManipulatorPosition, yManipulatorPosition)
            self.px1, self.py1 = event.x() + odx, event.y() + ody
            if self.move:
                self.__move()
                self.px0, self.py0 = event.x() + odx, event.y() + ody

        super(LineEdit, self).mouseMove(event, xManipulatorPosition, yManipulatorPosition)

    def mouseRelease(self, e, x, y):
        super(LineEdit, self).mouseRelease(e, x, y)

        if self.move:
            self.__move()

        self.move = False

    def __closerPoint(self, x, y):
        distanceTo0 = abs(x - self.x0) + abs(y - self.y0)
        distanceTo1 = abs(self.x1 - x) + abs(self.y1 - y)
        if distanceTo0 > 100 and distanceTo1 > 100:
            self.__0Point = False
            self.__1Point = False
        elif distanceTo0 < distanceTo1:
            self.__0Point = True
            self.__1Point = False
        else:
            self.__0Point = False
            self.__1Point = True

    def __isCenter(self):
        if self.__0Point:
            return self.py1 + self.pressPrecision > self.y0 > self.py1 - self.pressPrecision and \
                self.px1 + self.pressPrecision > self.x0 > self.px1 - self.pressPrecision

        elif self.__1Point:
            return self.py1 + self.pressPrecision > self.y1 > self.py1 - self.pressPrecision and \
                self.px1 + self.pressPrecision > self.x1 > self.px1 - self.pressPrecision

        else:
            return self.inROIext(self.px1, self.py1)

    def __move(self):
        if self.__0Point:
            self.x0 = self.px1
            self.y0 = self.py1

        elif self.__1Point:
            self.x1 = self.px1
            self.y1 = self.py1

        else:
            dx, dy = self.px1 - self.px0, self.py1 - self.py0
            self.x0 += dx
            self.x1 += dx
            self.y0 += dy
            self.y1 += dy
