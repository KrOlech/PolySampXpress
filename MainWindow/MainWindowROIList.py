from MainWindow.MainWindowManipulatorInterfejs.MainWindowManipulatorInterfejs import MainWindowManipulatorInterfejs
from ROI.ROIList import ROIList


class MainWindowROIList(MainWindowManipulatorInterfejs):

    def __init__(self, *args, **kwargs):
        super(MainWindowROIList, self).__init__(*args, **kwargs)

        self.roiList = ROIList(self, self.widget)
        self.roiList.hide()

    def showROIList(self, e):
        if e.x() > 2400:  # dopracowac wartosc
            self.roiList.show()
            self.roiList.move(2250, 0)  # dopracowac wartosc

        else:
            self.roiList.hide()

    def showROIListButton(self, e):
        self.roiList.move(0, 0)
        self.roiList.show()

    def addROIToList(self):
        self.roiList.addROI(self.cameraView.ROIList[-1].label)

    def removeROIFromList(self, lable):
        self.roiList.removeROI(lable)


if __name__ == '__main__':
    import faulthandler
    from PyQt5.QtWidgets import QApplication
    import sys

    faulthandler.enable()

    app = QApplication(sys.argv)

    window = MainWindowROIList(app.desktop().availableGeometry().size())

    window.show()

    app.exec_()
