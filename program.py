import customtkinter
from PIL import ImageTk, Image
from tkinter import filedialog
from Functions import *
import logging
import tkinter as tk

# Variaveis globais importantes de busca

global PADRAO_TRANSPORTADORA, PADRAO_PRODUTO, PATH_PRODUTO, PATH_TRANSPORTADORA

PATH_TRANSPORTADORA = DbLink().PATHS[0]
PADRAO_TRANSPORTADORA = DbLink().PADRAO_DADOS[0]
PATH_PRODUTO = DbLink().PATHS[1]
PADRAO_PRODUTO = DbLink().PADRAO_DADOS[1]


class TabelaTransportadoraDuplicatasPopup(customtkinter.CTkToplevel):
    def __init__(self, *args, header=[], **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x400")
        self.title("Itens Ignorados (Duplicaatas)")
        criar_tabela(self, PADRAO_TRANSPORTADORA, header)


class BaixadoSucessoPopup(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x130")
        self.title("Aviso")
        header_label = customtkinter.CTkLabel(
            self, text="Baixado com Sucesso!").pack(padx=20, pady=20)
        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70, height=30,
                                            fg_color="#df8110", hover_color="#ce770f", command=self.fechar_janela).pack(padx=5, pady=5)

    def fechar_janela(self):
        self.destroy()


class CadastroSucessoPopup(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x130")
        self.title("Aviso")
        header_label = customtkinter.CTkLabel(
            self, text="Cadastrado com Sucesso!").pack(padx=20, pady=20)
        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70, height=30,
                                            fg_color="#df8110", hover_color="#ce770f", command=self.fechar_janela).pack(padx=5, pady=5)

    def fechar_janela(self):
        self.destroy()


class ErroInesperadoPopup(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x130")
        self.title("Aviso")
        header_label = customtkinter.CTkLabel(
            self, text="Erro Inesperado!").pack(padx=20, pady=20)
        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70, height=30,
                                            fg_color="#df8110", hover_color="#ce770f", command=self.fechar_janela).pack(padx=5, pady=5)

    def fechar_janela(self):
        self.destroy()

class ItemExistente(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x130")
        self.title("Aviso")
        header_label = customtkinter.CTkLabel(
            self, text="Item Já Existente!").pack(padx=20, pady=20)
        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70, height=30,
                                            fg_color="#df8110", hover_color="#ce770f", command=self.fechar_janela).pack(padx=5, pady=5)

    def fechar_janela(self):
        self.destroy()

class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=700, height=480)


class PainelLateral(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Widgets estão no App principal


class Home(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Imagem da tela inicial
        img = ImageTk.PhotoImage(Image.open(
            "images/home.png").resize((700, 480)))
        label = customtkinter.CTkLabel(self, text='', image=img)
        label.pack()


class CadastroTransportadoraScreen(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Widgets da tela

        label_nome = customtkinter.CTkLabel(self, text="Nome:").grid(
            row=0, column=0, pady=20, padx=10)
        self.nome = customtkinter.CTkEntry(
            self, width=140, height=25, border_width=1, corner_radius=2).grid(row=0, column=1)
        label_pinicial = customtkinter.CTkLabel(
            self, text="Peso Inicial:").grid(row=1, column=0, pady=20, padx=10)
        self.peso_inicial = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2,).grid(row=1, column=1)
        label_pfinal = customtkinter.CTkLabel(
            self, text="Peso Final:").grid(row=2, column=0, pady=20, padx=10)
        self.peso_final = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2).grid(row=2, column=1)
        label_cepinicial = customtkinter.CTkLabel(
            self, text="Cep Inicial:").grid(row=3, column=0, pady=20, padx=10)
        self.cep_inicial = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2).grid(row=3, column=1)
        label_cepfinal = customtkinter.CTkLabel(
            self, text="Cep Final:").grid(row=4, column=0, pady=20, padx=10)
        self.cep_final = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2).grid(row=4, column=1)
        label_prazo = customtkinter.CTkLabel(self, text="Prazo:").grid(
            row=5, column=0, pady=20, padx=10)
        self.prazo = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2).grid(row=5, column=1)
        label_estado = customtkinter.CTkLabel(
            self, text="Estado:").grid(row=0, column=2, pady=20, padx=10)
        self.estado = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2).grid(row=0, column=3)
        label_cidade = customtkinter.CTkLabel(
            self, text="Cidade:").grid(row=1, column=2, pady=20, padx=10)
        self.cidade = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2).grid(row=1, column=3)
        label_regiao = customtkinter.CTkLabel(
            self, text="Região:").grid(row=2, column=2, pady=20, padx=10)
        self.regiao = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2).grid(row=2, column=3)
        label_vfrete = customtkinter.CTkLabel(
            self, text="Valor Frete:").grid(row=3, column=2, pady=20, padx=10)
        self.valor_frete = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2).grid(row=3, column=3)
        label_fretemin = customtkinter.CTkLabel(
            self, text="Frete Mín:").grid(row=4, column=2, pady=20, padx=10)
        self.frete_min = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2).grid(row=4, column=3)
        label_tac = customtkinter.CTkLabel(self, text="Tac:").grid(
            row=5, column=2, pady=20, padx=10)
        self.tac = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2).grid(row=5, column=3)
        label_gris = customtkinter.CTkLabel(self, text="Gris:").grid(
            row=0, column=4, pady=20, padx=10)
        self.gris = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2).grid(row=0, column=5)
        label_advalorem = customtkinter.CTkLabel(
            self, text="Advalorem:").grid(row=1, column=4, pady=20, padx=10)
        self.advalorem = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2).grid(row=1, column=5)
        label_pedagio = customtkinter.CTkLabel(
            self, text="Pedágio:").grid(row=2, column=4, pady=20, padx=10)
        self.pedagio = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2).grid(row=2, column=5)
        label_tas = customtkinter.CTkLabel(self, text="Tas:").grid(
            row=3, column=4, pady=20, padx=10)
        self.tas = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2).grid(row=3, column=5)
        label_icms = customtkinter.CTkLabel(self, text="Icms:").grid(
            row=4, column=4, pady=20, padx=10)
        self.icms = customtkinter.CTkEntry(
            self, width=85, height=25, border_width=1, corner_radius=2).grid(row=4, column=5)
        label_outros = customtkinter.CTkLabel(
            self, text="Outros:").grid(row=5, column=4, pady=20, padx=10)
        self.outros = customtkinter.CTkEntry(
            self, width=140, height=25, border_width=1, corner_radius=2).grid(row=5, column=5)
        button_importar = customtkinter.CTkButton(
            self, text="Importar", corner_radius=7, height=30,  width=100, fg_color="#df8110", hover_color="#ce770f", command=self.importar_transportadoras_from_excel)
        button_importar.grid(row=6, column=0, padx=25, pady=20)
        button_cadastrar = customtkinter.CTkButton(
            self, text="Cadastrar", corner_radius=7, height=30,  width=100, fg_color="#3d9336", hover_color="#51bc48", command=self.cadastrar_transportadora_from_inputs)
        button_cadastrar.grid(row=6, column=5, pady=20)
        # Fim dos widgets

    # Métodos da tela de cadastro de transportadoras
    
    # Pegar todos os textos dos inputs desse frame
    def get_all_inputs_text(self):
        all_inputs = [child.get() for child in self.winfo_children(
        ) if isinstance(child, customtkinter.CTkEntry)]

        return all_inputs
    
    # Zerar todos os inputs
    def clear_all_entries(self):
        for child in self.winfo_children():
            if isinstance(child, customtkinter.CTkEntry):
                child.delete(0, tk.END)
    
    def importar_transportadoras_from_excel(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Arquivos de excel", "*.xlsx")])
        try:
            
            # Retorna os dados iguais e os dados únicos
            upload_returned = upload_massivo_transportadora(file_path)
            
            # Caso tenha dados únicos exibe o popup de cadastro concluído, caso contrario exibe a tabela de duplicatas
            if len(upload_returned[0]) > 0:
                TabelaTransportadoraDuplicatasPopup(
                    self, header=upload_returned[0])
            if len(upload_returned[1]) > 0:
                CadastroSucessoPopup(self)
            if len(upload_returned[1]) == 0:
                logging.warning('nao foi preciso o cadastro de nenhuma transportadora')
        except:
            logging.warning("Erro ao importar dados transportadora")
            ErroInesperadoPopup(self)

    def cadastrar_transportadora_from_inputs(self):
        try:
            text_entries = self.get_all_inputs_text()
            
            # Gera um loggin caso o usuario não digite o nome da empresa
            if len(text_entries[0]) <= 0:
                logging.warning('empresa sem nome')
            
            # Cadastra a transportadora
            else:
                new_text_entries = []
                new_text_entries.append(text_entries)
                dados_insert = list_to_dict(
                    new_text_entries, PADRAO_TRANSPORTADORA[1:])
                post_dados = post_db(PATH_TRANSPORTADORA, dados_insert, search_same=new_text_entries)
                self.clear_all_entries()
                if post_dados is not False:
                    CadastroSucessoPopup(self)
                else:
                    ItemExistente(self)
                    
        except:
            logging.warning('Cadastro manual transportadora')
            ErroInesperadoPopup(self)


class EditarTransportadoraScreen(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        img = ImageTk.PhotoImage(Image.open(
            "images/home.png").resize((700, 450)))

        # Create a Label Widget to display the text or Image
        label = customtkinter.CTkLabel(self, text='', image=img)
        label.pack()


class VisualizarTransportadoraScreen(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        img = ImageTk.PhotoImage(Image.open(
            "images/home.png").resize((700, 450)))

        # Create a Label Widget to display the text or Image
        label = customtkinter.CTkLabel(self, text='', image=img)
        label.pack()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configurações gerais da janela
        customtkinter.set_appearance_mode("dark")
        self.title("Calculadora de Frete")
        self.geometry("900x500")
        self.resizable(False, False)

        """
            /// PAINEL LATERAL ///

        """
        self.painel_lateral = PainelLateral(self)
        self.painel_lateral.pack(side='left')
        truck_image = ImageTk.PhotoImage(Image.open(
            "images/truck.png").resize((20, 20)), Image.ANTIALIAS)
        pencil_image = ImageTk.PhotoImage(Image.open(
            "images/pencil.png").resize((20, 20)), Image.ANTIALIAS)
        eye_image = ImageTk.PhotoImage(Image.open(
            "images/eye.png").resize((20, 20)), Image.ANTIALIAS)
        bag_image = ImageTk.PhotoImage(Image.open(
            "images/bag.png").resize((20, 20)), Image.ANTIALIAS)
        house_image = ImageTk.PhotoImage(Image.open(
            "images/house.png").resize((15, 15)), Image.ANTIALIAS)
        home_button = customtkinter.CTkButton(self.painel_lateral, text="Home", corner_radius=0, height=60,
                                              command=self.home_screen, fg_color="#1a1a1a", hover_color="#272727", anchor="center", image=house_image).pack()
        label_transp = customtkinter.CTkLabel(
            self.painel_lateral, text="Transportadora", height=45)
        cadastrar_transp = customtkinter.CTkButton(self.painel_lateral, text="Cadastrar", corner_radius=0, command=self.cadastro_transportadora_screen,
                                                   height=60, fg_color="#333333", hover_color="#272727", anchor="center", image=truck_image).pack()
        visualizar_transp = customtkinter.CTkButton(self.painel_lateral, text="Visualizar", corner_radius=0,
                                                    height=50, fg_color="#333333", hover_color="#272727", image=eye_image, anchor="center").pack()
        editar_transp = customtkinter.CTkButton(self.painel_lateral, text="Editar", corner_radius=0,
                                                height=60, fg_color="#333333", hover_color="#272727", anchor="center", image=pencil_image).pack()
        produto_label = customtkinter.CTkLabel(
            self.painel_lateral, text="Produto", height=35).pack()
        cadastrar_produto = customtkinter.CTkButton(self.painel_lateral, text="Cadastrar", corner_radius=0,
                                                    height=50, fg_color="#333333", hover_color="#272727", image=bag_image, anchor="center").pack()
        visualizar_produto = customtkinter.CTkButton(self.painel_lateral, text="Visualizar", corner_radius=0,
                                                     height=50, fg_color="#333333", hover_color="#272727", image=eye_image, anchor="center").pack()
        editar_produto = customtkinter.CTkButton(self.painel_lateral, text="Editar", corner_radius=0,
                                                 height=50, fg_color="#333333", hover_color="#272727", image=pencil_image, anchor="center").pack()
        calculo_label = customtkinter.CTkLabel(
            self.painel_lateral, text="Calculo Frete", height=35).pack()
        calcular_frete = customtkinter.CTkButton(self.painel_lateral, text="Calcular", corner_radius=0,
                                                 height=50, fg_color="#333333", hover_color="#272727", image=eye_image, anchor="center").pack()

        # Frame Principal
        self.MAIN_FRAME = MainFrame(self)
        self.MAIN_FRAME.pack(side='right', padx=30)
        self.MAIN_FRAME.pack_propagate(False)

        # Home de Entrada
        self.MAIN_HOME_SCREEN = Home(self.MAIN_FRAME)
        self.MAIN_HOME_SCREEN.pack()

    def delete_pages(self):
        for frame in self.MAIN_FRAME.winfo_children():
            frame.destroy()

    def home_screen(self):
        self.delete_pages()
        home_screen = Home(self.MAIN_FRAME)
        home_screen.pack()

    def cadastro_transportadora_screen(self):
        self.delete_pages()
        cadastro_transportadora_screen = CadastroTransportadoraScreen(
            self.MAIN_FRAME)
        cadastro_transportadora_screen.pack(ipadx=30, ipady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
