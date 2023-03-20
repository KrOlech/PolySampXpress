from PyQt5.QtWidgets import QMainWindow, QAction

from utilitis.Logger.Logger import Loger


class MainWindowAbstract(QMainWindow, Loger):

    def qActionCreate(self, name: str, triggerFun, checkable=False) -> QAction:
        qAction = QAction(name, self)
        qAction.setCheckable(checkable)
        qAction.triggered.connect(triggerFun)
        return qAction
