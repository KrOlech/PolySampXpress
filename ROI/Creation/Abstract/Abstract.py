from abc import ABCMeta, abstractmethod

from PyQt5.QtWidgets import QLabel


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

    @abstractmethod
    def savePressLocation(self, e):
        pass

    @abstractmethod
    def seveReliseLocation(self, e):
        pass
