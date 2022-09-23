


from MainWindow.MainWindowManipulatorInterfejs.MainWindowRightClickMenu.RightClickMenu import MainWindow


class MAINWINDOW(MainWindow):
   pass


if __name__ == '__main__':
   import sys
   from PyQt5.QtWidgets import QApplication
   app = QApplication(sys.argv)

   window = MainWindow()

   window.show()

   app.exec_()
