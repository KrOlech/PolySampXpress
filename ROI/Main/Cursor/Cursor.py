from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from abc import abstractmethod, ABCMeta

from ROI.Main.ComonNames.CommonNames import CommonNames
from utilitis.Abstract import abstractmetod


class Cursor(CommonNames):
    __metaclass__ = ABCMeta

    def cursorEdit(self, e, x, y):
        self.mousePositionCheck(e, x, y)
        if self.move:
            QApplication.setOverrideCursor(Qt.SizeAllCursor)
        elif self.rightTop or self.leftBottom:
            QApplication.setOverrideCursor(Qt.SizeFDiagCursor)
        elif self.leftTop or self.rightBottom:
            QApplication.setOverrideCursor(Qt.SizeBDiagCursor)
        elif self.left or self.right:
            QApplication.setOverrideCursor(Qt.SizeHorCursor)
        elif self.top or self.bottom:
            QApplication.setOverrideCursor(Qt.SizeVerCursor)
        else:
            QApplication.setOverrideCursor(Qt.ArrowCursor)
