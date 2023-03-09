from PyQt5.QtWidgets import QMainWindow, QAction


class MainWindowAbstract(QMainWindow):

    def qActionCreate(self, name: str, triggerFun, checkable=False) -> QAction:
        qAction = QAction(name, self)
        qAction.setCheckable(checkable)
        qAction.triggered.connect(triggerFun)
        return qAction
