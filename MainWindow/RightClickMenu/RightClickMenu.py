from PyQt5 import QtGui
from PyQt5.QtWidgets import QMenu


class RightMenu(QMenu):

    def __init__(self, mainWindow, *args, **kwargs):
        super(RightMenu, self).__init__(*args, **kwargs)

        self.mainWindow = mainWindow

        self.center = self.addAction("Center Hear")
        self.center.triggered.connect(self.mainWindow.center)

    def addRoiMenus(self, rois, editTrybe):
        menus = []
        if editTrybe:
            self.center = self.addAction("end edit")
            self.center.triggered.connect(self.mainWindow.endEdit)

        for roi in rois:
            menu = self.addMenu(str(roi.name))
            menus.append(menu)
            edit = menu.addAction("Edit ROI")
            rename = menu.addAction("Rename")
            delete = menu.addAction("delete ROI")
            edit.triggered.connect(roi.edit)
            delete.triggered.connect(roi.delete)
            rename.triggered.connect(roi.rename)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.mainWindow.hideRightClickButtons()
        super(RightMenu, self).closeEvent(a0)



