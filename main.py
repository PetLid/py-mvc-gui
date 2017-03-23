from src.app.controllers.List import Controller as ListController
import tkinter as tk

N = tk.N
S = tk.S
E = tk.E
W = tk.W

root = tk.Tk()

# Fix layout
leftFrame = tk.Frame()
leftFrame.grid(sticky=N+S+W+E)

centerFrame = tk.Frame(width=200)
centerFrame.grid(column=1, row=0, sticky=N+S+W+E)

rightFrame = tk.Frame()
rightFrame.grid(column=2, row=0, sticky=N+S+W+E)

tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 1, weight=1)
tk.Grid.columnconfigure(root, 2, weight=1)

#
list1 = ListController(leftFrame)
list1.AddContainer('Test')
list1.AddContainer('Test2')
list1.AddContainer('Test3')
list1.SetTitle('Banana')
#list1.model.containers['Test'].data.AddContainee('Sub')


#
list2 = ListController(rightFrame)
list2.AddContainer('Test')
list2.AddContainer('Test2')
list2.AddContainer('Test3')
list2.SetTitle('Apelsin')



#app = Controller(root)
root.mainloop()
