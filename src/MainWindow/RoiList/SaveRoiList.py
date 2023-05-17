from PyQt5.QtWidgets import QFileDialog

from src.BaseClass.JsonRead.JsonRead import JsonHandling


class SaveRoiList(JsonHandling):

    def __init__(self, master, roiList):
        self.master = master
        self.roiList = roiList

    def save(self):
        data = {roi.name: roi.__dict__() for roi in self.roiList}
        folderPath, _ = QFileDialog.getSaveFileName(self.master, "Select Location to save Roi List", "",
                                                    "Json Files (*.json)")
        self.loger(folderPath)
        self.simpleSaveFile(folderPath, data)
