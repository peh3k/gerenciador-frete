import customtkinter
import tkinter as tk
from PIL import ImageTk, Image






class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        self.title("minimal example app")
        self.geometry("900x550")
        self.minsize(700, 300)
        self.maxsize(900, 500)

        truck_image = ImageTk.PhotoImage(Image.open("images/truck.png").resize((20,20)), Image.ANTIALIAS)

        pencil_image = ImageTk.PhotoImage(Image.open("images/pencil.png").resize((20,20)), Image.ANTIALIAS)

        eye_image = ImageTk.PhotoImage(Image.open("images/eye.png").resize((20,20)), Image.ANTIALIAS)

        bag_image = ImageTk.PhotoImage(Image.open("images/bag.png").resize((20,20)), Image.ANTIALIAS)

        self.painel = customtkinter.CTkFrame(self, height=550, width=180)
        self.painel.grid(row=0, column=0)

        label_transp = customtkinter.CTkLabel(self.painel, text="Transportadora", height=45)
        label_transp.pack()

        cadastrar_transp = customtkinter.CTkButton(self.painel, text="Cadastrar", corner_radius=0, height=60, fg_color="#333333", hover_color="#272727", anchor="w", image=truck_image, command=self.cadastro_transportadora)
        cadastrar_transp.pack()

        editar_transp = customtkinter.CTkButton(self.painel, text="Editar", corner_radius=0, height=60, fg_color="#333333", hover_color="#272727", anchor="w", image=pencil_image)
        editar_transp.pack()

        visualizar_transp = customtkinter.CTkButton(self.painel, text="Visualizar", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=eye_image, anchor="w")
        visualizar_transp.pack()

        produto_label = customtkinter.CTkLabel(self.painel, text="Produto", height=35)
        produto_label.pack()

        cadastrar_produto = customtkinter.CTkButton(self.painel, text="Cadastrar", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=bag_image, anchor="w")
        cadastrar_produto.pack()

        editar_produto = customtkinter.CTkButton(self.painel, text="Editar", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=pencil_image, anchor="w")
        editar_produto.pack()

        visualizar_produto = customtkinter.CTkButton(self.painel, text="Visualizar", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=eye_image, anchor="w")
        visualizar_produto.pack()

        frete_label = customtkinter.CTkLabel(self.painel, text="Frete", height=35)
        frete_label.pack()
        frete_label = customtkinter.CTkLabel(self.painel, text="Frete", height=35)
        frete_label.pack()
        frete_label = customtkinter.CTkLabel(self.painel, text="Frete", height=35)
        frete_label.pack()

        self.main_frame = customtkinter.CTkFrame(self, width=700, height=450, fg_color='#313131')
        self.main_frame.grid(row=0, column=1, padx=30, pady= 30)

    def cadastro_transportadora(self):
        self.delete_pages()
        
        nome = customtkinter.CTkEntry(self.main_frame,
                               placeholder_text="Nome",
                               width=120,
                               height=25,
                               border_width=1,
                               corner_radius=1)

        nome = customtkinter.CTkEntry(self.main_frame,
                               placeholder_text="Nome",
                               width=120,
                               height=25,
                               border_width=1,
                               corner_radius=1)

        nome = customtkinter.CTkEntry(self.main_frame,
                               placeholder_text="Nome",
                               width=120,
                               height=25,
                               border_width=1,
                               corner_radius=1)

        nome = customtkinter.CTkEntry(self.main_frame,
                               placeholder_text="Nome",
                               width=120,
                               height=25,
                               border_width=1,
                               corner_radius=1)
        
        nome = customtkinter.CTkEntry(self.main_frame,
                               placeholder_text="Nome",
                               width=120,
                               height=25,
                               border_width=1,
                               corner_radius=1)
        nome = customtkinter.CTkEntry(self.main_frame,
                               placeholder_text="Nome",
                               width=120,
                               height=25,
                               border_width=1,
                               corner_radius=1)

        nome = customtkinter.CTkEntry(self.main_frame,
                               placeholder_text="Nome",
                               width=120,
                               height=25,
                               border_width=1,
                               corner_radius=1)

        nome = customtkinter.CTkEntry(self.main_frame,
                               placeholder_text="Nome",
                               width=120,
                               height=25,
                               border_width=1,
                               corner_radius=1)

        nome = customtkinter.CTkEntry(self.main_frame,
                               placeholder_text="Nome",
                               width=120,
                               height=25,
                               border_width=1,
                               corner_radius=1)
        
        nome = customtkinter.CTkEntry(self.main_frame,
                               placeholder_text="Nome",
                               width=120,
                               height=25,
                               border_width=1,
                               corner_radius=1)
        
        

    def delete_pages(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()

        
class CadastroTransportadora(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        



if __name__ == "__main__":
    app = App()
    app.mainloop()