from abc import ABCMeta, abstractmethod

from src.Python.BaseClass.JsonRead.JsonRead import JsonHandling
from src.Python.BaseClass.Logger.Logger import Loger


class DataBaseReader(Loger, dict):
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def dataBaseFileName(self):
        return ""

    def __init__(self):
        super().__init__()
        for key, value in self.readDataBase().items():
            self[key] = value

    def saveDataBase(self):
        JsonHandling.saveFile(self.dataBaseFileName, self)

    def readDataBase(self):
        return JsonHandling.readFile(self.dataBaseFileName)
