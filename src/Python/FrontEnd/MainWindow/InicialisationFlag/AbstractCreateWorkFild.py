class AbstractCreateWorkFild:

    def createWorkFild(self, field):
        nrWorkFields = len(self.master.workFildActions)

        name = f"X:{field[0]}_{field[1]}; Y:{field[2]}_{field[3]}"

        action = self.master.qActionCreate(name, lambda checked, nr=nrWorkFields: self.master.togle(nr), checkable=True)

        self.master.workFildMenu.addAction(action)
        self.master.workFildActions.append(action)
        self.master.readWorkFieldWindow.workFields.append(field)

        self.master.togle(nrWorkFields)
