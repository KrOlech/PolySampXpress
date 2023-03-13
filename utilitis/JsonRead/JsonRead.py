import json
from os import getcwd


class JsonHandling:

    @staticmethod
    def getFileLocation(file) -> str:
        mag = r"\Magisterkav2"
        lMag = len(mag)
        config = r"\Config"
        fullPath = getcwd()
        fullPath = fullPath[:fullPath.find(mag) + lMag]
        return fullPath + config + "\\" + file

    def readFile(self, filePath) -> dict:
        with open(self.getFileLocation(filePath), 'r') as file:
            rowData = json.load(file)

        return rowData

    def saveFile(self, filePath, dictionary) -> dict:
        with open(self.getFileLocation(filePath), 'w') as file:
            json.dump(dictionary, file, indent=4)


def getFileLocation(file) -> str:
    mag = r"\Magisterkav2"
    lMag = len(mag)
    config = r"\Config"
    fullPath = getcwd()
    fullPath = fullPath[:fullPath.find(mag) + lMag]
    return fullPath + config + "\\" + file


def loadOffsetsJson():
    with open(getFileLocation("ManipulatorConfig.json"), 'r') as file:
        data = json.load(file)
    return float(data["xOffset"]), float(data["yOffset"])


def loadPolaRoboczeJson():
    jsonKeys = ["Xmin", "Xmax", "Ymin", "Ymax"]

    with open(getFileLocation("PolaRoboczeConfig.json"), 'r') as file:
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


def loadCameraResolutionJson():
    with open(getFileLocation(r"CameraConfig.json"), 'r') as file:
        resolution = json.load(file)["ScaledResolution"]
    x, y, fps = loadResolution(resolution)
    return x, y


def loadNativeCameraResolutionJson():
    with open(getFileLocation(r"CameraConfig.json"), 'r') as file:
        resolution = json.load(file)["NativeResolution"]

    return loadResolution(resolution)


def loadResolution(resolution):
    with open(getFileLocation(r"Resolutions.json"), 'r') as file:
        data = json.load(file)[resolution]

    return int(data["xResolution"]), int(data["yResolution"]), int(data["FPS"])


if __name__ == '__main__':
    print(getFileLocation("test"))
