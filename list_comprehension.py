'''
List Comprehension

As List comprehension são amplamente utilizadas em scripts para gilizar a execução de varios tipos de
operações.

Atividades de busca e varredura entre elementos de listas são muiti
frequentes. A linguagem Python nos disponibiliza uma maneira condensada e inteligente
de fazer isso.
De modo simplificado , com list comprehension podemos desenvolver listas usando
uma notação condensada que dispensa a utilização de loops for
externos. A utilização desses tipos de listas nos traz vantagens como melhores desempenhos
de tempo computacional .
A maneira de fazer declarações com a list comprehension lembra muito como fazermos descrições de conjuntos numéricos em notação
matemática. Veja um exemplo geral.

lc = [x for x in 'sequência']
O exemplo abaixo mostra como podemos pegar uma lista com 100 valores de 0 a 99 e elevar
cada elemento ao quadrado. Veja como fazer isso com apenas uma linha de código .
# exemplo
list_num = [x**2 for x in range(100)]

print(list_num)

list_par = [x for x in list_num if x % 2 == 0] # Obter lista somente com elementos de valores par da 'list_num"
print(list_par)

'''

# Podemos utilizar a list comprehension em strings veja abaixo :
# de uma sequencia de caracteres retornar cada caracter

letras = [ letra for letra in 'Python']
print(letras)
