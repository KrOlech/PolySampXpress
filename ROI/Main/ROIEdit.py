from ROI.Main.Borders import ROIBorders


class ROIEdit(ROIBorders):
    px0, py0 = 0, 0
    px1, py1 = 0, 0

    def __init__(self, *args, **kwargs):
        super(ROIEdit, self).__init__(*args, **kwargs)

    def updateViue(self):
        self.label.update()

    def delete(self):
        super(ROIEdit, self).delete()
        self.master.endEdit()

    def edit(self):
        self.master.editTribe = True
        self.master.editedROI = self

    def mousePress(self, e, x, y):
        self.firstPress = True
        self.mousePositionCheck(e, x, y)
        self.rect = self.createRectangle()
        self.updateViue()

    def __move(self):
        dx, dy = self.px1 - self.px0, self.py1 - self.py0
        self.x0 += dx
        self.x1 += dx
        self.y0 += dy
        self.y1 += dy

    def mouseRelease(self, e, x, y):

        self.firstPress = False

        dx, dy = self.calculateOffset(x, y)
        self.px1, self.py1 = e.x() + dx, e.y() + dy

        if self.move:
            self.__move()
        else:
            self.__edgeMove()

        self.rect = self.createRectangle()
        self.setNewBorders()
        self.master.leftMouseButton = False
        self.updateViue()

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

    def mouseMove(self, e, x, y):

        if self.firstPress:
            odx, ody = self.calculateOffset(x, y)
            self.px1, self.py1 = e.x() + odx, e.y() + ody

            if self.move:
                self.__move()
                self.px0, self.py0 = e.x() + odx, e.y() + ody
            else:
                self.__edgeMove()

        self.rect = self.createRectangle()
        self.updateViue()

    def mousePositionCheck(self, e, x, y):

        self.top = False
        self.bottom = False
        self.left = False
        self.right = False

        self.leftTop = False
        self.rightTop = False

        self.leftBottom = False
        self.rightBottom = False

        self.move = False

        dx, dy = self.calculateOffset(x, y)

        self.px0, self.py0 = e.x() + dx, e.y() + dy

        if self.x0 - self.pressPrecision < self.px0 < \
                self.x0 + self.pressPrecision and \
                self.y0 - self.pressPrecision < self.py0 < \
                self.y1 + self.pressPrecision:
            self.right = True

        if self.x1 - self.pressPrecision < self.px0 < \
                self.x1 + self.pressPrecision and \
                self.y0 - self.pressPrecision < self.py0 < \
                self.y1 + self.pressPrecision:
            self.left = True

        if self.y0 - self.pressPrecision < self.py0 < \
                self.y0 + self.pressPrecision and \
                self.x0 - self.pressPrecision < self.px0 < \
                self.x1 + self.pressPrecision:
            self.top = True

        if self.y1 - self.pressPrecision < self.py0 < \
                self.y1 + self.pressPrecision and \
                self.x0 - self.pressPrecision < self.px0 < \
                self.x1 + self.pressPrecision:
            self.bottom = True

        self.leftTop = self.left and self.top
        self.rightTop = self.right and self.top

        self.leftBottom = self.left and self.bottom
        self.rightBottom = self.right and self.bottom

        if self.y0 + self.pressPrecision < self.py0 < \
                self.y1 - self.pressPrecision and \
                self.x0 + self.pressPrecision < self.px0 < \
                self.x1 - self.pressPrecision:
            self.move = True
