import json
from os import getcwd


def getFileLocation(file) -> str:
    mag = r"\Magisterka"
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
        Resolution = json.load(file)["ScaledResolution"]

    with open(getFileLocation(r"Resolutions.json"), 'r') as file:
        data = json.load(file)[Resolution]

    return int(data["xResolution"]), int(data["yResolution"])


def loadNativeCameraResolutionJson():
    with open(getFileLocation(r"CameraConfig.json"), 'r') as file:
        Resolution = json.load(file)["NativeResolution"]

    with open(getFileLocation(r"Resolutions.json"), 'r') as file:
        data = json.load(file)[Resolution]

    return int(data["xResolution"]), int(data["yResolution"]), int(data["FPS"])


if __name__ == '__main__':
    print(getFileLocation("test"))
