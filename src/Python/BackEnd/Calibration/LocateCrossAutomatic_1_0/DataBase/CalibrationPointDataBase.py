from src.Python.BackEnd.Calibration.LocateCrossAutomatic_1_0.DataBase.DataBaseReader import DataBaseReader


class CalibrationPointDataBase(DataBaseReader):

    @property
    def dataBaseFileName(self):
        return "CalibrationPointDataBase.json"

    def getCrossSize(self, key):
        return self[str(key)]["Size"]

    def getCrossWidthInPx(self, key):
        return self[str(key)]["pxWidth"]
