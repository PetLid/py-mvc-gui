import tkinter as tk
from ...lib.Observable import Observable

class Model:
    def __init__(self, name):
        self.containees = []
        self.name = Observable(name)

    # def addContainee(self, value):
    #     self.myMoney.set(self.myMoney.get() + value)
    #
    # def removeMoney(self, value):
    #     self.myMoney.set(self.myMoney.get() - value)
