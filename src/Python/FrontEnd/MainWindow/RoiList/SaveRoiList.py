import os

from PyQt5.QtWidgets import QFileDialog

from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from datetime import datetime
from os import mkdir, chdir, curdir
import zipfile
import json
import zipfile
import numpy as np
from PIL import Image
from io import BytesIO


class SaveRoiList(JsonHandling):

    def __init__(self, master, roiList):
        self.master = master
        self.roiList = roiList

    def save(self):
        currentDirectory = curdir
        data = {roi.name: roi.fileDict for roi in self.roiList}

        folderPath, _ = QFileDialog.getSaveFileName(self.master, "Select Location to save Roi List", "",
                                                    "Json Files (*.zip)")

        self.loger(f"folder path: {folderPath}")

        if folderPath:
            fileName = folderPath[folderPath.rfind(r"/") + 1:]

            chdir(folderPath[:folderPath.rfind(r"/")])

            with zipfile.ZipFile(f'{fileName}', 'w') as zipF:

                with zipF.open('data.json', 'w') as jsonfile:
                    jsonfile.write(json.dumps(data, indent=4).encode('utf-8'))

                for roi in self.roiList:
                    photoArray = roi.createViue()

                    name = str(roi.name) + ".png"

                    img = Image.fromarray(photoArray)

                    imgByte = BytesIO()
                    img.save(imgByte, format='PNG')  # Save as PNG or JPEG

                    # Write the image to the zip file
                    zipF.writestr(name, imgByte.getvalue())

            chdir(currentDirectory)

    def emergancySave(self):

        data = {roi.name: roi.fileDict for roi in self.roiList}

        now = datetime.now()

        fileName = f"{str(now.date())}-{str(now.hour)}.{str(now.minute)}.{str(now.second)}"

        with zipfile.ZipFile(f'{fileName}', 'w') as zipF:
            with zipF.open('data.json', 'w') as jsonfile:
                jsonfile.write(json.dumps(data, indent=4).encode('utf-8'))

            for roi in self.roiList:
                photoArray = roi.createViue()

                name = str(roi.name) + ".png"

                img = Image.fromarray(photoArray)

                imgByte = BytesIO()
                img.save(imgByte, format='PNG')  # Save as PNG or JPEG

                # Write the image to the zip file
                zipF.writestr(name, imgByte.getvalue())
