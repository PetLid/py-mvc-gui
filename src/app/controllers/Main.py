import tkinter as tk

from ..models.Main import Model
from ..views.Main import View
from ..views.ChangerWidget import ChangerWidget

class Controller:
    def __init__(self, root):
        self.model = Model()
        self.model.myMoney.addCallback(self.MoneyChanged)
        self.view1 = View(root)
        self.view2 = ChangerWidget(self.view1)
        self.view2.addButton.config(command=self.AddMoney)
        self.view2.removeButton.config(command=self.RemoveMoney)
        self.MoneyChanged(self.model.myMoney.get())

    def AddMoney(self):
        self.model.addMoney(10)

    def RemoveMoney(self):
        self.model.removeMoney(10)

    def MoneyChanged(self, money):
        self.view1.SetMoney(money)


# if __name__ == '__main__':
#     root = tk.Tk()
#     root.withdraw()
#     app = Controller(root)
#     root.mainloop()
