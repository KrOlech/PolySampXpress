import json
from abc import ABCMeta
from os.path import abspath
from sys import platform

from Python.BaseClass.Logger.Logger import Loger


class JsonHandling(Loger):
    __metaclass__ = ABCMeta

    manipulatorMainFile = "ManipulatorFullConfig.json"

    roiConfigFile = "RoiConfig.json"

    @staticmethod
    def readRoiConfig() -> dict:
        return JsonHandling.readFile(JsonHandling.roiConfigFile)

    @staticmethod
    def readROILabelConfig() -> dict:
        return JsonHandling.readRoiConfig()["Label"]

    @staticmethod
    def readRoiLabelScalles():
        scalles = JsonHandling.readROILabelConfig()["scalle"]
        return scalles["X"], scalles["Y"]

    @staticmethod
    def readManipulatorRange():
        data = JsonHandling.readFile(JsonHandling.manipulatorMainFile)

        border = data["borders"]

        return border["x"], border["y"]

    @staticmethod
    def readManipulatorMax():
        borderX, borderY = JsonHandling.readManipulatorRange()

        return borderX["max"], borderY["max"]

    @staticmethod
    def readManipulatorMin():
        borderX, borderY = JsonHandling.readManipulatorRange()

        return borderX["min"], borderY["min"]

    @staticmethod
    def getFileLocation(file) -> str:

        if platform == "linux" or platform == "linux2":
            expectedLocation = "Config/" + file
            return expectedLocation
        elif platform == "win32":
            expectedLocation = r"C:\Program Files\PollsampleX\Config"
            return expectedLocation + "\\" + file
        else:
            JsonHandling.logError("OS Type Error - [Unsaported OS]")
            return ""


    @staticmethod
    def readFile(filePath) -> dict:
        return JsonHandling.readFileRow(JsonHandling.getFileLocation(filePath))

    @staticmethod
    def readFileRow(filePath) -> dict:
        with open(filePath, 'r') as file:
            rowData = json.load(file)

        return rowData

    @staticmethod
    def saveFile(filePath, dictionary: dict):
        JsonHandling.simpleSaveFile(JsonHandling.getFileLocation(filePath), dictionary)

    @staticmethod
    def simpleSaveFile(filePath, dictionary: dict):
        try:
            with open(filePath, 'w') as file:
                json.dump(dictionary, file, indent=4)
        except PermissionError as error:
            Loger.log(error,"simpleSaveFile","ERROR" )

    @staticmethod
    def readManipulatorPosition():
        manipulatorConfig = JsonHandling.readFile("ManipulatorFullConfig.json")
        positions = manipulatorConfig["CurrentPosition"]
        return positions["x"], positions["y"]

    @staticmethod
    def saveManipulatorPosition(positions: dict):
        manipulatorConfig = JsonHandling.readFile("ManipulatorFullConfig.json")
        manipulatorConfig["CurrentPosition"] = positions
        JsonHandling.saveFile("ManipulatorFullConfig.json", manipulatorConfig)

    @staticmethod
    def loadResolution(resolution):
        with open(JsonHandling.getFileLocation(r"Resolutions.json"), 'r') as file:
            data = json.load(file)[resolution]

        return int(data["xResolution"]), int(data["yResolution"]), int(data["FPS"])

    @staticmethod
    def loadOffsetsJson(zoom=0.85):
        zoomS = str(int(zoom))
        with open(JsonHandling.getFileLocation("ManipulatorFullConfig.json"), 'r') as file:
            data = json.load(file)
        return float(data[zoomS]["offsets"]["x"]), float(data[zoomS]["offsets"]["y"])

    @staticmethod
    def loadZoomLocationJson():
        with open(JsonHandling.getFileLocation("ManipulatorFullConfig.json"), 'r') as file:
            data = json.load(file)
        return float(data["CurrentPosition"]["zoom"])

    @staticmethod
    def loadFokusLocationJson():
        with open(JsonHandling.getFileLocation("ManipulatorFullConfig.json"), 'r') as file:
            data = json.load(file)
        return float(data["CurrentPosition"]["fokus"])

    @staticmethod
    def saveZoomLocationJson(zoom):
        with open(JsonHandling.getFileLocation("ManipulatorFullConfig.json"), 'r') as file:
            data = json.load(file)
        data["CurrentPosition"]["zoom"] = zoom
        try:
            with open(JsonHandling.getFileLocation("ManipulatorFullConfig.json"), 'w') as file:
                json.dump(data, file, indent=4)
        except PermissionError as error:
            Loger.log(error,"saveZoomLocationJson","ERROR" )


    @staticmethod
    def saveFokusLocationJson(fokus):
        with open(JsonHandling.getFileLocation("ManipulatorFullConfig.json"), 'r') as file:
            data = json.load(file)
        data["CurrentPosition"]["fokus"] = fokus
        try:
            with open(JsonHandling.getFileLocation("ManipulatorFullConfig.json"), 'w') as file:
                json.dump(data, file, indent=4)
        except PermissionError as e:
            print(e)

    @staticmethod
    def loadPolaRoboczeJson():
        jsonKeys = ["Xmin", "Xmax", "Ymin", "Ymax"]

        with open(JsonHandling.getFileLocation("PolaRoboczeConfig.json"), 'r') as file:
            data = json.load(file)

        fild = []
        for key, pole in data.items():

            try:
                fild.append([float(pole[jKey]) for jKey in jsonKeys])
                fild[-1].append(key)
            except KeyError:
                print(f"In {key} their is missing value neasesery values keys are: {jsonKeys}")
                fild = []
                break
        return fild

    @staticmethod
    def loadCameraResolutionJson():
        with open(JsonHandling.getFileLocation(r"CameraConfig.json"), 'r') as file:
            resolution = json.load(file)["ScaledResolution"]
        x, y, fps = JsonHandling.loadResolution(resolution)
        return x, y

    @staticmethod
    def loadNativeCameraResolutionJson():
        with open(JsonHandling.getFileLocation(r"CameraConfig.json"), 'r') as file:
            resolution = json.load(file)["NativeResolution"]

        return JsonHandling.loadResolution(resolution)

    @staticmethod
    def loadTreyConfigurations():
        with open(JsonHandling.getFileLocation(r"TreyConfig.json"), 'r') as file:
            treys = json.load(file)

        return treys


if __name__ == '__main__':
    print(JsonHandling.getFileLocation("test"))
