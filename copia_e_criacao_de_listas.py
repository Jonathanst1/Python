'''
  CÓPIA E CRIAÇÃO DE LISTAS
A sintaxe do python apresenta uma estrutura muito inteligente e peculiar
vamos estudar nesta parte um exemplo que mostra uma peculiaridade interessante
e muito importante de ser conhecida.

Algumas vezes precisamos fazer cópias de variáveis do tipo lista
Para isso precisamos ter cuidado, pois ao invés de uma cópia
poderemos estar fazendo apenas uma referenciação, um apontamento , mas não uma cópia

vejamos com cuidado o exemplo abaixo :

#faz referenciação de numeros para novos
numeros = [11,22,33,44,55]
novos = numeros
novos.append(1)
novos.append(77)
print(numeros)
'''

# exemplo

#lista de números
numeros = [11,22,33,44,55]



# Podemos notar , no exemplo acima , que não criamos uma nova variável(novos)
#como os elementos de (numeros).Para fazermos isso, vejamos abaixo
# como prosseguir:

# Cria nova variável com elementos de 'numeros'
numeros2 = numeros[:]
numeros2.append(57)
print(numeros)
print(numeros2)

# Veja outras duas maneiras de fazer cópias de listas :
numeros3 = numeros.copy() # faz a copia do elemento de numeros para numeros 3

numeros4 = list(numeros) # faz cópia dos elementos de numeros para numeros 3
print(numeros3)
print(numeros4)