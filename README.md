# Sudoku - Projeto da Disciplina Lógica de Programação

Este projeto é um jogo de Sudoku desenvolvido para a disciplina **Lógica de Programação** do curso de **Análise e Desenvolvimento de Sistemas (ADS)**. 

O jogo foi implementado em Python utilizando a biblioteca Tkinter para a interface gráfica, e possui diferentes níveis de dificuldade, sistema de erros, tempo e uma tela de fim de jogo.

---

## Sobre o Projeto

- Desenvolvido para praticar lógica de programação, manipulação de interfaces gráficas e estruturação de código orientado a objetos.
- Implementa funcionalidades como verificação de erros, limite de tentativas, controle de tempo e navegação entre diferentes telas (menu, jogo e fim de jogo).
- Possui níveis de dificuldade: Fácil, Médio, Difícil, Muito Difícil e Extremo.
- Exibe uma mensagem de vitória ou derrota ao final do jogo.

---

## Como Jogar

1. **Inicie o jogo** executando o arquivo principal (`Main.py`).
2. **Escolha a dificuldade** no menu inicial.
3. A janela do jogo será aberta mostrando um tabuleiro 9x9 de Sudoku.
4. Preencha as células vazias com números de 1 a 9, respeitando as regras do Sudoku:
   - Cada número deve aparecer apenas uma vez em cada linha, coluna e região 3x3.
5. Você pode:
   - **Mostrar solução:** para ver o tabuleiro completo preenchido corretamente.
   - **Resetar jogo:** para começar o tabuleiro atual novamente.
   - **Voltar ao menu:** para retornar à tela inicial e escolher outro nível.
6. Cuidado com os erros: você pode errar até 3 vezes. Ao atingir o limite, o jogo termina.
7. Complete o tabuleiro corretamente para vencer o jogo.
8. Na tela de fim de jogo, você pode escolher:
   - Jogar novamente no mesmo nível,
   - Passar para o próximo nível (se tiver vencido),
   - Voltar ao menu principal,
   - Ou sair do jogo.

---

## Requisitos

- Python 3.x
- Biblioteca Pillow (PIL) para exibir gifs animados
- Tkinter (geralmente já vem instalado com o Python)

Para instalar a biblioteca Pillow, execute:

```bash
pip install pillow
