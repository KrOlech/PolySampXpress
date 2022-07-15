
from PyQt5.QtWidgets import QMainWindow, QApplication

from PyQt5 import QtGui
import sys

class MainWindow(QMainWindow):

   def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
      print(self.size())

if __name__ == '__main__':


   app = QApplication(sys.argv)

   window = MainWindow()

   window.show()

   app.exec_()

