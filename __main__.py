import customtkinter
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
from Functions import *
from tkinter import filedialog
choice = []
padrao_dados = [key for key in DbLink().PADRAO_DADOS[1].keys()]


def criar_tabela(frame, colunas, linhas):
    bg_colors = ["white", "gray"]
    frame_tabela = ttk.Frame(frame)
    frame_tabela.pack(fill='both', expand=True)
    style = ttk.Style()
    style.configure("Custom.Treeview", highlightthickness=0,
                    bd=2, relief="groove")
    # cria a lista de colunas e linhas

    # define o objeto Treeview
    tree = ttk.Treeview(frame_tabela, style="Custom.Treeview",
                        columns=colunas, show='headings')

    # define o nome das colunas
    for col in colunas:
        tree.heading(col, text=col)

    for a in linhas:
        tree.insert('', 'end', values=a)

    # configura as colunas para se ajustarem à largura dos dados
    for col in colunas:
        tree.column(col, width=130, anchor='center')

    # verifica se o número de colunas é maior que a largura da janela
    if len(colunas) > 1:
        # cria um scrollbar horizontal
        hsb = ttk.Scrollbar(
            frame_tabela, orient='horizontal', command=tree.xview)
        hsb.pack(side='bottom', fill='x')
        tree.configure(xscrollcommand=hsb.set)

    # cria um scrollbar vertical
    vsb = ttk.Scrollbar(
        frame_tabela, orient='vertical', command=tree.yview)
    vsb.pack(side='right', fill='y')
    tree.configure(yscrollcommand=vsb.set)
    tree.tag_configure("white", background="white")
    tree.tag_configure("gray", background="gray")

    # Aplicar as cores de fundo às linhas da tabela
    for i, item in enumerate(tree.get_children()):
        bg_color = bg_colors[i % len(bg_colors)]
        tree.item(item, tags=(bg_color,))
    # adiciona a tabela e configura o layout
    tree.pack(fill='both', expand=True)


class TabelaTransportadora(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        width = 650
        height = 400

        # obter as dimensões da tela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        downloadimage = ImageTk.PhotoImage(Image.open(
            "images/download.png").resize((15, 15)), Image.ANTIALIAS)
        button = customtkinter.CTkButton(
            self, text='Baixar', image=downloadimage, width=30, command=self.baixar_tabela)
        button.pack(side="bottom", pady=10)

        self.baixado_screen = None
        self.baixado_fail = None


        # calcular as coordenadas x e y da janela
        x = (screen_width // 2) - (width // 2) + 60
        y = (screen_height // 2) - (height // 2) - 25

        # definir a posição da janela
        self.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.title("Transportadoras")

        colunas = [i for i in DbLink().PADRAO_DADOS[0].keys()]
        get = get_db('Transportadora')
        list_dict = [get[item] for item in get]
        padrao = [item for item in DbLink().PADRAO_DADOS[0]]

        new_list = []
        for a in range(len(get)):
            dict = {}
            for i in range(len(padrao)):

                dict[padrao[i]] = list_dict[a][padrao[i]]
            new_list.append(dict)

        all_dicts = dicts_to_lists(new_list)
        criar_tabela(self, colunas, all_dicts[1:])

    def baixar_tabela(self):
        try:
            dados = get_db('Transportadora')
            lista = [dados[item] for item in dados]
            padrao = [item for item in DbLink().PADRAO_DADOS[0]]
            nova_lista = [list(item.values()) for item in lista]
            padrao.sort()
            criar_tabela_excel(padrao, nova_lista,
                               'Tabela_Transportadoras.xlsx')
            if self.baixado_screen is None or not self.baixado_screen.winfo_exists():
                # create window if its None or destroyed
                self.baixado_screen = BaixadoSucesso(self)
        except:
            if self.baixado_fail is None or not self.baixado_fail.winfo_exists():
                # create window if its None or destroyed
                self.baixado_fail = CadastroFail(self)


class TabelaProdutos(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        width = 650
        height = 400

        # obter as dimensões da tela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.baixado_screen = None
        self.baixado_fail = None

        downloadimage = ImageTk.PhotoImage(Image.open(
            "images/download.png").resize((15, 15)), Image.ANTIALIAS)
        button = customtkinter.CTkButton(
            self, text='Baixar', image=downloadimage, width=30, command=self.baixar_tabela)
        button.pack(side="bottom", pady=10)

        # calcular as coordenadas x e y da janela
        x = (screen_width // 2) - (width // 2) + 60
        y = (screen_height // 2) - (height // 2) - 25

        # definir a posição da janela
        self.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.title("Produtos")

        colunas = [i for i in DbLink().PADRAO_DADOS[1].keys()]
        get = get_db('Produto')
        list_dict = [get[item] for item in get]
        padrao = [item for item in DbLink().PADRAO_DADOS[1]]

        new_list = []
        for a in range(len(list_dict)):
            dict = {}
            for i in range(len(padrao)):

                dict[padrao[i]] = list_dict[a][padrao[i]]

            new_list.append(dict)

        all_dicts = dicts_to_lists(new_list)
        criar_tabela(self, colunas, all_dicts[1:])

    def baixar_tabela(self):
        try:
            dados = get_db('Produto')
            lista = [dados[item] for item in dados]
            padrao = [item for item in DbLink().PADRAO_DADOS[1]]
            nova_lista = [list(item.values()) for item in lista]
            padrao.sort()
            criar_tabela_excel(padrao, nova_lista, 'Tabela_Produtos.xlsx')

            if self.baixado_screen is None or not self.baixado_screen.winfo_exists():
                # create window if its None or destroyed
                self.baixado_screen = BaixadoSucesso(self)
        except:
            if self.baixado_fail is None or not self.baixado_fail.winfo_exists():
                # create window if its None or destroyed
                self.baixado_fail = CadastroFail(self)


class DeleterTransportadora(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("300x180")
        self.title("Aviso")
        self.label = customtkinter.CTkLabel(
            self, text="DELETAR TRANSPORTADORA?")
        self.label.pack(pady=20)

        yes_button = customtkinter.CTkButton(self, text="Sim", corner_radius=7, width=70,
                                             height=30, fg_color="#009900", hover_color="#008000",
                                             command=self.delete_transportadora)
        no_button = customtkinter.CTkButton(self, text="Não", corner_radius=7, width=70,
                                            height=30, fg_color="#ff1a1a", hover_color="#ff0000",
                                            command=self.fechar_janela)
        yes_button.pack(side='left', padx=40)
        no_button.pack(side='right', padx=40)

    def delete_transportadora(self):
        key = get_db(DbLink().PATHS['1'], find_key_by_name=choice[-1])
        delete_db(DbLink().PATHS['1']+'/'+key)

        self.destroy()

    def fechar_janela(self):
        self.destroy()


class BaixadoSucesso(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("200x130")
  

        # definir a posição da janela

        self.title("Aviso")
        self.label = customtkinter.CTkLabel(
            self, text="Baixado com Sucesso!")
        self.label.pack(padx=20, pady=20)

        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70,
                                            height=30, fg_color="#df8110", hover_color="#ce770f",
                                            command=self.fechar_janela)
        ok_button.pack(padx=5, pady=5)

    def fechar_janela(self):
        self.destroy()


class CadastroSucess(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x130")
        self.title("Aviso")
        self.label = customtkinter.CTkLabel(
            self, text="Cadastrado com Sucesso!")
        self.label.pack(padx=20, pady=20)

        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70,
                                            height=30, fg_color="#df8110", hover_color="#ce770f",
                                            command=self.fechar_janela)
        ok_button.pack(padx=5, pady=5)

    def fechar_janela(self):
        self.destroy()


class NaoEncontrado(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x130")
        self.title("Aviso")
        self.label = customtkinter.CTkLabel(self, text="Não Encontrado!")
        self.label.pack(padx=20, pady=20)

        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70,
                                            height=30, fg_color="#df8110", hover_color="#ce770f",
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

        ok_button = customtkinter.CTkButton(self, text="OK", corner_radius=7, width=70,
                                            height=30, fg_color="#df8110", hover_color="#ce770f",
                                            command=self.fechar_janela)
        ok_button.pack(padx=5, pady=5)

    def fechar_janela(self):
        self.destroy()


class App(customtkinter.CTk):

    def get_all_inputs(self, get=False):
        if get:
            all_inputs = [child.get() for child in self.main_frame.winfo_children(
            ) if isinstance(child, customtkinter.CTkEntry)]
        else:
            all_inputs = [child for child in self.main_frame.winfo_children(
            ) if isinstance(child, customtkinter.CTkEntry)]
        return all_inputs

    def convert_json(self, padrao_dados, inputs=[], *ignore):
        all_inputs = self.get_all_inputs(get=True)
        if len(inputs) > 0:
            all_inputs = inputs
        padrao_dados = [key for key in DbLink(
        ).PADRAO_DADOS[padrao_dados] if key not in ignore]
        data_json = {}
        for i in range(len(all_inputs)):
            data_json[padrao_dados[i]] = all_inputs[i]

        return data_json

    def clear_all_entries(self):
        for child in self.main_frame.winfo_children():
            if isinstance(child, customtkinter.CTkEntry):
                child.delete(0, tk.END)

    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        self.title("Calculadora de Frete")
        width = 900
        height = 570

        # obter as dimensões da tela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # calcular as coordenadas x e y da janela
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # definir a posição da janela
        self.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.resizable(False, False)

        self.cadastro_sucess = None
        self.cadastro_fail = None
        self.deletar_screen = None
        self.tabela_transportadora = None
        self.tabela_produto = None
        self.nao_encontrado = None

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

        self.trash_image = ImageTk.PhotoImage(Image.open(
            "images/trash.png").resize((15, 15)), Image.ANTIALIAS)

        self.search_image = ImageTk.PhotoImage(Image.open(
            "images/search.png").resize((15, 15)), Image.ANTIALIAS)

        self.painel = customtkinter.CTkFrame(
            self, height=550, width=180, fg_color="#262527")
        self.painel.grid(row=0, column=0)

        home_button = customtkinter.CTkButton(self.painel, text="Home", corner_radius=0, height=60,
                                              fg_color="#1a1a1a", hover_color="#272727", anchor="center", image=house_image, command=self.home_screen)

        label_transp = customtkinter.CTkLabel(
            self.painel, text="Transportadora", height=45)

        cadastrar_transp = customtkinter.CTkButton(self.painel, text="Cadastrar", corner_radius=0, height=60,
                                                   fg_color="#333333", hover_color="#272727", anchor="center", image=truck_image, command=self.cadastro_transportadora)

        editar_transp = customtkinter.CTkButton(self.painel, text="Editar", corner_radius=0,
                                                height=60, fg_color="#333333", hover_color="#272727", anchor="center", command=self.EditarTransportadoraScreen, image=pencil_image)

        visualizar_transp = customtkinter.CTkButton(
            self.painel, text="Visualizar", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=eye_image, anchor="center", command=self.VisualizarTranspScreen)

        produto_label = customtkinter.CTkLabel(
            self.painel, text="Produto", height=35)

        cadastrar_produto = customtkinter.CTkButton(
            self.painel, text="Cadastrar", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=bag_image, anchor="center", command=self.cadastro_produto_screen)

        editar_produto = customtkinter.CTkButton(self.painel, text="Editar", corner_radius=0,
                                                 height=50, fg_color="#333333", hover_color="#272727", image=pencil_image, anchor="center", command=self.editar_produto_screen)

        visualizar_produto = customtkinter.CTkButton(
            self.painel, text="Visualizar", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=eye_image, anchor="center", command=self.view_tabela_produto)

        calculo_label = customtkinter.CTkLabel(
            self.painel, text="Calculo Frete", height=35)

        calcular_frete = customtkinter.CTkButton(
            self.painel, text="Calcular", corner_radius=0, height=50, fg_color="#333333", hover_color="#272727", image=eye_image, anchor="center")

        home_button.pack()
        label_transp.pack()
        cadastrar_transp.pack()
        
        visualizar_transp.pack()
        editar_transp.pack()
        produto_label.pack()
        cadastrar_produto.pack()
        visualizar_produto.pack()
        editar_produto.pack()
        
        calculo_label.pack()
        calcular_frete.pack()
        

        self.main_frame = customtkinter.CTkFrame(
            self, width=700, height=450, fg_color='#313131')
        self.main_frame.grid(row=0, column=1, padx=15, pady=15, ipadx=10)
        self.main_frame.grid_propagate(False)

        self.main_frame.place(anchor='center', relx=0.58, rely=0.5)
        img = ImageTk.PhotoImage(Image.open(
            "images/home.png").resize((700, 450)))

        # Create a Label Widget to display the text or Image
        label = customtkinter.CTkLabel(self.main_frame, text='', image=img)
        label.pack()

    def home_screen(self):
        self.delete_pages()
        img = ImageTk.PhotoImage(Image.open(
            "images/home.png").resize((700, 450)))

        # Create a Label Widget to display the text or Image
        label = customtkinter.CTkLabel(self.main_frame, text='', image=img)
        label.pack()

    def editar_produto_screen(self):
        self.delete_pages()

        self.codigo_interno = customtkinter.CTkEntry(self.main_frame,
                                                     width=85,
                                                     height=25,
                                                     border_width=1,
                                                     corner_radius=1,
                                                     )
        self.descricao = customtkinter.CTkEntry(self.main_frame,
                                                width=200,
                                                height=25,
                                                border_width=1,
                                                corner_radius=1,
                                                )
        self.unidade = customtkinter.CTkEntry(self.main_frame,
                                              width=85,
                                              height=25,
                                              border_width=1,
                                              corner_radius=1,
                                              )
        self.valor_venda = customtkinter.CTkEntry(self.main_frame,
                                                  width=85,
                                                  height=25,
                                                  border_width=1,
                                                  corner_radius=1,
                                                  )
        self.peso = customtkinter.CTkEntry(self.main_frame,
                                           width=85,
                                           height=25,
                                           border_width=1,
                                           corner_radius=1,
                                           )
        self.comprimento = customtkinter.CTkEntry(self.main_frame,
                                                  width=85,
                                                  height=25,
                                                  border_width=1,
                                                  corner_radius=1,
                                                  )
        self.largura = customtkinter.CTkEntry(self.main_frame,
                                              width=85,
                                              height=25,
                                              border_width=1,
                                              corner_radius=1,
                                              )
        self.altura = customtkinter.CTkEntry(self.main_frame,
                                             width=85,
                                             height=25,
                                             border_width=1,
                                             corner_radius=1,
                                             )
        label_codigo = customtkinter.CTkLabel(
            self.main_frame,
            text="Código:"

        )
        label_descricao = customtkinter.CTkLabel(
            self.main_frame,
            text="Descrição:"

        )
        label_unidade = customtkinter.CTkLabel(
            self.main_frame,
            text="Unidade:"

        )
        label_valor_venda = customtkinter.CTkLabel(
            self.main_frame,
            text="Valor Venda:"

        )
        label_peso = customtkinter.CTkLabel(
            self.main_frame,
            text="Peso:"

        )
        label_comprimento = customtkinter.CTkLabel(
            self.main_frame,
            text="Comprimento:"

        )
        label_largura = customtkinter.CTkLabel(
            self.main_frame,
            text="largura:"

        )
        label_altura = customtkinter.CTkLabel(
            self.main_frame,
            text="Altura:"
        )

        label_codigo.grid(row=0, column=2, pady=20, padx=30)
        label_descricao.grid(row=3, column=2, pady=20, padx=30)
        label_unidade.grid(row=1, column=2, pady=20, padx=30)
        label_valor_venda.grid(row=2, column=2, pady=20, padx=30)
        label_peso.grid(row=0, column=4, pady=20, padx=30)
        label_comprimento.grid(row=1, column=4, pady=20, padx=30)
        label_largura.grid(row=2, column=4, pady=20, padx=30)
        label_altura.grid(row=3, column=4, pady=20, padx=30)

        self.codigo_interno.grid(row=0, column=3, pady=20)
        self.descricao.grid(row=3, column=3, pady=20)
        self.unidade.grid(row=1, column=3, pady=20)
        self.valor_venda.grid(row=2, column=3, pady=20)
        self.peso.grid(row=0, column=5, pady=20)
        self.comprimento.grid(row=1, column=5, pady=20)
        self.largura.grid(row=2, column=5, pady=20)
        self.altura.grid(row=3, column=5, pady=20)

        button_atualizar = customtkinter.CTkButton(self.main_frame, text="Atualizar", corner_radius=7,
                                                   height=30,  width=100, fg_color="#3d9336", hover_color="#51bc48", command=self.atualizar_produto)
        button_atualizar.grid(row=4, column=5, pady=20)

        button_cada = customtkinter.CTkButton(self.main_frame, image=self.search_image, text="", corner_radius=7,
                                              height=30,  width=20, fg_color="#808080", hover_color="#666666", command=self.is_product_exists)
        button_cada.grid(row=0, column=1, padx=20)

    def atualizar_produto(self):
        inputs = self.get_all_inputs(get=True)
        dict = self.convert_json(1, inputs[1:], 'ID', 'codigo interno')

        text = self.codigo_interno.get()
        name_key = find_key_by_code(
            DbLink().PATHS['2'], int(text))
        try:

            patch_db(DbLink().PATHS['2']+'/'+name_key, dict)
            self.clear_all_entries()

            if self.cadastro_sucess is None or not self.cadastro_sucess.winfo_exists():
                # create window if its None or destroyed
                self.cadastro_sucess = CadastroSucess(self)
            else:
                self.cadastro_fail.focus()
        except:
            if self.cadastro_fail is None or not self.cadastro_fail.winfo_exists():
                # create window if its None or destroyed
                self.cadastro_fail = CadastroFail(self)
            else:
                self.cadastro_fail.focus()

    def is_product_exists(self):
        texto = self.codigo_interno.get()
        dados_json = get_db(DbLink().PATHS['2'])
        dados_list = [dados_json[item] for item in dados_json]
        all_entries = self.get_all_inputs()
        padrao = [item for item in DbLink().PADRAO_DADOS[1]
                  if item not in ['ID']]
        achou = 0
        for item in dados_list:
            if int(texto) == item['codigo interno']:
                self.clear_all_entries()
                achou += 1
                for i in range(len(all_entries)):
                    all_entries[i].insert(0, item[padrao[i]])

        if achou == 0:
            self.clear_all_entries()
            if self.nao_encontrado is None or not self.nao_encontrado.winfo_exists():
                # create window if its None or destroyed
                self.nao_encontrado = NaoEncontrado(self)
            else:
                self.nao_encontrado.focus()  # if window exists focus it

    def view_tabela_produto(self):
        if self.tabela_produto is None or not self.tabela_produto.winfo_exists():
            # create window if its None or destroyed
            self.tabela_produto = TabelaProdutos(self)
        else:
            self.tabela_produto.focus()  # if window exists focus it

    def cadastro_produto_screen(self):
        self.delete_pages()

        self.codigo_interno = customtkinter.CTkEntry(self.main_frame,
                                                     width=85,
                                                     height=25,
                                                     border_width=1,
                                                     corner_radius=1,
                                                     )
        self.descricao = customtkinter.CTkEntry(self.main_frame,
                                                width=200,
                                                height=25,
                                                border_width=1,
                                                corner_radius=1,
                                                )
        self.unidade = customtkinter.CTkEntry(self.main_frame,
                                              width=85,
                                              height=25,
                                              border_width=1,
                                              corner_radius=1,
                                              )
        self.valor_venda = customtkinter.CTkEntry(self.main_frame,
                                                  width=85,
                                                  height=25,
                                                  border_width=1,
                                                  corner_radius=1,
                                                  )
        self.peso = customtkinter.CTkEntry(self.main_frame,
                                           width=85,
                                           height=25,
                                           border_width=1,
                                           corner_radius=1,
                                           )
        self.comprimento = customtkinter.CTkEntry(self.main_frame,
                                                  width=85,
                                                  height=25,
                                                  border_width=1,
                                                  corner_radius=1,
                                                  )
        self.largura = customtkinter.CTkEntry(self.main_frame,
                                              width=85,
                                              height=25,
                                              border_width=1,
                                              corner_radius=1,
                                              )
        self.altura = customtkinter.CTkEntry(self.main_frame,
                                             width=85,
                                             height=25,
                                             border_width=1,
                                             corner_radius=1,
                                             )
        label_codigo = customtkinter.CTkLabel(
            self.main_frame,
            text="Código:"

        )
        label_descricao = customtkinter.CTkLabel(
            self.main_frame,
            text="Descrição:"

        )
        label_unidade = customtkinter.CTkLabel(
            self.main_frame,
            text="Unidade:"

        )
        label_valor_venda = customtkinter.CTkLabel(
            self.main_frame,
            text="Valor Venda:"

        )
        label_peso = customtkinter.CTkLabel(
            self.main_frame,
            text="Peso:"

        )
        label_comprimento = customtkinter.CTkLabel(
            self.main_frame,
            text="Comprimento:"

        )
        label_largura = customtkinter.CTkLabel(
            self.main_frame,
            text="largura:"

        )
        label_altura = customtkinter.CTkLabel(
            self.main_frame,
            text="Altura:"
        )

        label_codigo.grid(row=0, column=2, pady=20, padx=30)
        label_descricao.grid(row=3, column=2, pady=20, padx=30)
        label_unidade.grid(row=1, column=2, pady=20, padx=30)
        label_valor_venda.grid(row=2, column=2, pady=20, padx=30)
        label_peso.grid(row=0, column=4, pady=20, padx=30)
        label_comprimento.grid(row=1, column=4, pady=20, padx=30)
        label_largura.grid(row=2, column=4, pady=20, padx=30)
        label_altura.grid(row=3, column=4, pady=20, padx=30)

        self.codigo_interno.grid(row=0, column=3, pady=20)
        self.descricao.grid(row=3, column=3, pady=20)
        self.unidade.grid(row=1, column=3, pady=20)
        self.valor_venda.grid(row=2, column=3, pady=20)
        self.peso.grid(row=0, column=5, pady=20)
        self.comprimento.grid(row=1, column=5, pady=20)
        self.largura.grid(row=2, column=5, pady=20)
        self.altura.grid(row=3, column=5, pady=20)

        button_cadastrar = customtkinter.CTkButton(self.main_frame, text="Cadastrar", corner_radius=7,
                                                   height=30,  width=100, fg_color="#3d9336", hover_color="#51bc48", command=self.cadastrar_produto)
        button_cadastrar.grid(row=4, column=5, pady=20)

        button_importar = customtkinter.CTkButton(self.main_frame, text="Importar", corner_radius=7,
                                                  height=30,  width=100, fg_color="#df8110", hover_color="#ce770f", command=self.importar_dados_produto)
        button_importar.grid(row=4, column=2, pady=20, padx=30)

    def cadastrar_produto(self):
        try:
            all_entries, padrao_dados, data_json = self.get_all_inputs(
                get=True), [key for key in DbLink().PADRAO_DADOS[1].keys()], {}
            for i in range(len(all_entries)):
                data_json[padrao_dados[i+1]] = all_entries[i]
            data_json['ID'] = get_db(DbLink().PATHS['2'], last=True)
            post_db(DbLink().PATHS['2'], data_json)

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

    def importar_dados_produto(self):
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("Arquivos de excel", "*.xlsx")])

            upload_massivo_db(file_path, 1, DbLink().PATHS['2'])

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

    def VisualizarTranspScreen(self):

        if self.tabela_transportadora is None or not self.tabela_transportadora.winfo_exists():
            # create window if its None or destroyed
            self.tabela_transportadora = TabelaTransportadora(self)
        else:
            self.tabela_transportadora.focus()

    def EditarTransportadoraScreen(self):
        self.delete_pages()

        def optionmenu_callback(choice):
            self.clear_all_entries()
            self.choice = choice
            padrao_dados, json_dados = DbLink().PADRAO_DADOS[0], get_db(DbLink().PATHS['1'])[
                get_db(DbLink().PATHS['1'], find_key_by_name=self.choice)]
            for i in padrao_dados:
                padrao_dados[i] = json_dados[i]
            ordem_dados = [
                [item for chave, item in padrao_dados.items() if chave not in [
                    'ID', 'nome']],
                [i for i in self.get_all_inputs()]
            ]
            for i in range(len(ordem_dados[1])):
                ordem_dados[1][i].insert(0, ordem_dados[0][i])
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

        button_apagar = customtkinter.CTkButton(self.main_frame, text="Deletar", corner_radius=7,
                                                height=30, text_color='black',  width=100, fg_color="#ff1a1a", hover_color="#ff0000", command=self.deletar_transportadora, image=self.trash_image)
        button_apagar.grid(row=6, column=0, pady=20, padx=20)

    def deletar_transportadora(self):
        try:
            choice.append(self.choice)
            if self.deletar_screen is None or not self.deletar_screen.winfo_exists():
                # create window if its None or destroyed
                self.deletar_screen = DeleterTransportadora(self)
            else:
                self.deletar_screen.focus()
            self.clear_all_entries()
        except:
            if self.cadastro_fail is None or not self.cadastro_fail.winfo_exists():
                # create window if its None or destroyed
                self.cadastro_fail = CadastroFail(self)
            else:
                self.cadastro_fail.focus()

    def atualizar_transportadora(self):
        try:
            name_key = get_db(
                DbLink().PATHS['1'], find_key_by_name=self.choice)

            patch_db(DbLink().PATHS['1']+'/'+name_key,
                     self.convert_json(0, 'ID', 'nome'))
            self.clear_all_entries()
            self.nome_.set('-')
            if self.cadastro_sucess is None or not self.cadastro_sucess.winfo_exists():
                # create window if its None or destroyed
                self.cadastro_sucess = CadastroSucess(self)
            else:
                self.cadastro_fail.focus()
        except:
            if self.cadastro_fail is None or not self.cadastro_fail.winfo_exists():
                # create window if its None or destroyed
                self.cadastro_fail = CadastroFail(self)
            else:
                self.cadastro_fail.focus()

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
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("Arquivos de excel", "*.xlsx")])

            upload_massivo_db(file_path, 0, DbLink().PATHS['1'])
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

    def cadastrar_transportadora(self):

        try:
            all_entries, padrao_dados, data_json = self.get_all_inputs(
                get=True), [key for key in DbLink().PADRAO_DADOS[0].keys()], {}
            for i in range(len(all_entries)):
                data_json[padrao_dados[i+1]] = all_entries[i]
            data_json['ID'] = get_db(DbLink().PATHS['1'], last=True)
            post_db(DbLink().PATHS['1'], data_json)

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
