from abc import ABCMeta, abstractmethod

from PyQt5.QtWidgets import QLabel

from Python.BackEnd.ROI.Main.Line.Line import Line
from Python.BackEnd.ROI.Main.Point.PointClass import Point
from Python.BackEnd.ROI.Main.ROI.ROI import ROI
from Python.BaseClass.Logger.Logger import Loger


class CreateRoiAbstract(QLabel, Loger):
    __metaclass__ = ABCMeta

    roiNames = 0

    @abstractmethod
    def eventFilter(self, source, event):
        return super().eventFilter(source, event)

    @abstractmethod
    def mousePressEvent(self, e):
        self.abstractmetod()

    @abstractmethod
    def mouseReleaseEvent(self, e):
        self.abstractmetod()

    @abstractmethod
    def mouseMoveEvent(self, e):
        self.abstractmetod()

    @abstractmethod
    def savePressLocation(self, e):
        self.abstractmetod()

    @abstractmethod
    def seveReliseLocation(self, e):
        self.abstractmetod()

    def __checIfSizeIsValid(self) -> bool:
        return abs(self.x1 - self.x2) < 10 and abs(self.y1 - self.y2) < 10

    def createAndAddROIToList(self, scatter=False):

        if self.__checIfSizeIsValid():
            self.ROIList.append(
                Point(self, self.x2, self.y2, self.roiNames + 1, self.mainWindow.manipulatorInterferes.x,
                      self.mainWindow.manipulatorInterferes.y, self.pixelAbsolutValue))
        else:
            self.ROIList.append(
                ROI(self, self.x1, self.y1, self.x2, self.y2, self.roiNames + 1, self.mainWindow.manipulatorInterferes.x,
                    self.mainWindow.manipulatorInterferes.y, self.pixelAbsolutValue, scatter=scatter))

        self.roiNames += 1

        self.mainWindow.addROIToList()

    def createAndAddLineToList(self):
        self.ROIList.append(
            Line(self, self.x1, self.y1, self.x2, self.y2, self.roiNames + 1, self.mainWindow.manipulatorInterferes.x,
                self.mainWindow.manipulatorInterferes.y, self.pixelAbsolutValue))
        self.roiNames += 1

        self.mainWindow.addROIToList()