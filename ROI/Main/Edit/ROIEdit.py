from ROI.Main.Abstract.AbstractROI import AbstractROI
from ROI.Main.Edit.Abstract import AbstractEdit


class ROIEdit(AbstractROI, AbstractEdit):
    px0, py0 = 0, 0
    px1, py1 = 0, 0

    def __init__(self, *args, **kwargs):
        super(ROIEdit, self).__init__(*args, **kwargs)

    def delete(self):
        super(ROIEdit, self).delete()

    def mouseRelease(self, e, x, y):
        super(ROIEdit, self).mouseRelease(e, x, y)

        if self.move:
            self.__move()
        else:
            self.__edgeMove()

    def mouseMove(self, e, x, y):

        if self.firstPress:
            odx, ody = self.calculateOffset(x, y)
            self.px1, self.py1 = e.x() + odx, e.y() + ody

            if self.move:
                self.__move()
                self.px0, self.py0 = e.x() + odx, e.y() + ody
            else:
                self.__edgeMove()

        super(ROIEdit, self).mouseMove(e, x, y)

    def __negateAll(self):
        self.top = False
        self.bottom = False
        self.left = False
        self.right = False

        self.leftTop = False
        self.rightTop = False

        self.leftBottom = False
        self.rightBottom = False

        self.move = False

    def mousePositionCheck(self, e, x, y):

        self.__negateAll()

        dx, dy = self.calculateOffset(x, y)

        self.px0, self.py0 = e.x() + dx, e.y() + dy

        self.move = self.isCenter()

        if self.move:
            return

        self.right = self.isRight

        self.left = self.isLeft()

        self.top = self.isTop()

        self.bottom = self.isBottom()

        self.leftTop = self.left and self.top
        self.rightTop = self.right and self.top

        self.leftBottom = self.left and self.bottom
        self.rightBottom = self.right and self.bottom



    def __edgeMove(self):
        if self.leftTop:
            self.x1 = self.px1
            self.y0 = self.py1
        elif self.leftBottom:
            self.x1 = self.px1
            self.y1 = self.py1
        elif self.rightBottom:
            self.x0 = self.px1
            self.y1 = self.py1
        elif self.rightTop:
            self.x0 = self.px1
            self.y0 = self.py1
        elif self.bottom:
            self.y1 = self.py1
        elif self.left:
            self.x1 = self.px1
        elif self.right:
            self.x0 = self.px1
        elif self.top:
            self.y0 = self.py1

    def __move(self):
        dx, dy = self.px1 - self.px0, self.py1 - self.py0
        self.x0 += dx
        self.x1 += dx
        self.y0 += dy
        self.y1 += dy
