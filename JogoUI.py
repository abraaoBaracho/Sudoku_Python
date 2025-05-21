import tkinter as tk
from Jogo import Jogo
from GameOver import GameOver

class JogoUI:
    def __init__(self, menu_janela, nivel):
        self.menu_janela = menu_janela
        self.menu_janela.withdraw()  # Oculta o menu
        self.nivel = nivel
        self.jogo = Jogo(nivel)
        self.tempo_decorrido = 0
        self.erros = 0
        self.jogo_encerrado = False

        self.janela = tk.Toplevel(self.menu_janela)  # Janela do jogo
        self.janela.title(f"Sudoku - Nível {nivel}")
        self.janela.attributes("-fullscreen", True)
        self.janela.bind("<Escape>", lambda e: self.janela.attributes("-fullscreen", False))
        self.janela.configure(bg="#2D3332")

        self.label_tempo = None
        self.criar_interface()
        self.atualizar_tempo()

    def criar_interface(self):
        self.grade = []
        frame_tabuleiro = tk.Frame(self.janela, bg="#2D3332")
        frame_tabuleiro.place(relx=0.5, rely=0.4, anchor='center')

        frame_topo = tk.Frame(self.janela, bg="#2D3332")
        frame_topo.place(relx=0.5, rely=0.05, anchor='n')

        tk.Label(
            frame_topo,
            text=f"Sudoku - Nível {self.nivel}",
            font=("Arial", 32, "bold"),
            bg="#2D3332",
            fg="white"
        ).pack(side="left", padx=20)

        self.label_tempo = tk.Label(
            frame_topo,
            text="Tempo: 00:00",
            font=("Arial", 16),
            bg="#2D3332",
            fg="#0DFAE3"
        )
        self.label_tempo.pack(side="left", padx=40)

        for i in range(9):
            linha = []
            for j in range(9):
                valor = self.jogo.tabuleiro[i][j]
                frame = tk.Frame(frame_tabuleiro)
                frame.grid(
                    row=i, column=j,
                    padx=(4 if j % 3 == 0 else 1, 4 if j == 8 else 0),
                    pady=(4 if i % 3 == 0 else 1, 4 if i == 8 else 0)
                )

                vcmd = (self.janela.register(lambda P: P.isdigit() and 1 <= int(P) <= 9 if P else True), "%P")
                entrada = tk.Entry(
                    frame,
                    width=3,
                    bg="#3FA59B",
                    font=("Arial", 24),
                    justify='center',
                    relief="flat",
                    validate="key",
                    validatecommand=vcmd
                )
                entrada.pack()

                entrada.bind("<FocusOut>", lambda e, i=i, j=j: self.verificar_erro(e.widget.get(), i, j))

                if valor != 0:
                    entrada.insert(0, str(valor))
                    entrada.config(state="disabled", disabledforeground="black")

                linha.append(entrada)
            self.grade.append(linha)

        self.label_erros = tk.Label(
            self.janela,
            text="Erros: 0/3",
            font=("Arial", 16),
            bg="#2D3332",
            fg="red"
        )
        self.label_erros.place(relx=0.5, rely=0.75, anchor="center")

        frame_botoes = tk.Frame(self.janela, bg="#2D3332")
        frame_botoes.place(relx=0.5, rely=0.88, anchor='center')

        tk.Button(frame_botoes, text="Mostrar Solução", font=("Arial", 14), command=self.mostrar_solucao).pack(side="left", padx=10)
        tk.Button(frame_botoes, text="Voltar ao Menu", font=("Arial", 14), command=self.voltar_menu,
                  bg="#FF5733", fg="white", activebackground="#C70039").pack(side="left", padx=10)
        tk.Button(frame_botoes, text="Resetar Jogo", font=("Arial", 14), command=self.resetar_jogo,
                  bg="#FF5733", fg="white", activebackground="#C70039").pack(side="left", padx=10)

    def mostrar_solucao(self):
        for i in range(9):
            for j in range(9):
                self.grade[i][j].config(state="normal")
                self.grade[i][j].delete(0, tk.END)
                self.grade[i][j].insert(0, str(self.jogo.tabuleiro_preenchido[i][j]))
                self.grade[i][j].config(state="disabled")

    def voltar_menu(self):
        self.janela.destroy()
        self.menu_janela.deiconify()

    def resetar_jogo(self):
        self.jogo = Jogo(self.nivel)
        for i in range(9):
            for j in range(9):
                self.grade[i][j].config(state="normal")
                self.grade[i][j].delete(0, tk.END)
                valor = self.jogo.tabuleiro[i][j]
                if valor != 0:
                    self.grade[i][j].insert(0, str(valor))
                    self.grade[i][j].config(state="disabled", disabledforeground="black")

    def atualizar_tempo(self):
        minutos = self.tempo_decorrido // 60
        segundos = self.tempo_decorrido % 60
        self.label_tempo.config(text=f"Tempo: {minutos:02}:{segundos:02}")
        self.tempo_decorrido += 1
        self.janela.after(1000, self.atualizar_tempo)

    def verificar_erro(self, valor, i, j):
        entrada = self.grade[i][j]
        if valor == "":
            entrada.config(fg="black")
            return

        if int(valor) != self.jogo.tabuleiro_preenchido[i][j]:
            self.erros += 1
            self.label_erros.config(text=f"Erros: {self.erros}/3")
            entrada.config(fg="red")
        else:
            entrada.config(fg="white")

        if self.erros >= 3 and not self.jogo_encerrado:
            self.jogo_encerrado = True
            self.janela.destroy()
            GameOver(self.menu_janela, "derrota", self.nivel)

        elif self.verificar_vitoria() and not self.jogo_encerrado:
            self.jogo_encerrado = True
            self.janela.destroy()
            GameOver(self.menu_janela, "vitoria", self.nivel)

    def verificar_vitoria(self):
        for i in range(9):
            for j in range(9):
                valor = self.grade[i][j].get()
                if not valor.isdigit() or int(valor) != self.jogo.tabuleiro_preenchido[i][j]:
                    return False
        return True
