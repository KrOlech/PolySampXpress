from abc import ABCMeta, abstractmethod

from PyQt5.QtWidgets import QLabel

from ROI.Main.ROI import ROI


class CreateRoiAbstract(QLabel):
    __metaclass__ = ABCMeta

    roiNames = 0

    @abstractmethod
    def eventFilter(self, source, event):
        return super().eventFilter(source, event)

    @abstractmethod
    def mousePressEvent(self, e):
        pass

    @abstractmethod
    def mouseReleaseEvent(self, e):
        pass

    @abstractmethod
    def mouseMoveEvent(self, e):
        pass

    def savePressLocation(self, e):
        self.x1 = e.x()
        self.y1 = e.y()
        self.x2 = e.x()
        self.y2 = e.y()
        self.pressed = True

    @abstractmethod
    def saveTemporaryLocation(self, e):
        self.x2 = e.x()
        self.y2 = e.y()


    def seveReliseLocation(self, e):
        if self.pressed:
            self.x2 = e.x()
            self.y2 = e.y()

            self.ROIList.append(
                ROI(self, self.x1, self.y1, self.x2, self.y2, self.roiNames + 1, self.mainWindow.manipulator.x,
                    self.mainWindow.manipulator.y))
            self.roiNames += 1

            self.pressed = False

            self.mainWindow.addROIToList()