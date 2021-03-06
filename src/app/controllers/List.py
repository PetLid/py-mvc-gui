import tkinter as tk

from ..models.List import Model
from ..views.List import View

class Controller:
    def __init__(self, root, title="Unnamed"):
        self.model = Model(title)
        self.model.name.addCallback(self.SetTitle)
        self.view = View(root, title)
    #    self.MoneyChanged(self.model.myMoney.get())

    # def AddMoney(self):
    #     self.model.addMoney(10)
    #
    # def RemoveMoney(self):
    #     self.model.removeMoney(10)
    #
    def SetTitle(self, title):
        self.view.setTitle(title)

    def AddContainer(self, name):
        self.model.addContainer(self.view.tree, name)
        #self.model.containers[name].addCallback()
        self.view.AddContainer(name)


#    def ContainerChanged(self, name):
#        self.view.addContainer(name)


# if __name__ == '__main__':
#     root = tk.Tk()
#     root.withdraw()
#     app = Controller(root)
#     root.mainloop()
