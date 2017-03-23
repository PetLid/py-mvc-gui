import tkinter as tk
from ...lib.Observable import Observable
#from ..controllers.Container import Controller

class Model:
    def __init__(self, name):
        self.containees = {}
        self.name = Observable(name)

    def addContainee(self, tree, value):
        self.containers[name] = Observable(Containee(tree, name))
    #
    # def removeMoney(self, value):
    #     self.myMoney.set(self.myMoney.get() - value)
