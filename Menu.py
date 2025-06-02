import tkinter as tk
from PIL import Image, ImageTk
from JogoUI import JogoUI

class Menu:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sudoku - Menu Inicial")
        self.janela.attributes("-fullscreen", True)
        self.janela.bind("<Escape>", lambda e: self.janela.attributes("-fullscreen", False))
        self.janela.configure(bg="#2D3332")

        # Imagem de capa
        try:
            imagem_original = Image.open("img/sudoku.png")  # caminho da imagem
            imagem_redimensionada = imagem_original.resize((600, 400))
            self.imagem = ImageTk.PhotoImage(imagem_redimensionada)
            self.label_imagem = tk.Label(self.janela, image=self.imagem, bg="#BEC3C2")
            self.label_imagem.pack(pady=10)
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")

        # Título
        self.titulo = tk.Label(self.janela, text="Escolha o Nível", font=("Arial", 24), bg="#2D3332", fg="white")
        self.titulo.pack(pady=10)

        # Lista de níveis
        niveis = ["Fácil", "Médio", "Difícil", "Muito Difícil", "Extremo"]
        for nivel in niveis:
            tk.Button(
                self.janela,
                text=nivel,
                font=("Arial", 20),
                bg="#2D3332",
                fg="white",
                activebackground="#437A75",
                activeforeground="white",
                bd=0,
                width=20,
                height=2,
                command=lambda n=nivel: self.iniciar_jogo(n)
            ).pack(pady=5)

        # Botão para sair
        tk.Button(
            self.janela,
            text="Sair",
            font=("Arial", 20),
            bg="#2D3332",
            fg="white",
            activebackground="#437A75",
            activeforeground="white",
            bd=0,
            width=20,
            height=2,
            command=self.janela.quit
        ).pack(pady=5)

    def iniciar_jogo(self, nivel):
        # Oculta o menu e abre o jogo em uma Toplevel
        JogoUI(self.janela, nivel)

