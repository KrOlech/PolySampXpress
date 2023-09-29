from PyQt5.QtWidgets import QMainWindow, QAction

from src.Python.BaseClass.Logger.Logger import Loger


class MainWindowAbstract(QMainWindow, Loger):
    zoomInterface = None

    def qActionCreate(self, name: str, triggerFun, checkable=False) -> QAction:
        qAction = QAction(name, self)
        qAction.setCheckable(checkable)
        qAction.triggered.connect(triggerFun)
        return qAction
