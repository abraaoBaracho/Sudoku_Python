import random

TAMANHO = 9

dificuldades = {
        'Fácil': 40,
        'Médio': 30,
        'Difícil': 25,
        'Muito Difícil': 20,
        'Extremo': 15
    }

def numero_valido(tabuleiro, linha, coluna, numero):
    # Verifica linha
    if numero in tabuleiro[linha]:
        return False
    # Verifica coluna
    for i in range(TAMANHO):
        if tabuleiro[i][coluna] == numero:
            return False
    # Verifica bloco 3x3
    bloco_linha = (linha // 3) * 3
    bloco_coluna = (coluna // 3) * 3
    for i in range(3):
        for j in range(3):
            if tabuleiro[bloco_linha + i][bloco_coluna + j] == numero:
                return False
    return True

def gerar_tabuleiro(nivel, tentativas_max=5):
    numeros_iniciais = dificuldades[nivel]

    while True:  # laço principal: tenta até conseguir um tabuleiro válido
        for tentativa in range(tentativas_max):
            # Etapa 1: Gera tabuleiro completo
            tabuleiro = [[0 for _ in range(9)] for _ in range(9)]
            preencher_tabuleiro(tabuleiro)

            # Etapa 2: Tenta remover mantendo uma única solução
            posicoes = [(i, j) for i in range(9) for j in range(9)]
            random.shuffle(posicoes)
            removidos = 0

            while removidos < (81 - numeros_iniciais) and posicoes:
                i, j = posicoes.pop()
                temp = tabuleiro[i][j]
                tabuleiro[i][j] = 0
                if contar_solucoes(tabuleiro) != 1:
                    tabuleiro[i][j] = temp  # desfaz
                else:
                    removidos += 1

            if removidos == (81 - numeros_iniciais):
                return tabuleiro  # conseguiu com sucesso!

            print(f"Tentativa {tentativa + 1} falhou. Tentando novamente...")

        print("Falhou 5 vezes. Gerando novo tabuleiro base e reiniciando...")


def contar_solucoes(tabuleiro, limite=2):
    contador = [0]

    def resolver(tab):
        if contador[0] >= limite:
            return
        for linha in range(TAMANHO):
            for coluna in range(TAMANHO):
                if tab[linha][coluna] == 0:
                    for numero in range(1, 10):
                        if numero_valido(tab, linha, coluna, numero):
                            tab[linha][coluna] = numero
                            resolver(tab)
                            tab[linha][coluna] = 0
                    return
        contador[0] += 1

    resolver([linha[:] for linha in tabuleiro])
    return contador[0]

def preencher_tabuleiro(tabuleiro):
    for i in range(TAMANHO):
        for j in range(TAMANHO):
            if tabuleiro[i][j] == 0:
                numeros = list(range(1, 10))
                random.shuffle(numeros)
                for numero in numeros:
                    if numero_valido(tabuleiro, i, j, numero):
                        tabuleiro[i][j] = numero
                        if preencher_tabuleiro(tabuleiro):
                            return True
                        tabuleiro[i][j] = 0
                return False
    return True

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(str(num) if num != 0 else "." for num in linha))
    print()




tabuleiro_teste = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 9, 0, 7, 0],
    [0, 0, 0, 8, 0, 0, 4, 3, 0],
    [0, 5, 0, 1, 3, 2, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 1, 0, 0, 4, 0, 0, 0],
    [0, 8, 6, 0, 0, 0, 1, 9, 0],
    [0, 0, 4, 0, 0, 5, 0, 0, 0],
    [0, 0, 9, 0, 0, 3, 0, 0, 0],
]

print("Soluções encontradas:", contar_solucoes(tabuleiro_teste))
