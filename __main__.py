import customtkinter
import tkinter as tk
from PIL import ImageTk, Image
from Functions import *
from tkinter import END
from tkinter import filedialog


class CadastroSucess(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x130")
        self.title("Aviso")
        self.label = customtkinter.CTkLabel(
            self, text="Cadastrado com Sucesso!")
        self.label.pack(padx=20, pady=20)

        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=30,
                                            height=10, fg_color="green", hover_color="#272727", anchor="w",
                                            command=self.fechar_janela)
        ok_button.pack(padx=5, pady=5)

    def fechar_janela(self):
        self.destroy()


class CadastroFail(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x130")
        self.title("Aviso")
        self.label = customtkinter.CTkLabel(self, text="Erro Inesperado!")
        self.label.pack(padx=20, pady=20)

        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=30,
                                            height=10, fg_color="green", hover_color="#272727", anchor="w",
                                            command=self.fechar_janela)
        ok_button.pack(padx=5, pady=5)

    def fechar_janela(self):
        self.destroy()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        self.title("minimal example app")
        self.geometry("900x550")
        self.minsize(700, 300)
        self.maxsize(900, 500)

        self.cadastro_sucess = None
        self.cadastro_fail = None

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
                                                height=60, fg_color="#333333", hover_color="#272727", anchor="w", command=self.editar_transportadora, image=pencil_image)
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

    def convert_json(self, *ignore):
        all_inputs = [child.get() for child in self.main_frame.winfo_children(
        ) if isinstance(child, customtkinter.CTkEntry)]
        padrao_dados = [key for key in DbLink(
        ).PADRAO_DADOS if key not in ignore]
        data_json = {}
        for i in range(len(all_inputs)):
            data_json[padrao_dados[i]] = all_inputs[i]

        return data_json

    def clear_all_entries(self):
        for child in self.main_frame.winfo_children():
            if isinstance(child, customtkinter.CTkEntry):
                child.delete(0, tk.END)

    def editar_transportadora(self):
        self.delete_pages()

        def optionmenu_callback(choice):
            self.clear_all_entries()

            self.choice = choice
            dados = get_db('Transportadora', find_name=choice)
            self.peso_inicial_.insert(0, dados['peso inicial'])
            self.peso_final_.insert(0, dados['peso final'])
            self.cep_inicial_.insert(0, dados['cep inicial'])
            self.cep_final_.insert(0, dados['cep final'])
            self.prazo_.insert(0, dados['prazo'])
            self.estado_.insert(0, dados['estado'])
            self.cidade_.insert(0, dados['cidade'])
            self.regiao_.insert(0, dados['regiao'])
            self.valor_frete_.insert(0, dados['valor frete'])
            self.frete_min_.insert(0, dados['frete min'])
            self.tac_.insert(0, dados['tac'])
            self.gris_.insert(0, dados['gris'])
            self.advalorem_.insert(0, dados['advalorem'])
            self.pedagio_.insert(0, dados['pedagio'])
            self.tas_.insert(0, dados['tas'])
            self.icms_.insert(0, dados['icms'])
            self.outros_.insert(0, dados['outros'])

        self.nome_ = customtkinter.CTkOptionMenu(self.main_frame,
                                                 values=get_db(
                                                     'Transportadora', names=True),
                                                 command=optionmenu_callback,
                                                 fg_color="#df8110",
                                                 button_color="#bb6d0f",
                                                 button_hover_color="#a9630f",
                                                 width=100)

        self.peso_inicial_ = customtkinter.CTkEntry(self.main_frame,
                                                    width=85,
                                                    height=25,
                                                    border_width=1,
                                                    corner_radius=1,
                                                    )

        self.peso_final_ = customtkinter.CTkEntry(self.main_frame,
                                                  width=85,
                                                  height=25,
                                                  border_width=1,
                                                  corner_radius=1)

        self.cep_inicial_ = customtkinter.CTkEntry(self.main_frame,
                                                   width=85,
                                                   height=25,
                                                   border_width=1,
                                                   corner_radius=1)

        self.cep_final_ = customtkinter.CTkEntry(self.main_frame,
                                                 width=85,
                                                 height=25,
                                                 border_width=1,
                                                 corner_radius=1)
        self.prazo_ = customtkinter.CTkEntry(self.main_frame,
                                             width=85,
                                             height=25,
                                             border_width=1,
                                             corner_radius=1)

        self.estado_ = customtkinter.CTkEntry(self.main_frame,
                                              width=85,
                                              height=25,
                                              border_width=1,
                                              corner_radius=1)

        self.cidade_ = customtkinter.CTkEntry(self.main_frame,
                                              width=85,
                                              height=25,
                                              border_width=1,
                                              corner_radius=1)

        self.regiao_ = customtkinter.CTkEntry(self.main_frame,
                                              width=85,
                                              height=25,
                                              border_width=1,
                                              corner_radius=1)

        self.valor_frete_ = customtkinter.CTkEntry(self.main_frame,
                                                   width=85,
                                                   height=25,
                                                   border_width=1,
                                                   corner_radius=1)

        self.frete_min_ = customtkinter.CTkEntry(self.main_frame,
                                                 width=85,
                                                 height=25,
                                                 border_width=1,
                                                 corner_radius=1)

        self.tac_ = customtkinter.CTkEntry(self.main_frame,
                                           width=85,
                                           height=25,
                                           border_width=1,
                                           corner_radius=1)

        self.gris_ = customtkinter.CTkEntry(self.main_frame,
                                            width=85,
                                            height=25,
                                            border_width=1,
                                            corner_radius=1)

        self.advalorem_ = customtkinter.CTkEntry(self.main_frame,
                                                 width=85,
                                                 height=25,
                                                 border_width=1,
                                                 corner_radius=1)

        self.pedagio_ = customtkinter.CTkEntry(self.main_frame,
                                               width=85,
                                               height=25,
                                               border_width=1,
                                               corner_radius=1)
        self.tas_ = customtkinter.CTkEntry(self.main_frame,
                                           width=85,
                                           height=25,
                                           border_width=1,
                                           corner_radius=1)

        self.icms_ = customtkinter.CTkEntry(self.main_frame,
                                            width=85,
                                            height=25,
                                            border_width=1,
                                            corner_radius=1)

        self.outros_ = customtkinter.CTkEntry(self.main_frame,
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

        self.nome_.grid(row=0, column=1, pady=20)
        self.nome_.set('-')
        self.peso_inicial_.grid(row=1, column=1, pady=20)
        self.peso_final_.grid(row=2, column=1, pady=20)
        self.cep_inicial_.grid(row=3, column=1, pady=20)
        self.cep_final_.grid(row=4, column=1, pady=20)
        self.prazo_.grid(row=5, column=1, pady=20)
        self.estado_.grid(row=0, column=3, pady=20)
        self.cidade_.grid(row=1, column=3, pady=20)
        self.regiao_.grid(row=2, column=3, pady=20)
        self.valor_frete_.grid(row=3, column=3, pady=20)
        self.frete_min_.grid(row=4, column=3, pady=20)
        self.tac_.grid(row=5, column=3, pady=20)
        self.gris_.grid(row=0, column=5, pady=20)
        self.advalorem_.grid(row=1, column=5, pady=20)
        self.pedagio_.grid(row=2, column=5, pady=20)
        self.tas_.grid(row=3, column=5, pady=20)
        self.icms_.grid(row=4, column=5, pady=20)
        self.outros_.grid(row=5, column=5, pady=20)

        button_atualizar = customtkinter.CTkButton(self.main_frame, text="Atualizar", corner_radius=7,
                                                   height=30,  width=100, fg_color="#3d9336", hover_color="#51bc48", command=self.atualizar_transportadora)
        button_atualizar.grid(row=6, column=5, pady=20)

    def atualizar_transportadora(self):

        name_key = get_db(DbLink().PATHS['1'], find_key_by_name=self.choice)

        patch_db(DbLink().PATHS['1']+'/'+name_key,
                 self.convert_json('ID', 'nome'))
        self.clear_all_entries()
        self.nome_.set('-')

    def cadastro_transportadora(self):
        self.delete_pages()

        self.nome = customtkinter.CTkEntry(self.main_frame,
                                           width=140,
                                           height=25,
                                           border_width=1,
                                           corner_radius=1)

        self.peso_inicial = customtkinter.CTkEntry(self.main_frame,
                                                   width=85,
                                                   height=25,
                                                   border_width=1,
                                                   corner_radius=1,
                                                   )

        self.peso_final = customtkinter.CTkEntry(self.main_frame,
                                                 width=85,
                                                 height=25,
                                                 border_width=1,
                                                 corner_radius=1)

        self.cep_inicial = customtkinter.CTkEntry(self.main_frame,
                                                  width=85,
                                                  height=25,
                                                  border_width=1,
                                                  corner_radius=1)

        self.cep_final = customtkinter.CTkEntry(self.main_frame,
                                                width=85,
                                                height=25,
                                                border_width=1,
                                                corner_radius=1)
        self.prazo = customtkinter.CTkEntry(self.main_frame,
                                            width=85,
                                            height=25,
                                            border_width=1,
                                            corner_radius=1)

        self.estado = customtkinter.CTkEntry(self.main_frame,
                                             width=85,
                                             height=25,
                                             border_width=1,
                                             corner_radius=1)

        self.cidade = customtkinter.CTkEntry(self.main_frame,
                                             width=85,
                                             height=25,
                                             border_width=1,
                                             corner_radius=1)

        self.regiao = customtkinter.CTkEntry(self.main_frame,
                                             width=85,
                                             height=25,
                                             border_width=1,
                                             corner_radius=1)

        self.valor_frete = customtkinter.CTkEntry(self.main_frame,
                                                  width=85,
                                                  height=25,
                                                  border_width=1,
                                                  corner_radius=1)

        self.frete_min = customtkinter.CTkEntry(self.main_frame,
                                                width=85,
                                                height=25,
                                                border_width=1,
                                                corner_radius=1)

        self.tac = customtkinter.CTkEntry(self.main_frame,
                                          width=85,
                                          height=25,
                                          border_width=1,
                                          corner_radius=1)

        self.gris = customtkinter.CTkEntry(self.main_frame,
                                           width=85,
                                           height=25,
                                           border_width=1,
                                           corner_radius=1)

        self.advalorem = customtkinter.CTkEntry(self.main_frame,
                                                width=85,
                                                height=25,
                                                border_width=1,
                                                corner_radius=1)

        self.pedagio = customtkinter.CTkEntry(self.main_frame,
                                              width=85,
                                              height=25,
                                              border_width=1,
                                              corner_radius=1)
        self.tas = customtkinter.CTkEntry(self.main_frame,
                                          width=85,
                                          height=25,
                                          border_width=1,
                                          corner_radius=1)

        self.icms = customtkinter.CTkEntry(self.main_frame,
                                           width=85,
                                           height=25,
                                           border_width=1,
                                           corner_radius=1)

        self.outros = customtkinter.CTkEntry(self.main_frame,
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

        button_importar = customtkinter.CTkButton(self.main_frame, text="Importar", corner_radius=7,
                                                  height=30,  width=100, fg_color="#df8110", hover_color="#ce770f", command=self.importar_dados)
        button_importar.grid(row=6, column=0, pady=20, padx=30)

    def importar_dados(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Arquivos de excel", "*.xlsx")])

        dados = get_excel_rows(file_path)

        for lista in dados:

            post_db('Transportadora', {
                "ID": lista[0],
                "nome": lista[1],
                "peso inicial": lista[2],
                "peso final": lista[3],
                "cep inicial": lista[4],
                "cep final": lista[5],
                "prazo": lista[6],
                "estado": lista[7],
                "cidade": lista[8],
                "regiao": lista[9],
                "valor frete": lista[10],
                "frete min": lista[11],
                "tac": lista[12],
                "gris": lista[13],
                "advalorem": lista[14],
                "pedagio": lista[15],
                "tas": lista[16],
                "icms": lista[17],
                "outros": lista[18],
            })

    def cadastrar_transportadora(self):

        try:
            post_db('Transportadora', {
                "ID": get_db('Transportadora', last=True),
                "nome": self.nome.get(),
                "peso inicial": self.peso_inicial.get(),
                "peso final": self.peso_final.get(),
                "cep inicial": self.cep_inicial.get(),
                "cep final": self.cep_final.get(),
                "prazo": self.prazo.get(),
                "estado": self.estado.get(),
                "cidade": self.cidade.get(),
                "regiao": self.regiao.get(),
                "valor frete": self.valor_frete.get(),
                "frete min": self.frete_min.get(),
                "tac": self.tac.get(),
                "gris": self.gris.get(),
                "advalorem": self.advalorem.get(),
                "pedagio": self.pedagio.get(),
                "tas": self.tas.get(),
                "icms": self.icms.get(),
                "outros": self.outros.get(),
            })

            self.clear_all_entries()

            if self.cadastro_sucess is None or not self.cadastro_sucess.winfo_exists():
                # create window if its None or destroyed
                self.cadastro_sucess = CadastroSucess(self)
            else:
                self.cadastro_sucess.focus()  # if window exists focus it
        except:
            if self.cadastro_fail is None or not self.cadastro_fail.winfo_exists():
                # create window if its None or destroyed
                self.cadastro_fail = CadastroFail(self)
            else:
                self.cadastro_fail.focus()

    def delete_pages(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
