"""
Indexação em Python

# Exemplos

varstr = 'Estudo'
print(varstr[0])
print(varstr[1])
print(varstr[2])
print(varstr[3])
print(varstr[4])
print(varstr[5])


# podemos utilizar o método find() dos objetos strings
# para encontrar o indice da posição em que se encontra
# um determinado caractere ou conjunto de caracteres

   # exemplo
varstr = 'Estudo'

print(varstr.find('t'))

Muitas vezes precisamos pegar conjuntos de caracteres a partir de uma determinada posição (indexação).
 Para isso podemos utilizar os dois pontos ‘:’ para fazer slices (fatiamentos).

F. V. C. Santos, Rafael. Python: Guia prático
 do básico ao avançado (Cientista de dados Livro 2) (p. 73). rafaelfvcs. Edição do Kindle.
  """

  # exemplo
#frase = 'Python é uma linguagem muito poderosa!'
#print(frase[2:])

#frase = 'Python é uma linguagem muito poderosa!'
#print(frase[::3]) # retorna a string pulando 3 ccaracteress.

frase = 'Python é uma linguagem muito poderosa!'
print(frase[::-1]) # rettorna a string pulando 1 caraactere