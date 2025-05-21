import random
import logging

logging.basicConfig(level=logging.INFO)

TAMANHO = 9

dificuldades = {
    'Fácil': 40,
    'Médio': 30,
    'Difícil': 25,
    'Muito Difícil': 24,
    'Extremo': 23
}

class Jogo:
    def __init__(self, nivel):
        self.nivel = nivel
        self.tabuleiro = [[0 for _ in range(TAMANHO)] for _ in range(TAMANHO)]
        self.gerar_tabuleiro(nivel)

    def numero_valido(self, linha, coluna, numero, tab):
        # Verifica linha
        if numero in tab[linha]:
            return False
        # Verifica coluna
        for i in range(TAMANHO):
            if tab[i][coluna] == numero:
                return False
        # Verifica bloco 3x3
        bloco_linha = (linha // 3) * 3
        bloco_coluna = (coluna // 3) * 3
        for i in range(3):
            for j in range(3):
                if tab[bloco_linha + i][bloco_coluna + j] == numero:
                    return False
        return True

    def gerar_tabuleiro(self, nivel, tentativas_max=5):
        numeros_iniciais = dificuldades[nivel]
        max_tentativas_gerais = 10
        tentativa_geral = 0

        while tentativa_geral < max_tentativas_gerais:  # tenta várias vezes gerar um tabuleiro válido
            tentativa_geral += 1
            for tentativa in range(tentativas_max):
                # Etapa 1: Gera tabuleiro completo
                self.tabuleiro = [[0 for _ in range(TAMANHO)] for _ in range(TAMANHO)]
                if not self.preencher_tabuleiro():
                    continue

                # Salva uma cópia do tabuleiro preenchido
                self.tabuleiro_preenchido = [linha[:] for linha in self.tabuleiro]

                # Etapa 2: Tenta remover mantendo uma única solução
                posicoes = [(i, j) for i in range(TAMANHO) for j in range(TAMANHO)]
                random.shuffle(posicoes)
                removidos = 0

                while removidos < (81 - numeros_iniciais) and posicoes:
                    i, j = posicoes.pop()
                    temp = self.tabuleiro[i][j]
                    self.tabuleiro[i][j] = 0
                    if self.contar_solucoes() != 1:
                        self.tabuleiro[i][j] = temp  # desfaz
                    else:
                        removidos += 1

                if removidos == (81 - numeros_iniciais):
                    return  # conseguiu com sucesso!

                logging.warning(f"Tentativa {tentativa + 1} falhou. Tentando novamente...")

            logging.error("Falhou 3 vezes. Gerando novo tabuleiro base e reiniciando...")

        raise Exception("Falha ao gerar um tabuleiro válido após várias tentativas.")

    def contar_solucoes(self, limite=2):
        contador = [0]

        def resolver(tab):
            if contador[0] >= limite:
                return
            for linha in range(TAMANHO):
                for coluna in range(TAMANHO):
                    if tab[linha][coluna] == 0:
                        for numero in range(1, 10):
                            if self.numero_valido(linha, coluna, numero, tab):
                                tab[linha][coluna] = numero
                                resolver(tab)
                                tab[linha][coluna] = 0
                        return
            contador[0] += 1

        resolver([linha[:] for linha in self.tabuleiro])
        return contador[0]

    def preencher_tabuleiro(self):
        for i in range(TAMANHO):
            for j in range(TAMANHO):
                if self.tabuleiro[i][j] == 0:
                    numeros = list(range(1, 10))
                    random.shuffle(numeros)
                    for numero in numeros:
                        if self.numero_valido(i, j, numero, self.tabuleiro):
                            self.tabuleiro[i][j] = numero
                            if self.preencher_tabuleiro():
                                return True
                            self.tabuleiro[i][j] = 0
                    return False
        return True

    def imprimir_tabuleiro(self):
        for linha in self.tabuleiro:
            print(" ".join(str(num) if num != 0 else "." for num in linha))
        print()

    def verificar_erro(self, n, i, j):
    
        if not hasattr(self, 'tabuleiro_preenchido'):
            raise ValueError("O tabuleiro preenchido ainda não foi gerado.")
        
        return self.tabuleiro_preenchido[i][j] == n

