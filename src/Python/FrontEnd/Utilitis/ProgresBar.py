from PyQt5.QtWidgets import QProgressBar


class ProgresBar(QProgressBar):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setTextVisible(False)

        self.setStyleSheet("QProgressBar"
                          "{"
                          "border: solid grey;"
                          "border-radius: 15px;"
                          " color: black; "
                          "}"
                          "QProgressBar::chunk "
                          "{background-color: # 05B8CC;"
                          "border-radius :15px;"
                          "}")