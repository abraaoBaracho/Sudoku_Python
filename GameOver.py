import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

dificuldades = {
    'Fácil': 1,
    'Médio': 2,
    'Difícil': 3,
    'Muito Difícil': 4,
    'Extremo': 5
}

class GameOver:
    def __init__(self, menu_janela, resultado, nivel):
        self.menu_janela = menu_janela
        self.janela = tk.Toplevel(self.menu_janela)
        self.janela.title("Fim de Jogo")
        self.janela.attributes("-fullscreen", True)
        self.janela.configure(bg="#2D3332")
        self.janela.bind("<Escape>", lambda e: self.janela.attributes("-fullscreen", False))

        texto = "Você Venceu!" if resultado == "vitoria" else "Você Perdeu!"
        cor = "#0DFAE3" if resultado == "vitoria" else "red"

        tk.Label(
            self.janela,
            text=texto,
            font=("Arial", 48, "bold"),
            bg="#2D3332",
            fg=cor
        ).pack(pady=60)

        gif_path = "img/win.gif" if resultado == "vitoria" else "img/lose.gif"
        self.carregar_gif(gif_path)

        if resultado == "vitoria":
            tk.Button(
                self.janela,
                text="Próximo Nível",
                font=("Arial", 20),
                command=lambda: self.proximo_nivel(nivel),
                bg="#FF5733",
                fg="white",
                activebackground="#C70039",
                activeforeground="white",
                width=20,
                height=2
            ).pack(pady=10)
        else:
            tk.Button(
                self.janela,
                text="Jogar Novamente",
                font=("Arial", 20),
                command=lambda: self.jogar_novamente(nivel),
                bg="#FF5733",
                fg="white",
                activebackground="#C70039",
                activeforeground="white",
                width=20,
                height=2
            ).pack(pady=10)

        tk.Button(
            self.janela,
            text="Voltar ao Menu",
            font=("Arial", 20),
            command=self.voltar_menu,
            bg="#FF5733",
            fg="white",
            activebackground="#C70039",
            activeforeground="white",
            width=20,
            height=2
        ).pack(pady=10)

        tk.Button(
            self.janela,
            text="Sair do Jogo",
            font=("Arial", 20),
            command=self.sair_jogo,
            bg="#555",
            fg="white",
            width=20,
            height=2
        ).pack(pady=10)

    def carregar_gif(self, caminho):
        self.frames = []
        try:
            gif = Image.open(caminho)
            for frame in ImageSequence.Iterator(gif):
                frame = frame.resize((400, 400))
                self.frames.append(ImageTk.PhotoImage(frame))

            self.gif_index = 0
            self.label_gif = tk.Label(self.janela, bg="#2D3332")
            self.label_gif.pack()
            self.atualizar_gif()
        except Exception as e:
            print(f"Erro ao carregar GIF: {e}")

    def atualizar_gif(self):
        if self.frames:
            frame = self.frames[self.gif_index]
            self.label_gif.config(image=frame)
            self.gif_index = (self.gif_index + 1) % len(self.frames)
            self.janela.after(80, self.atualizar_gif)

    def voltar_menu(self):
        self.janela.destroy()
        self.menu_janela.deiconify()

    def proximo_nivel(self, nivel):
        chaves = list(dificuldades.keys())
        indice = chaves.index(nivel) + 1
        if indice >= len(chaves):
            proximo_nivel = nivel
        else:
            proximo_nivel = chaves[indice]

        self.janela.destroy()
        self.menu_janela.deiconify()
        from JogoUI import JogoUI
        nova_janela = tk.Toplevel(self.menu_janela)
        JogoUI(nova_janela, proximo_nivel)

    def jogar_novamente(self, nivel):
        self.janela.destroy()
        self.menu_janela.deiconify()
        from JogoUI import JogoUI
        nova_janela = tk.Toplevel(self.menu_janela)
        JogoUI(nova_janela, nivel)

    def sair_jogo(self):
        self.janela.quit()
        self.janela.destroy()