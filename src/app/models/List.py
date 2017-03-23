import tkinter as tk
from ...lib.Observable import Observable
from ..controllers.Container import Controller as Container

class Model:
    def __init__(self, name):
        self.containers = {}
        self.name = Observable(name)

    def setName(self, name):
        self.name.set(name)

    def addContainer(self, tree, name):
        self.containers[name] = Observable(Container(tree, name))

    def renameContainer(self, prevName, name):
        self.containers[name] = self.containers[prevName]
        del self.containers[prevName]

        self.containers[name].set(Container(name))

    def removeContainer(self, name):
        del self.containers[name]
