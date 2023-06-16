from src.Zoom.FrontEnd.ZoomLabel import ZoomLabel
from src.Zoom.FrontEnd.ZoomSlider import ZoomSlider
from src.Zoom.Interface.DialogWindow import ZoomChangeDialogWindow


class ZoomInterface:
    zoomChange = False

    def __init__(self, master):
        self.master = master
        self.zoomManipulator = master.manipulatorInterferes

        self.zoomLabel = ZoomLabel(self.master, 0)

    def createZoomSlider(self):
        return ZoomSlider(self, widget=self.master, value=0)  # self.zoomManipulator.x)

    def zoomValueChange(self):
        ZoomChangeDialogWindow(self).exec_()

    def endZoomChange(self):
        self.zoomChange = False
