import tkinter as tk
from tkinter import ttk

class View(tk.Toplevel):
    def __init__(self, master, name):

        master.insert('', 'end', text=name)

    # def AddAttribute(self, name):
    #     container = self.tree.insert('', 'end', text=name)
    #     attribute = self.tree.insert(container, 'end', text=name)
    #     self.tree.insert(attribute, 'end', text=name)
