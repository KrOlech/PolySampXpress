from abc import ABCMeta

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

from Python.BackEnd.ROI.Main.ComonNames.CommonNames import CommonNames


class Cursor(CommonNames):
    __metaclass__ = ABCMeta

    def cursorEdit(self, e, x, y):
        self.mousePositionCheck(e, x, y)
        if self.move:
            QApplication.setOverrideCursor(Qt.CursorShape.SizeAllCursor)
        elif self.rightTop or self.leftBottom:
            QApplication.setOverrideCursor(Qt.CursorShape.SizeFDiagCursor)
        elif self.leftTop or self.rightBottom:
            QApplication.setOverrideCursor(Qt.CursorShape.SizeBDiagCursor)
        elif self.left or self.right:
            QApplication.setOverrideCursor(Qt.CursorShape.SizeHorCursor)
        elif self.top or self.bottom:
            QApplication.setOverrideCursor(Qt.CursorShape.SizeVerCursor)
        else:
            QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)
