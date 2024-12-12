from Python.FrontEnd.MainWindow.RoiList.LoadRoiList import LoadRoiList
from Python.FrontEnd.MainWindow.RoiList.SaveRoiList import SaveRoiList
from Python.FrontEnd.MainWindow.ManipulatorInterfejs.MainWindowManipulatorInterfejs import \
    MainWindowManipulatorInterfejs
from Python.BackEnd.ROI.List.ROIList import ROIList
from functools import cache


class MainWindowROIList(MainWindowManipulatorInterfejs):

    def __init__(self, *args, **kwargs):
        super(MainWindowROIList, self).__init__(*args, **kwargs)

        self.roiList = ROIList(self, self.widget)
        self.roiList.move(self.roiListWidthFilld - 80, 0)  # toDo proper Load from file not Hard coded
        self.roiList.show()

    @property
    @cache
    def roiListWidthFilld(self):
        return self.windowSize.width() - self.roiList.width

    def showROIListButton(self, e):
        pass  # toDo extra window with info on ROIs

    def addROIToList(self, roi):
        self.cameraView.ROIList.append(roi)
        self.cameraView.roiNames += 1
        self.roiList.addROI(roi.label)

    def removeROIFromList(self, lable):
        self.roiList.removeROI(lable)

    def saveListOfROI(self):
        SaveRoiList(self, self.cameraView.ROIList).save()

    def emergancysaveListOfROI(self):
        SaveRoiList(self, self.cameraView.ROIList).emergancySave()

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
