'''
 ---------Jogo de adivinhação de número.-------

 As regras são bastante simples. Vamos a elas :

 - O jogador deverá escolher um número qualquer entre 0 e 50;

 - O jogador receberá dicas se seu chute está acima ou abaixo do valor oculto gerado
 pelo computador de maneira aleatória, caso não acerte de primeiro o número ;

 - O jogador terá 10 tetntativas para adivinhar qual foi o número oculto gerado
 pelo computador entre  intervalo de (0 a 50)

'''

import numpy as np

n_tentativas = 10

print('Adivinhe o número entre 1 a 50 !Você tem ',n_tentativas,' chances!')

# Gera um número aleatório inteiro entre 0 e 100:

num_oculto = np.random.randint(0,50)

while n_tentativas > 0:
    n_tentativas = n_tentativas - 1
    chute = int(input('Escolha um número: '))
    if chute > num_oculto:
        print('O número oculto é menor!')
        print('Nº RESTANTE DE TENTATIVAS = %d' % n_tentativas)
    elif chute < num_oculto:
        print('O número oculto é maior!')
        print('Nº  RESTANTE DE TENTATIVAS = %d' % n_tentativas)
    else:
        print('Parabéns! você acertou o nº que é : %d' % num_oculto)
        break

if n_tentativas ==0:
    print('---------------------')
    print('Infelizmente suas tentativas acabaram!')
    print('O nº oculto era : %d'% num_oculto)