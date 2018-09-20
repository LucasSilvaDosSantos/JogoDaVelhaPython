# ------------------/-------------------#
# Jogo da velha versão 1.0 sem OO       #
# 19/09/2018                            #
# Lucas Silva Dos Santos                #
# santos94us@hotmail.com / @gmail.com   #
# -----------------/--------------------#


# Exibição do tabuleiro para o jogo
def tabuleiro(t):
    print(f'+---+---+---+\n'
          f'| {t[0]} | {t[1]} | {t[2]} |\n'
          f'+---+---+---+\n'
          f'| {t[3]} | {t[4]} | {t[5]} |\n'
          f'+---+---+---+\n'
          f'| {t[6]} | {t[7]} | {t[8]} |\n'
          f'+---+---+---+\n')


# Validação da jogada e chamada da mudança de jogador
def jogada(j):
    pos = int(input('Escolha uma possição para jogar: '))
    if (pos < 1) or (pos > 9) or t[pos - 1] == 'X' or t[pos - 1] == 'O':
        print('Jogada Invalida, jogue novamente')
        return j
    else:
        # Mudança de t para nova rodada
        t[pos - 1] = j
        j = mudaJogador(j)
        tabuleiro(t)
        return j


# Função responsavel pela mudança do jogador
def mudaJogador(jogador):
    if jogador == 'X':
        return 'O'
    else:
        return 'X'


def vitoria():
    ganhador = 'N'
    if t[0] == t[1] == t[2]:  # Linha 1 Coluna 1,2,3
        if t[0] == 'X':
            ganhador = 'X'  # 123 tabela
        elif t[0] == 'O':
            ganhador = 'O'  # 123 tabela

    elif t[3] == t[4] == t[5]:  # Linha 2 Coluna 1,2,3
        if t[3] == 'X':
            ganhador = 'X'  # 456 tabela
        elif t[3] == 'O':
            ganhador = 'O'

    elif t[6] == t[7] == t[8]:  # Linha 3 Coluna 1,2,3
        if t[6] == 'X':
            ganhador = 'X'  # 789 tabela
        elif t[6] == 'O':
            ganhador = 'O'  # 789 tabela

    elif t[0] == t[3] == t[6]:  # Linhas 1,2,3 Coluna 1
        if t[0] == 'X':
            ganhador = 'X'  # 147 tabela
        elif t[0] == 'O':
            ganhador = 'O'  # 147 tabela

    elif t[1] == t[4] == t[7]:  # Linha 1,2,3 Coluna 2
        if t[1] == 'X':
            ganhador = 'X'  # 258 tabela
        elif t[1] == 'O':
            ganhador = 'O'  # 258 tabela

    elif t[2] == t[5] == t[8]:  # Linha 1,2,3 Coluna 3
        if t[2] == 'X':
            ganhador = 'X'  # 369 tabela
        elif t[2] == 'O':
            ganhador = 'O'  # 369 tabela

    elif t[0] == t[4] == t[8]:  # Linha 1,2,3 Coluna 1,2,3
        if t[0] == 'X':
            ganhador = 'X'  # 159 tabela
        elif t[0] == 'O':
            ganhador = 'O'  # 159 tabela

    elif (t[2] == t[4] == t[6]) == 'X':  # Linha 1,2,3 Coluna 1,2,3
        if t[2] == 'X':
            ganhador = 'X'  # 357 tabela
        elif t[2] == 'O':
            ganhador = 'O'  # 357 tabela

    return ganhador


# Possiçoes iniciais no tabuleiro
t = [1, 2, 3, 4, 5, 6, 7, 8, 9]

tabuleiro(t)

jogador = 'O'  # Quem começa o jogo

while True:
    if jogador == 'O':
        print('Vez do O')
        jogador = jogada('O')
    else:
        print('Vez do X')
        jogador = jogada('X')
    fim_de_jogo = vitoria()
    if (fim_de_jogo == 'X') or (fim_de_jogo == 'O'):
        print(f'Fim da partida o ganhador foi {fim_de_jogo}!')
        break
