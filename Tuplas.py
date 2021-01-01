'''
Tuplas
As tuplas são estruturas bastante semelhantes ás listas. A princpal
diferença entre tuplas e listas é que tuplas são
estrutura que armazenam dados e são mutáveis . Por outro lado como sabemos,ás listas
são estruturas mutáveis

Principais caracteristicas das tuplas :

- Seu tamanho não pode ser alterado
diferentemente dos dicionários e listas;

-Seus elementos são mutáveis , iteráveis e ordenados;

-Não pode conter múltiplos tipos de dados.

A estrutura geral de uma tupla é basicamente a mesma de uma lista
onde seus valores são separados por vírgulas, porém entre parênteses ;

tupla = ('val1','val2','valn'

PODEMOS NOTAR QUE UMA TUPLA É CARACTERIZADA PELO USO DE PARÊNTESES ()
LEMBRANDO QUE EM LISTAS UTILIZAMOS COLCHETES E EM DICIONÁRIO USAMOS CHAVES {}

'''
# Exemplo

# Definição de uma tupla sem parênteses

tupla1 = 'a','b','c','d','e'
print(tupla1)

tupla2 = ('a','b','c','d','e')
print(tupla2)

print(type(tupla1))
print(type(tupla2))

# Definir uma tupla

tu1 = (1,2,3,4,5)

# transformar uma tupla em lista

list1 = [1,2,3]

list = list(tu1)

# Adicionar um valor a lista

list1.append(6)

print(tu1)
print(list1)