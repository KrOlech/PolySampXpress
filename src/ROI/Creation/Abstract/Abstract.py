from abc import ABCMeta, abstractmethod

from PyQt5.QtWidgets import QLabel

from src.ROI.Main.ROI.ROI import ROI
from src.BaseClass.Abstract import abstractmetod
from src.BaseClass.Logger.Logger import Loger


class CreateRoiAbstract(QLabel, Loger):
    __metaclass__ = ABCMeta

    roiNames = 0

    @abstractmethod
    def eventFilter(self, source, event):
        return super().eventFilter(source, event)

    @abstractmethod
    def mousePressEvent(self, e):
        abstractmetod(self)

    @abstractmethod
    def mouseReleaseEvent(self, e):
        abstractmetod(self)

    @abstractmethod
    def mouseMoveEvent(self, e):
        abstractmetod(self)

    @abstractmethod
    def savePressLocation(self, e):
        abstractmetod(self)

    @abstractmethod
    def seveReliseLocation(self, e):
        abstractmetod(self)

    def createAndAddROIToList(self, scatter=False):
        if abs(self.x1 - self.x2) < 10 and abs(self.y1 - self.y2) < 10:
            return

        self.ROIList.append(
            ROI(self, self.x1, self.y1, self.x2, self.y2, self.roiNames + 1, self.mainWindow.manipulatorInterferes.x,
                self.mainWindow.manipulatorInterferes.y, self.pixelAbsolutValue, scatter=scatter))
        self.roiNames += 1

        self.mainWindow.addROIToList()
