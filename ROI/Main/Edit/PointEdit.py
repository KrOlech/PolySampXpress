from ROI.Main.Abstract.AbstractPoint import AbstractPoint
from ROI.Main.Edit.Abstract import AbstractEdit


class PointEdit(AbstractPoint, AbstractEdit):
    px, py = 0, 0

    def __init__(self, *args, **kwargs):
        super(PointEdit, self).__init__(*args, **kwargs)

    def delete(self):
        super(PointEdit, self).delete()

    def __move(self):
        self.x0 = self.px
        self.y0 = self.py


    def mouseMove(self, e, x, y):
        if self.firstPress:
            odx, ody = self.calculateOffset(x, y)
            self.px, self.py = e.x() + odx, e.y() + ody
            if self.move:
                self.__move()

        super(PointEdit, self).mouseMove(e, x, y)

    def mousePositionCheck(self, e, x, y):
        self.move = False

        dx, dy = self.calculateOffset(x, y)

        self.px, self.py = e.x() + dx, e.y() + dy

        self.move = self.isCenter()

    def isCenter(self):
        return self.py + self.pressPrecision > self.y0 > self.py - self.pressPrecision and \
               self.px + self.pressPrecision > self.x0 > self.px - self.pressPrecision
