from tkinter import *

root = Tk()

entry1 = Entry(root)
entry1.pack()

entry2 = Entry(root)
entry2.pack()

# Define o foco do teclado no segundo campo de entrada
entry2.focus()

root.mainloop()
