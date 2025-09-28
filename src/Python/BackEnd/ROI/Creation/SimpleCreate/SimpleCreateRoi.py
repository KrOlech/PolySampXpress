from Python.BackEnd.ROI.Creation.Abstract.Abstract import CreateRoiAbstract


class SimpleCreateRoi(CreateRoiAbstract):

    def __savePressLocation(self, e):
        self.x1 = e.position().x()
        self.y1 = e.position().y()
        self.x2 = e.position().x()
        self.y2 = e.position().y()
        self.pressed = True

    def __seveReliseLocation(self, e):
        if self.pressed:
            self.x2 = e.position().x()
            self.y2 = e.position().y()

            self.createAndAddROIToList()

            self.pressed = False

    def __saveTemporaryLocation(self, e):
        self.x2 = e.position().x()
        self.y2 = e.position().y()

    def __toggleModeCleenUp(self):
        self.pressed = False
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
