from Frames.FramesDependences import *

class Home(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Imagem da tela inicial
        img = ImageTk.PhotoImage(Image.open(
            "images/home.png").resize((700, 480)))
        label = customtkinter.CTkLabel(self, text='', image=img)
        label.pack()