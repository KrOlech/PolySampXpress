from src.MainWindow.RoiList.LoadRoiList import LoadRoiList
from src.MainWindow.RoiList.SaveRoiList import SaveRoiList
from src.MainWindow.ManipulatorInterfejs.MainWindowManipulatorInterfejs import MainWindowManipulatorInterfejs
from src.ROI.List.ROIList import ROIList
from functools import cache


class MainWindowROIList(MainWindowManipulatorInterfejs):

    def __init__(self, *args, **kwargs):
        super(MainWindowROIList, self).__init__(*args, **kwargs)

        self.roiList = ROIList(self, self.widget)
        self.roiList.hide()

    @property
    @cache
    def roiListWidthFilld(self):
        return self.windowSize.width() - self.roiList.width

    def showROIList(self, e):
        if e.x() > self.roiListWidthFilld:
            self.roiList.move(self.roiListWidthFilld, 0)
            self.roiList.show()
        else:
            self.roiList.hide()

    def showROIListButton(self, e):
        self.roiList.move(0, 0)
        self.roiList.show()

    def addROIToList(self):
        self.roiList.addROI(self.cameraView.ROIList[-1].label)

    def removeROIFromList(self, lable):
        self.roiList.removeROI(lable)

    def saveListOfROI(self):
        SaveRoiList(self, self.cameraView.ROIList).save()

    def loadListOfROI(self):
        LoadRoiList(self).load()

if __name__ == '__main__':
    import faulthandler
    from PyQt5.QtWidgets import QApplication
    import sys

    faulthandler.enable()

    app = QApplication(sys.argv)

    window = MainWindowROIList(app.desktop().availableGeometry().size())

    window.show()

    app.exec_()
