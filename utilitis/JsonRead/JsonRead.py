import json



def loadOffsetsJson():
    with open(r"C:\Users\user\KrzysztofOlech\Magisterka\Config\ManipulatorConfig.json",'r') as file:
        data = json.load(file)
    return data["xOffset"],data["yOffset"]


if __name__ == '__main__':

    print(loadOffsetsJson())