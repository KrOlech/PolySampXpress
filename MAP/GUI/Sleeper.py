from time import sleep

from PyQt5.QtCore import QObject, pyqtSignal


class sleeper(QObject):
    finished = pyqtSignal()

    def __init__(self, master, time, fun, *args, **kwargs):
        super(sleeper, self).__init__(*args, **kwargs)
        self.master = master
        self.time = time
        self.fun = fun

    def run(self):
        sleep(self.time)
        if self.fun is not None:
            self.fun()
        else:
            self.master.takphoto()
        self.finished.emit()
