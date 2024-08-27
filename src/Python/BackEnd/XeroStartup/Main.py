from Python.BackEnd.Calibration.LocateCrossAutomatic_3_0.main import LocateCross
from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from Python.BaseClass.Logger.Logger import Loger


class XeroStartup(Loger):

    def __init__(self, master):
        self.master = master

        self.treyConfig = JsonHandling.loadTreyConfigurations()[self.master.sampleTreyName]
        self.treyConfigZoom = float(JsonHandling.loadTreyConfigurations()["zoom"][str(int(self.master.zoom))])

    def xeroOut(self):
        for name, point in self.treyConfig.items():
            fileName = f"Zoom_{self.master.zoom}_Trey_{self.master.sampleTreyName}_TreyNumer_{name}"

            self.master.manipulatorInterferes.goToCords(float(point["y"]), float(point["x"]))
            self.master.manipulatorInterferes.waitForTarget()

            self.master.manipulatorInterferes.autoFokusNotAsync()
            z = self.master.manipulatorInterferes.focusPosition

            x, y = LocateCross(self.master, fileName).locateCross()

            self.master.manipulatorInterferes.center(y, x, self.master.zoom)
            self.loger(f"calibration_Start location {x} {y}")
            self.master.manipulatorInterferes.waitForTarget()

            x0, y0 = LocateCross(self.master, fileName + "calibration_Start").locateCross()

            self.master.manipulatorInterferes.setSpeed(self.treyConfigZoom)
            self.master.manipulatorInterferes.moveUp()
            self.master.manipulatorInterferes.moveLeft()
            self.master.manipulatorInterferes.waitForTarget()

            xC, yC = LocateCross(self.master, fileName + "calibration_End").locateCross()

            self.CalculateAndCheckCalibration([x0, y0], [xC, yC])

            self.master.refPoints[name] = {"x": x, "y": y, "z": z}

    def CalculateAndCheckCalibration(self, start, end):

        self.loger(f"Start point {start} , end point {end} ")

        dx = start[0] - end[0]
        dy = start[1] - end[1]

        dx /= self.treyConfigZoom
        dy /= self.treyConfigZoom

        ofsetX, ofsetY = JsonHandling.loadOffsetsJson(self.master.zoom)

        differenceX = abs(dx - ofsetX)
        differenceY = abs(dx - ofsetY)

        self.loger(f"raf dx difference: dx:{dx} , dy:{dy}, readed from file difrence ox:{ofsetX} , oy:{ofsetY}")

        if not (differenceX < 5 and differenceY < 5):
            # todo Rise proper Error
            self.logError("to mach difference in raf calibration check")
