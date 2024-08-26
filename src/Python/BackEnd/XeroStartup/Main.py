from Python.BackEnd.Calibration.LocateCrossAutomatic_3_0.main import LocateCross
from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from Python.BaseClass.Logger.Logger import Loger


class XeroStartup(Loger):

    def __init__(self, master):
        self.master = master

        self.treyConfig = JsonHandling.loadTreyConfigurations()[self.master.sampleTreyName]
        self.treyConfigZoom = float(JsonHandling.loadTreyConfigurations()["zoom"][self.master.zoom])

    def xeroOut(self):
        for name, point in self.treyConfig.items():
            self.master.manipulatorInterferes.goToCords(float(point["x"]), float(point["y"]))

            self.master.manipulatorInterferes.autoFokus()
            z = self.master.manipulatorInterferes.focusPosition

            x, y = LocateCross(self.master,
                               f"Zoom_{self.master.zoom}_Trey_{self.master.sampleTreyName}_TreyNumer_{name}").locateCross()

            self.master.manipulatorInterferes.goToCords(x, y)

            self.master.manipulatorInterferes.goToCords(x + self.treyConfigZoom, y + self.treyConfigZoom)

            xC, yC = LocateCross(self.master,
                                 f"Zoom_{self.master.zoom}_Trey_{self.master.sampleTreyName}_TreyNumer_{name}_Calibration").locateCross()

            self.CalculateAndCheckCalibration([x, y], [xC, yC])

            self.master.refPoints[name] = {"x": x, "y": y, "z": z}

    def CalculateAndCheckCalibration(self, start, end):

        dx = start[0] - end[0]
        dy = start[1] - end[1]

        dx /= self.treyConfigZoom
        dy /= self.treyConfigZoom

        ofsetX, ofsetY = JsonHandling.loadOffsetsJson(self.master.zoom)

        differenceX = abs(dx - ofsetX)
        differenceY = abs(dx - ofsetY)

        if not (differenceX < 5 and differenceY < 5):
            # todo Rise proper Error
            self.logError("to mach difference in raf calibration check")
