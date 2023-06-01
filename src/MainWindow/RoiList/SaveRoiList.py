from PyQt5.QtWidgets import QFileDialog

from src.BaseClass.JsonRead.JsonRead import JsonHandling
from datetime import datetime
from os import mkdir, chdir, curdir


class SaveRoiList(JsonHandling):

    def __init__(self, master, roiList):
        self.master = master
        self.roiList = roiList

    def save(self):
        curentDirectory = curdir
        data = {roi.name: roi.fileDict for roi in self.roiList}
        folderPath, _ = QFileDialog.getSaveFileName(self.master, "Select Location to save Roi List", "",
                                                    "Json Files (*.json)")
        self.loger(folderPath)

        if folderPath:

            fileName = folderPath[folderPath.rfind(r"/") + 1:]

            folderPath = folderPath[:folderPath.rfind(r"/")]

            chdir(folderPath)

            now = datetime.now()

            directoryName = f"{str(now.date())}-{str(now.hour)}.{str(now.minute)}.{str(now.second)}"

            mkdir(directoryName)

            self.simpleSaveFile(folderPath + r"/" + directoryName + r"/" + fileName, data)

            [roi.saveViue(folderPath + r"/" + directoryName + r"/") for roi in self.roiList]

            chdir(curentDirectory)
