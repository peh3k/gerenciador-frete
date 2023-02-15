import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Exemplo de Navegação")
        
        # Criação do frame principal que irá conter as demais telas
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        # Criação das telas
        self.tela1 = Tela1(self.container, self)
        self.tela2 = Tela2(self.container, self)
        
        # Exibe a primeira tela
        self.tela1.pack()
    
    def mostrar_tela1(self):
        # Esconde todas as telas e exibe a primeira
        self.tela1.pack()
        self.tela2.pack_forget()
        
    def mostrar_tela2(self):
        # Esconde todas as telas e exibe a segunda
        self.tela2.pack()
        self.tela1.pack_forget()

class Tela1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Criação dos widgets da tela 1
        label = tk.Label(self, text="Tela 1")
        button = tk.Button(self, text="Ir para tela 2", command=self.controller.mostrar_tela2)
        
        # Exibição dos widgets da tela 1
        label.pack()
        button.pack()

class Tela2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Criação dos widgets da tela 2
        label = tk.Label(self, text="Tela 2")
        button = tk.Button(self, text="Voltar para tela 1", command=self.controller.mostrar_tela1)
        
        # Exibição dos widgets da tela 2
        label.pack()
        button.pack()
        
if __name__ == '__main__':
    app = Application()
    app.mainloop()

'''
transportadora_label = customtkinter.CTkLabel(master=self, text="Transportadora", height=35)
        transportadora_label.grid(row=0, column=0)

        cadastrar_transp = customtkinter.CTkButton(master=self, text="Cadastrar", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=truck_image, anchor="w", command=self.cadastro_transportadora)
        cadastrar_transp.grid(row=1, column=0)

        editar_transp = customtkinter.CTkButton(master=self, text="Editar", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=pencil_image, anchor="w")
        editar_transp.grid(row=2, column=0)

        visualizar_transp = customtkinter.CTkButton(master=self, text="Visualizar", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=eye_image, anchor="w")
        visualizar_transp.grid(row=3, column=0)

        produto_label = customtkinter.CTkLabel(master=self, text="Produto", height=35)
        produto_label.grid(row=4, column=0, padx=20)

        cadastrar_produto = customtkinter.CTkButton(master=self, text="Cadastrar", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=bag_image, anchor="w")
        cadastrar_produto.grid(row=5, column=0)

        editar_produto = customtkinter.CTkButton(master=self, text="Editar", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=pencil_image, anchor="w")
        editar_produto.grid(row=6, column=0)

        visualizar_produto = customtkinter.CTkButton(master=self, text="Visualizar", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=eye_image, anchor="w")
        visualizar_produto.grid(row=7, column=0)

        self.cadastro_transp = CadastroTransportadora(master=self, height=300)

'''