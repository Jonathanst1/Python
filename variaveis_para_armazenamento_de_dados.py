'''
Variáveis para armazenamento de dados

Listas
As listas sçao uma das mais importantes e utilizadas variáveis em Python
as variáveis do tipo listas são tidas como uma sequência generalizada,
por isso os elementos dentro de uma lista podem ser facilmente mutáveis.Em outras palavras,podemos modificar facilmente, de diversos modos,
os elementos dentro de uma lista.

Para representarmos listas utilizamos os colchetes[].
 exemplo :
 lista = [1,2,3,4]
print(lista)

lista_vazia = [] # criando uma lista vazia
lista_vazia2= list() # Tmbém criando uma lista vazia

print(type(lista_vazia))
print(type(lista_vazia2))

# Para criar listas utilizamos[]
lista_nomes1 = ['Ramon','Ricardo','Rafael','Renata']
lista_nomes2 = ['Ramon,Ricardo,Rafael, Renata']

print(type(lista_nomes1))
print(lista_nomes1)
print(lista_nomes2)

# A função len() diz o tamanho da lista
print(len(lista_nomes1))
print(len(lista_nomes2))

# Retorna o elemento index 0
print(lista_nomes1[0])
print(lista_nomes2[0])

#Podemos misturar os tipos de elementos presentes na lista
#veja um exemplo a seguir:

lista_mista = ['elevador',77,3.14]
print(lista_mista)

# Vejamos agora como fica o acesso a cada um dos elementos da 'lista_mista'
print('Tamanho da lista =', len(lista_mista))

# Deletando elemento da lista

del lista_mista[1]
print(lista_mista)

# Uma maneira prática de deletar elementos específicos de uma lista
# é a partir do método remove().

lista_mista2 = ['casa',77,3.14,'viagem',123,10,3,77]
lista_mista2.remove(3.14)
lista_mista2.remove(77)
lista_mista2.remove(77)
print(lista_mista2)

      Aninhamento de listas
Podemos fazer aninhamentos com as listas, ou seja, dentro de estruturas
de listas podemos criar listas.Vamos ao exemplo abaixo :

  EXEMPLO
# Exemplo
# Vamos criar uma lista de listas

lista =[[11,22,33],[1,2,3,4],[100,200,300,400,500]]
print(type(lista)) # tipo de lista
print(lista)
print(len(lista)) # Tamanho da lista

# Note que cada elemento da lista também é uma lista:
print(lista[0])

# Para acessarmos elementos de lista devemos fazer o slice(fatiamento) da seguinte maneira:

print(lista[2][2]) # da lista 3 pegue o elemento 3
print(lista[2][4]) # da lista 3 pegue o elemento 5

    Junção de listas e avaliações de elementos
Devemos aprender o máximo possível a respeito da manupulação de listas
pois elas são largamente utilizadas nas atividades de um cientista ou analista de dados, por exemplo.
Lembrando que essas áreas de trabalho estão bastante aquecidas e com escassez muito grande de profissionais.

Mais cedo ou mais tarde precisaremos conectar
listas nos nossos processos de análises . Veja como fazer isso com Python:

# exemplo

lista1= [ 1,2,3,4,5]
lista2 = [22,33,44,55,66,77]

sua_lista = lista1 + lista2

print(sua_lista)

# Os elementos de uma lista são iteráveis e podem
# ser facilmente manipulados a partir de fatiamentos , veja alguns exemplos
# abaixo :

minha_lista = ['tio','mãe','pai','irmão','sobrinha']

# fatiando os 4 primeiros elementos da lista
print(minha_lista[0:4])

# fatiando os elementos de 2 a 7 da lista
print(minha_lista[1:3])

# ultimo elemento da lista
print(minha_lista[-1])

# Elementos de trás para frente da lista

print(minha_lista[::-1])


    OPERADOR IN

sum_lista =[1,2,3,4,5,22,33,44,55,66,77]
print(20 in sum_lista) # Avalia se o 20 esta na sum_lista

print(77 in sum_lista) # avalia se 77 está na sum_lista

sum_lista.append(121) # Adiciona o elemento 121 no fim da lista
print(sum_lista)

print(sum_lista.count(33)) # Conta quantas vezes o elemento 33 aparece

print(sum_lista.index(121)) # para saber o indice do elemento 121

sum_lista.insert(6,101)# adiciona o elemento 101 na posição 7
print(sum_lista.insert(6,101))
'''
sum_lista =[1,2,3,4,5,22,33,44,55,121,66,77]

sum_lista.sort() # ordena os elementos da lista
print(sum_lista)

sum_lista.reverse()
print(sum_lista)