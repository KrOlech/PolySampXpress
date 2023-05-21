from src.BaseClass.Logger.Logger import Loger


class InvalidSpeed(Exception):
    def __init__(self):
        super().__init__("[WARNING] - Invalid speed")


class NoCammeraConected(Exception, Loger):
    def __init__(self):
        super().__init__("[WARNING] - No Camera Connected Switching to camera simulator")
        self.logError(
            "Error During camera initialisation check it connection or if any other software is using it.")


if __name__ == '__main__':
    try:
        raise InvalidSpeed()
    except InvalidSpeed as e:
        print(e)
