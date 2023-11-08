import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QSlider
from PyQt5.QtCore import Qt

class FixedValueSlider(QSlider):
    def __init__(self):
        super().__init__(Qt.Horizontal)
        self.setRange(0, 100)
        self.setTickPosition(QSlider.TicksBelow)
        self.setTickInterval(5)
        self.valueChanged.connect(self.snap_to_steps)

    def snap_to_steps(self):
        value = self.value()
        snapped_value = round(value / 5) * 5
        self.setValue(snapped_value)

class SliderExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Slider with Fixed Values")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.slider = FixedValueSlider()
        self.slider.valueChanged.connect(self.slider_value_changed)

        self.label = QLabel("Value: 0", self)

        layout.addWidget(self.slider)
        layout.addWidget(self.label)

        central_widget.setLayout(layout)

    def slider_value_changed(self):
        value = self.slider.value()
        self.label.setText(f"Value: {value}")

def main():
    app = QApplication(sys.argv)
    window = SliderExample()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
