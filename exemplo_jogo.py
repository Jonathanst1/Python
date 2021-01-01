import numpy as np

n_tentativas = 10

print('Adivinhe a idade do João ! Você tem ',n_tentativas,' chances')

idade_joao = np.random.randint(0,100)

while n_tentativas >0:
    n_tentativas = n_tentativas -1
    chute = int(input('Escolha um número: '))
    if chute > idade_joao:
        print('João tem menos idade!')
        print('Você tem apenas %d tentativas'% n_tentativas,'tentativas!')
    elif chute < idade_joao:
        print('João tem mais idade!')
        print('Você tem apenas %d tentativas'% n_tentativas,'restantes !')
    else:
        print('Parabéns você acertou aa idade do joão que é : %d'% idade_joao,'anos !')
        break
if n_tentativas==0:
    print('----------------')
    print('Infelizmente suas tentativas acabaram! ')
    print('A idade do joão era : %d' %idade_joao,'anos!')