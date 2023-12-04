import json
from abc import ABCMeta
from os.path import abspath

from src.Python.BaseClass.Logger.Logger import Loger


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

        border = data["0"]["borders"]

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
    def getFileLocation(file) -> str:  # todo Corection for compilation
        config = r"\Config"
        fullPath = abspath(__file__)
        fullPath = fullPath[:fullPath.rfind('src')]
        return fullPath + config + "\\" + file

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
        with open(filePath, 'w') as file:
            json.dump(dictionary, file, indent=4)

    @staticmethod
    def readManipulatorPosition():
        manipulatorConfig = JsonHandling.readFile("ManipulatorFullConfig.json")
        positions = manipulatorConfig["0"]["CurrentPosition"]
        return positions["x"], positions["y"]

    @staticmethod
    def saveManipulatorPosition(positions: dict):
        manipulatorConfig = JsonHandling.readFile("ManipulatorFullConfig.json")
        manipulatorConfig["0"]["CurrentPosition"] = positions
        JsonHandling.saveFile("ManipulatorFullConfig.json", manipulatorConfig)

    @staticmethod
    def loadResolution(resolution):
        with open(JsonHandling.getFileLocation(r"Resolutions.json"), 'r') as file:
            data = json.load(file)[resolution]

        return int(data["xResolution"]), int(data["yResolution"]), int(data["FPS"])

    @staticmethod
    def loadOffsetsJson():
        with open(JsonHandling.getFileLocation("ManipulatorFullConfig.json"), 'r') as file:
            data = json.load(file)
        return float(data["0"]["offsets"]["x"]), float(data["0"]["offsets"]["y"])

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


if __name__ == '__main__':
    print(JsonHandling.getFileLocation("test"))
