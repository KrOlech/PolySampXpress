from Python.BackEnd.ROI.Main.Abstract.AbstractPoint import AbstractPoint
from Python.BackEnd.ROI.Main.Edit.Abstract import AbstractEdit


class PointEdit(AbstractPoint, AbstractEdit):
    px, py = 0, 0

    def __init__(self, *args, **kwargs):
        super(PointEdit, self).__init__(*args, **kwargs)

    def delete(self):
        super(PointEdit, self).delete()

    def __move(self):
        self.x0 = self.px
        self.y0 = self.py


    def mouseMove(self, event, xManipulatorPosition, yManipulatorPosition):
        if self.firstPress:
            odx, ody = self.calculateOffset(xManipulatorPosition, yManipulatorPosition)
            self.px, self.py = event.x() + odx, event.y() + ody
            if self.move:
                self.__move()

        super(PointEdit, self).mouseMove(event, xManipulatorPosition, yManipulatorPosition)

    def mousePositionCheck(self, event, xManipulatorPosition, yManipulatorPosition):
        self.move = False

        dx, dy = self.calculateOffset(xManipulatorPosition, yManipulatorPosition)

        self.px, self.py = event.x() + dx, event.y() + dy

        self.move = self.isCenter()

    def isCenter(self):
        return self.py + self.pressPrecision > self.y0 > self.py - self.pressPrecision and \
               self.px + self.pressPrecision > self.x0 > self.px - self.pressPrecision
