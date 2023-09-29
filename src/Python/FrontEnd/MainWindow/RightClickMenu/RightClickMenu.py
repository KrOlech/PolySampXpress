from PyQt5 import QtGui
from PyQt5.QtWidgets import QMenu


class RightMenu(QMenu):

    def __init__(self, master, *args, **kwargs):
        super(RightMenu, self).__init__(*args, **kwargs)

        self.master = master

        self.center = self.addAction("Center Hear")
        self.center.triggered.connect(self.master.center)

        if master.mainWindow.zoomInterface.zoomChange:
            self.endZoom = self.addAction("End Zoom Change")
            self.endZoom.triggered.connect(self.master.mainWindow.zoomInterface.endZoomChange)

    def addRoiMenus(self, rois, editTrybe):
        menus = []
        if editTrybe:
            self.center = self.addAction("end edit")
            self.center.triggered.connect(self.master.endEdit)

        for roi in rois:
            menu = self.addMenu(str(roi.name))
            menus.append(menu)
            edit = menu.addAction("Edit ROI")
            rename = menu.addAction("Rename")
            centerOn = menu.addAction("Center On")
            delete = menu.addAction("delete ROI")
            edit.triggered.connect(roi.edit)
            delete.triggered.connect(roi.delete)
            centerOn.triggered.connect(roi.centerOnMe)
            rename.triggered.connect(roi.rename)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.master.hideRightClickButtons()
        super(RightMenu, self).closeEvent(a0)
