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

        truck_image = ImageTk.PhotoImage(Image.open(
            "images/truck.png").resize((20, 20)), Image.ANTIALIAS)

        pencil_image = ImageTk.PhotoImage(Image.open(
            "images/pencil.png").resize((20, 20)), Image.ANTIALIAS)

        eye_image = ImageTk.PhotoImage(Image.open(
            "images/eye.png").resize((20, 20)), Image.ANTIALIAS)

        bag_image = ImageTk.PhotoImage(Image.open(
            "images/bag.png").resize((20, 20)), Image.ANTIALIAS)

        self.painel = customtkinter.CTkFrame(self, height=550, width=180)
        self.painel.grid(row=0, column=0)

        label_transp = customtkinter.CTkLabel(
            self.painel, text="Transportadora", height=45)
        label_transp.pack()

        cadastrar_transp = customtkinter.CTkButton(self.painel, text="Cadastrar", corner_radius=0, height=60,
                                                   fg_color="#333333", hover_color="#272727", anchor="w", image=truck_image, command=self.cadastro_transportadora)
        cadastrar_transp.pack()

        editar_transp = customtkinter.CTkButton(self.painel, text="Editar", corner_radius=0,
                                                height=60, fg_color="#333333", hover_color="#272727", anchor="w", image=pencil_image)
        editar_transp.pack()

        visualizar_transp = customtkinter.CTkButton(
            self.painel, text="Visualizar", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=eye_image, anchor="w")
        visualizar_transp.pack()

        produto_label = customtkinter.CTkLabel(
            self.painel, text="Produto", height=35)
        produto_label.pack()

        cadastrar_produto = customtkinter.CTkButton(
            self.painel, text="Cadastrar", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=bag_image, anchor="w")
        cadastrar_produto.pack()

        editar_produto = customtkinter.CTkButton(self.painel, text="Editar", corner_radius=0,
                                                 height=50, fg_color="#333333", hover_color="#272727", image=pencil_image, anchor="w")
        editar_produto.pack()

        visualizar_produto = customtkinter.CTkButton(
            self.painel, text="Visualizar", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=eye_image, anchor="w")
        visualizar_produto.pack()

        frete_label = customtkinter.CTkLabel(
            self.painel, text="Frete", height=35)
        frete_label.pack()
        frete_label = customtkinter.CTkLabel(
            self.painel, text="Frete", height=35)
        frete_label.pack()
        frete_label = customtkinter.CTkLabel(
            self.painel, text="Frete", height=35)
        frete_label.pack()

        self.main_frame = customtkinter.CTkFrame(
            self, width=700, height=450, fg_color='#313131')
        self.main_frame.grid(row=0, column=1, padx=30, pady=20, ipadx=10)

    def cadastro_transportadora(self):
        self.delete_pages()

        self.nome = customtkinter.CTkEntry(self.main_frame,
                                      placeholder_text="Nome",
                                      width=140,
                                      height=25,
                                      border_width=1,
                                      corner_radius=1)

        self.peso_inicial = customtkinter.CTkEntry(self.main_frame,
                                              placeholder_text="Peso Inicial",
                                              width=85,
                                              height=25,
                                              border_width=1,
                                              corner_radius=1,
                                              )

        self.peso_final = customtkinter.CTkEntry(self.main_frame,
                                            placeholder_text="Peso Final",
                                            width=85,
                                            height=25,
                                            border_width=1,
                                            corner_radius=1)

        self.cep_inicial = customtkinter.CTkEntry(self.main_frame,
                                             placeholder_text="Cep Inicial",
                                             width=85,
                                             height=25,
                                             border_width=1,
                                             corner_radius=1)

        self.cep_final = customtkinter.CTkEntry(self.main_frame,
                                           placeholder_text="Cep Final",
                                           width=85,
                                           height=25,
                                           border_width=1,
                                           corner_radius=1)
        self.prazo = customtkinter.CTkEntry(self.main_frame,
                                       placeholder_text="Prazo",
                                       width=85,
                                       height=25,
                                       border_width=1,
                                       corner_radius=1)

        self.estado = customtkinter.CTkEntry(self.main_frame,
                                        placeholder_text="Estado",
                                        width=85,
                                        height=25,
                                        border_width=1,
                                        corner_radius=1)

        self.cidade = customtkinter.CTkEntry(self.main_frame,
                                        placeholder_text="Cidade",
                                        width=85,
                                        height=25,
                                        border_width=1,
                                        corner_radius=1)

        self.regiao = customtkinter.CTkEntry(self.main_frame,
                                        placeholder_text="Região",
                                        width=85,
                                        height=25,
                                        border_width=1,
                                        corner_radius=1)

        self.valor_frete = customtkinter.CTkEntry(self.main_frame,
                                             placeholder_text="Valor Frete",
                                             width=85,
                                             height=25,
                                             border_width=1,
                                             corner_radius=1)

        self.frete_min = customtkinter.CTkEntry(self.main_frame,
                                           placeholder_text="Frete Mínimo",
                                           width=85,
                                           height=25,
                                           border_width=1,
                                           corner_radius=1)

        self.tac = customtkinter.CTkEntry(self.main_frame,
                                     placeholder_text="Tac",
                                     width=85,
                                     height=25,
                                     border_width=1,
                                     corner_radius=1)

        self.gris = customtkinter.CTkEntry(self.main_frame,
                                      placeholder_text="Gris",
                                      width=85,
                                      height=25,
                                      border_width=1,
                                      corner_radius=1)

        self.advalorem = customtkinter.CTkEntry(self.main_frame,
                                           placeholder_text="Advalorem",
                                           width=85,
                                           height=25,
                                           border_width=1,
                                           corner_radius=1)

        self.pedagio = customtkinter.CTkEntry(self.main_frame,
                                         placeholder_text="Pedágio",
                                         width=85,
                                         height=25,
                                         border_width=1,
                                         corner_radius=1)
        self.tas = customtkinter.CTkEntry(self.main_frame,
                                     placeholder_text="Tas",
                                     width=85,
                                     height=25,
                                     border_width=1,
                                     corner_radius=1)

        self.icms = customtkinter.CTkEntry(self.main_frame,
                                      placeholder_text="Icms",
                                      width=85,
                                      height=25,
                                      border_width=1,
                                      corner_radius=1)

        self.outros = customtkinter.CTkEntry(self.main_frame,
                                        placeholder_text="Outros",
                                        width=140,
                                        height=25,
                                        border_width=1,
                                        corner_radius=1)

        label_nome = customtkinter.CTkLabel(
            self.main_frame,
            text="Nome:"

        )
        label_pinicial = customtkinter.CTkLabel(
            self.main_frame,
            text="Peso Inicial:"

        )
        label_pfinal = customtkinter.CTkLabel(
            self.main_frame,
            text="Peso Final:"

        )
        label_cepinicial = customtkinter.CTkLabel(
            self.main_frame,
            text="Cep Inicial:"

        )
        label_cepfinal = customtkinter.CTkLabel(
            self.main_frame,
            text="Cep Final:"

        )
        label_prazo = customtkinter.CTkLabel(
            self.main_frame,
            text="Prazo:"

        )
        label_estado = customtkinter.CTkLabel(
            self.main_frame,
            text="Estado:"

        )
        label_cidade = customtkinter.CTkLabel(
            self.main_frame,
            text="Cidade:"

        )
        label_regiao = customtkinter.CTkLabel(
            self.main_frame,
            text="Região:"

        )
        label_vfrete = customtkinter.CTkLabel(
            self.main_frame,
            text="Valor Frete:"

        )
        label_fretemin = customtkinter.CTkLabel(
            self.main_frame,
            text="Frete Mín:"

        )
        label_tac = customtkinter.CTkLabel(
            self.main_frame,
            text="Tac:"

        )
        label_gris = customtkinter.CTkLabel(
            self.main_frame,
            text="Gris:"

        )
        label_advalorem = customtkinter.CTkLabel(
            self.main_frame,
            text="Advalorem:"

        )
        label_pedagio = customtkinter.CTkLabel(
            self.main_frame,
            text="Pedágio:"

        )
        label_tas = customtkinter.CTkLabel(
            self.main_frame,
            text="Tas:"

        )
        label_icms = customtkinter.CTkLabel(
            self.main_frame,
            text="Icms:"

        )

        label_outros = customtkinter.CTkLabel(
            self.main_frame,
            text="Outros:"

        )

        label_nome.grid(row=0, column=0, padx=10)
        label_pinicial.grid(row=1, column=0, padx=10)
        label_pfinal.grid(row=2, column=0, padx=10)
        label_cepinicial.grid(row=3, column=0, padx=10)
        label_cepfinal.grid(row=4, column=0, padx=10)
        label_prazo.grid(row=5, column=0, padx=10)
        label_estado.grid(row=0, column=2, padx=10)
        label_cidade.grid(row=1, column=2, padx=10)
        label_regiao.grid(row=2, column=2, padx=10)
        label_vfrete.grid(row=3, column=2, padx=10)
        label_fretemin.grid(row=4, column=2, padx=10)
        label_tac.grid(row=5, column=2, padx=10)
        label_gris.grid(row=0, column=4, padx=10)
        label_advalorem.grid(row=1, column=4, padx=10)
        label_pedagio.grid(row=2, column=4, padx=10)
        label_tas.grid(row=3, column=4, padx=10)
        label_icms.grid(row=4, column=4, padx=10)
        label_outros.grid(row=5, column=4, padx=10)

        self.nome.grid(row=0, column=1, pady=20)
        self.peso_inicial.grid(row=1, column=1, pady=20)
        self.peso_final.grid(row=2, column=1, pady=20)
        self.cep_inicial.grid(row=3, column=1, pady=20)
        self.cep_final.grid(row=4, column=1, pady=20)
        self.prazo.grid(row=5, column=1, pady=20)
        self.estado.grid(row=0, column=3, pady=20)
        self.cidade.grid(row=1, column=3, pady=20)
        self.regiao.grid(row=2, column=3, pady=20)
        self.valor_frete.grid(row=3, column=3, pady=20)
        self.frete_min.grid(row=4, column=3, pady=20)
        self.tac.grid(row=5, column=3, pady=20)
        self.gris.grid(row=0, column=5, pady=20)
        self.advalorem.grid(row=1, column=5, pady=20)
        self.pedagio.grid(row=2, column=5, pady=20)
        self.tas.grid(row=3, column=5, pady=20)
        self.icms.grid(row=4, column=5, pady=20)
        self.outros.grid(row=5, column=5, pady=20)

        button_cadastrar = customtkinter.CTkButton(self.main_frame, text="Cadastrar", corner_radius=7,
                                                   height=30,  width=100, fg_color="#3d9336", hover_color="#51bc48", command=self.cadastrar_transportadora)
        button_cadastrar.grid(row=6, column=5, pady=20)

    def cadastrar_transportadora(self):
        print(self.nome.get())

    def delete_pages(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
