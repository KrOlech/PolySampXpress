import json


def loadOffsetsJson():
    with open(r"C:\Users\user\KrzysztofOlech\Magisterka\Config\ManipulatorConfig.json", 'r') as file:
        data = json.load(file)
    return float(data["xOffset"]), float(data["yOffset"])


def loadPolaRoboczeJson():
    jsonKeys = ["Xmin", "Xmax", "Ymin", "Ymax"]

    with open(r"C:\Users\user\KrzysztofOlech\Magisterka\Config\PolaRoboczeConfig.json", 'r') as file:
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


if __name__ == '__main__':
    print(loadOffsetsJson())
