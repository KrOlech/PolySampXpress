from PyQt5.QtWidgets import QMenu


class RoiRightMenu(QMenu):

    def __init__(self, master, *args, **kwargs):
        super(RoiRightMenu, self).__init__(*args, **kwargs)

        self.master = master

        edit = self.addAction("Edit ROI")
        centerOn = self.addAction("Center On")
        rename = self.addAction("Rename")
        delete = self.addAction("delete ROI")
        edit.triggered.connect(master.edit)
        centerOn.triggered.connect(master.centerOnMe)
        rename.triggered.connect(master.rename)
        delete.triggered.connect(master.delete)

