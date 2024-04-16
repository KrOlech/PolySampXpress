class CalibrateProperty:

    @property
    def indexLegend(self):
        return {0: "x", 1: "y"}

    @property
    def configFile(self):
        return "ManipulatorFullConfig.json"

    @property
    def templateLocationX(self):
        return 990

    @property
    def templateLocationY(self):
        return 540

    @property
    def templateSize(self):
        return 100
