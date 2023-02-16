from tkinter import *
from tkinter import filedialog

# Cria a janela
root = Tk()

# Função para abrir o gerenciador de arquivos
def open_file():
    file_path = filedialog.askopenfilename()
    print(file_path)

# Cria o botão e adiciona-o à janela
button = Button(root, text="Abrir arquivo", command=open_file)
button.pack()

# Inicia o loop principal da GUI
root.mainloop()
