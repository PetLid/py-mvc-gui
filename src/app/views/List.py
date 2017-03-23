import tkinter as tk
from tkinter import ttk

class View(tk.Toplevel):
    def __init__(self, master, title):

        self.title = tk.Label(master, text=title)
        self.title.pack()

        self.tree = ttk.Treeview(master)
        self.tree.pack(fill=tk.BOTH)

    def setTitle(self, title):
        self.title['text'] = title

    def AddContainer(self, name):
        print('test')
        #container = self.tree.insert('', 'end', text=name)
        #attribute = self.tree.insert(container, 'end', text=name)
        #self.tree.insert(attribute, 'end', text=name)
