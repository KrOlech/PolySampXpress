from src.utilitis.JsonRead.JsonRead import JsonHandling


def test_JsonRead():
    jsonHandler = JsonHandling()

    print(jsonHandler.getFileLocation("test"))

    jsonHandler.readFile(r"CameraConfig.json")
