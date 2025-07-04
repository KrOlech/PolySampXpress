from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QToolButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPalette, QIcon

from Python.BaseClass.JsonRead.JsonRead import JsonHandling


class MyBar(QWidget):
    clickPos = None

    def __init__(self, parent, name="PolySampXpress beta-0.7"):
        super(MyBar, self).__init__(parent)
        self.setAutoFillBackground(True)

        self.setBackgroundRole(QPalette.Shadow)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)
        layout.addStretch()

        self.title = QLabel(name, self)
        self.title.setMinimumWidth(180)
        self.title.setForegroundRole(QPalette.Light)

        style = self.style()
        ref_size = self.fontMetrics().height()
        ref_size += style.pixelMetric(style.PM_ButtonMargin) * 2
        self.setMaximumHeight(ref_size + 2)

        btn_size = QSize(ref_size, ref_size)
        for target in ('min', 'close'):
            btn = QToolButton(self, focusPolicy=Qt.NoFocus)
            layout.addWidget(btn)
            btn.setFixedSize(btn_size)

            iconType = getattr(style,
                               'SP_TitleBar{}Button'.format(target.capitalize()))
            btn.setIcon(style.standardIcon(iconType))

            if target == 'close':
                colorNormal = 'red'
                colorHover = 'orangered'
            else:
                colorNormal = 'palette(mid)'
                colorHover = 'palette(light)'
            btn.setStyleSheet('''
                QToolButton {{
                    background-color: {};
                }}
                QToolButton:hover {{
                    background-color: {}
                }}
            '''.format(colorNormal, colorHover))

            signal = getattr(self, target + 'Clicked')
            btn.clicked.connect(signal)

            setattr(self, target + 'Button', btn)

            self.setWindowIcon(QIcon(JsonHandling.getFileLocation("smallLogo.png")))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clickPos = event.windowPos().toPoint()

    def mouseMoveEvent(self, event):
        if self.clickPos is not None:
            self.window().move(event.globalPos() - self.clickPos)

    def mouseReleaseEvent(self, QMouseEvent):
        self.clickPos = None

    def closeClicked(self):
        self.window().close()

    def maxClicked(self):
        self.window().showMaximized()

    def normalClicked(self):
        self.window().showNormal()

    def minClicked(self):
        self.window().showMinimized()
