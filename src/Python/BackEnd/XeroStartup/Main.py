from Python.BackEnd.Calibration.LocateCrossAutomatic_3_0.main import LocateCross
from Python.BackEnd.ROI.Main.Point.PointClass import Point
from Python.BaseClass.JsonRead.JsonRead import JsonHandling
from Python.BaseClass.Logger.Logger import Loger


class XeroStartup(Loger):
    treyConfigZoom = None

    def __init__(self, master):
        self.master = master

        self.treyConfig = JsonHandling.loadTreyConfigurations()[self.master.sampleTreyName]

    def xeroOut(self):

        self.treyConfigZoom = float(JsonHandling.loadTreyConfigurations()["zoom"][str(int(self.master.zoom))])

        self.master.refPoints[self.treyConfigZoom] = {}

        for name, point in self.treyConfig.items():
            fileName = f"P00_Zoom_{self.master.zoom}_Trey_{self.master.sampleTreyName}_TreyNumer_{name}"

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

            p = Point(self.master.cameraView, x, y, f"{fileName}",
                      self.master.manipulatorInterferes.x,
                      self.master.manipulatorInterferes.y, [0, 0], ooPoint=False, zValue=z)

            self.master.cameraView.ROIList.append(p)

            self.master.addROIToList()

            self.master.refPoints[self.treyConfigZoom][name] = {"x": x, "y": y, "z": z, "point": p.fileDict}

            print(self.master.refPoints)

        self.master.zeroPoint[self.treyConfigZoom] = next(iter(self.master.refPoints[self.treyConfigZoom].values()))

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
