'''
Vetores e matrizes

Podemos representar conjuntos de dados com vetores .
Devemos imaginar que os vetores são úteis para armazenar coleções de valores de um único tipo.

Listas , dicionários e tuplas , como já estudado , Podem armazenar valores de diversos tipos. No entanto,
os vetores e matrizes , em termos matemáticos , precisam conter
elementos de um único tipo , que no nosso caso será o tipo numérico.

VETORES

Precisamos de uma biblioteca Python chamate NumPy para trabalharmos com arrays (vetores de um modo geral)
e matrizes multidimensionais. Assim , prescisamos carregar previamente essa biblioteca com o comando import

import numpy as np
# Criar um vetor

vet1 = np.array([1,2,3,4])
print(vet1)

print(type(vet1))

Perceba que o tipo da variável vet1 é um ' numpy.ndarray' que representa um vetor de maneira geral

Os elementos do vetor são todos apenas do tipo numérico (int,float ou double)
Veja o que acontece se tentarmos misturar os tipos dos elementos :


import numpy as np
# Criar um vetor

vet1 = np.array([1,2,3,4])
print(vet1)

print(type(vet1))

vet2 = np.array([1,2,3,'4']) # Tentando adicionar str '4'

print(vet2[1])

print(type(vet2[1]))

O que aconteceu no exemplo acima é algo bastante interessante. Podemos notar que iniciamos
adicionando valores numéricos ao nosso vet2 (1,2,3), porém o último elemento do vetor é uma string('4').

Sabemos que vetores e matrizes só podem conter um tipo específico de elemento e por isso o interpretador Python
decidiu transformar todos os elementos do vetor em uma string para manter a consistência de um vetor

A pergunta que não quer calar é : por que o Python não transformou a string'4' em um número ?

Veja o exemplo abaixo que vai esclarecer esse questionamento :

import numpy as np
# Criar um vetor

vet1 = np.array([1,2,3,4])
print(vet1)

print(type(vet1))

vet2 = np.array([1,2,3,'4']) # Tentando adicionar str '4'

print(vet2[1])

print(type(vet2[1]))

vet3 = np.array([7,8,9,'a'])
print(vet3)
print(type(vet3[0]))

------------------------------

             Matrizes

Quando estamos interessados em representar coleções de vetores , as matrizes
são uma meneira inteligente e simplificada que nos auxiliam nessa atividade.

Os elementos das matrizes podem ser números reais , números complexos , expressões algébricas e até mesmo funções.

Matrizes são compostas por linhas e colunas .
Assim como acontece para os vetores , as matrizes precisam possuir elementos de mesmo tipo . Veja o exemplo abaixo:


# Exemplo

import numpy as np

# Define uma matriz com 2 linhas e 3 colunas

a = np.array([[1,2,3],[3,4,5]])

# Define uma matriz com 3 linhas e 3 colunas

a2 = np.matrix([[1,2,3],[3,4,5]])

print(type(a))
print(type(a2))

# Note que podemos definir uma matriz de duas maneiras. De ambas as maneiras podemos
#executar as operações matriciais. Veja abaixo como obter elementos e fatias a partir das matrizes:

# acessar o elemento da linha 3

print(a[1,2])

# Obter todos os elementos da linha 1

print(a[: ,1])

# O mesmo comportamento de que precisamos manter o mesmo tipo de elementos de um vetor acontece com
# as matrizes :

import numpy as np

b = np.array([[1,2,3],[3,4,'5']])
print(b)

print(type(b[0][0]))

    Operações básicas com Vetores e Matrizes

Fazer operações com vetores e matrizes com o Python a partir da biblioteca NUMPY é bastante
simples e intuitivo .
import numpy as np

# Define o vetor

v = np.array([11,22,33])

# Define a matriz

a = np.array([[1,2,3],[4,5,6]])

# Define a matriz

b = np.array([[1,2,3],[2,3,3]])

# Soma o vetor com a matriz

sva = v + a

print(sva)

# Algumas operações são feitas elemento a elemento . O Python se responsabiliza
# de fazer a concordância operacional entre os elementos dos vetores e matrizes.

# Multiplica o vetor 'v' pela matriz 'a '

va = v*a
print(va)

# Soma dos elementos das matrizes

c = a + b
print(c)

# Operações com matrizes

d = 2* a + b
print(d)

# Devemos ter cuidado nas operações de multiplicação porque temos dois tipos de produtos entre matrizes
# Produto entre os escalares da matriz e o produto matricial. Veja no exemplo abaixo essa diferença.

map = a * b
print(map)

# Multiplicação Matricial

dab = np.dot(a,b) # teremos mensagem de erro !
'''

import numpy as np

print(dir(np))
print(help(np.dot))
