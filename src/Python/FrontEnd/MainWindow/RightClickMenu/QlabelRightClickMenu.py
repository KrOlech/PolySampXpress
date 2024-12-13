from PyQt5.QtCore import QThread

from Python.FrontEnd.MainWindow.RightClickMenu.QlabelROI import QlabelROI
from Python.FrontEnd.MainWindow.RightClickMenu.Worker import WorkerQObject


class QlabelRightClickMenu(QlabelROI):

    def right_menu(self, pos):
        self.mainWindow.rightMenu(pos)

        super(QlabelRightClickMenu, self).right_menu(pos)

    def hideRightClickButtons(self):
        self.thread = QThread()
        self.worker = WorkerQObject(self.mainWindow)

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()
