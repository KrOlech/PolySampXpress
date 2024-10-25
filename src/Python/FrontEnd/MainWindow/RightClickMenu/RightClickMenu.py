from PyQt5 import QtGui
from PyQt5.QtWidgets import QMenu


class RightMenu(QMenu):

    def __init__(self, master, *args, **kwargs):
        super(RightMenu, self).__init__(*args, **kwargs)

        self.master = master

        self.center = self.addAction("Center Here")
        self.center.triggered.connect(self.master.center)

        self.SaveFream = self.addAction("Save Current Frame")
        self.SaveFream.triggered.connect(self.master.mainWindow.saveCurrentFrame)

        # toDo Depraceted
        if master.mainWindow.zoomInterface.zoomChange and False:
            self.endZoom = self.addAction("End Zoom Change")
            self.endZoom.triggered.connect(self.master.mainWindow.zoomInterface.endZoomChange)

    def addRoiMenus(self, rois, editTrybe):

        if editTrybe:
            self.center = self.addAction("end edit")
            self.center.triggered.connect(self.master.endEdit)

        if len(rois) == 1:
            self.createSingleRoiMenu(rois[0])
        elif len(rois):
            self.createRoiMenus(rois)

    def createRoiMenus(self, rois):

        names = ["Edit ROI", "Rename", "Center On", "Delete ROI", "Edit Scatter"]

        functions = ["edit", "rename", "centerOnMe", "delete", "editScatter"]

        for name, fun in zip(names, functions):
            menu = self.addMenu(str(name))

            for roi in rois:
                action = menu.addAction(str(roi.name))
                action.triggered.connect(roi.__getattribute__(fun))

    def createSingleRoiMenu(self, roi):

        names = ["Edit ROI", "Rename", "Center On", "Delete ROI", "Edit Scatter"]

        functions = ["edit", "rename", "centerOnMe", "delete", "editScatter"]

        for name, fun in zip(names, functions):
            action = self.addAction(name + ' ' + str(roi.name))
            action.triggered.connect(roi.__getattribute__(fun))

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.master.hideRightClickButtons()
        super(RightMenu, self).closeEvent(a0)
