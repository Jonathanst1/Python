'''
---------Dicionários------
Uma maneira muito prática de organizar os dados e informações no Python é a partir de
dicionários

Podemos entender dicionário como uma tabela de dados do tipo chave e valor .
como vimos anteriormente, as listas são definidas a partir de colchetes []
já os elementos dos dicionários  são representados dentro de chaves {}

veja abaixo como é a estrutura do dicionário em PYTHON:

dict = {chave1 :valor1 , chave2:valor2,...,chaveN:valorN}

Os dicionários são otimos para fazer armazenamento de dados,quando mapeamento de
dados for um requisito técnico importante de ser considerado
Trabalhar com listas , como já foiestudado, não nos permite fazer associação de pares de valores
do tipo chave e valor como é o caso dos dicionários.

Portanto , com os dicionários , temos um mapeamento que relaciona uma coleção de objetos
que são armazenados por uma chave , ao invés de uma sequeência de objetos armazenados por sua posição
como é o caso das listas.

Veja abaixo a diferença entre uma lista e um dicionário :
# Exemplo:

# Exemplo de lista
salario_list = ['Pedro',1000,'Carlos',750,'Ricardo',2000,'Leticia',2500]
print(salario_list)
print(type(salario_list))

# Exemplo de dicionário

salario_dict = {'Pedro':1000,'Carlos':750,'Ricardo':2000,'Leticia':2500}
print(salario_dict)
print(type(salario_dict))

#Podemos notar que a diferença  visual é pequena .
# No entanto, estruturalmente temos diferenças significativas.

Nos dicionários podemos utilizar as chaves como índices para encontrarmos os valores
correspondentes. Veja como podemos fazer isso :


salario_dict = {'Pedro':1000,'Carlos':750,'Ricardo':2000,'Leticia':2500}
print(salario_dict['Pedro'])


print(salario_dict['Leticia'])

# Podemos adicionar valores aos dicionários da seguinte maneira :
len(salario_dict)
salario_dict['Rafael'] = 1200
print(salario_dict)

print(len(salario_dict))
Vamos agora conhecer os processamentos que podemos fazer com os dados
de um dicionário.


 ------------------ Principais métodos dos dicionários---------

 Assim como os objetos , listas possuem um conjunto de métodos específicos para manipulação
 de elementos . Os dicionários também possuem os seus próprios métodos.

 como de costume , podemos visualizar todos os métodos a partir do ponto mais a tecla tab.


salario_dict = {'Pedro':1000,'Carlos':750,'Ricardo':2000,'Leticia':2500}
salario_dict.keys()
print(salario_dict.keys())

# Podemos também ter acesso aos valores das chaves a partir do método. values():

salario_dict.values()
print(salario_dict.values())

# Caso tenhamos dois dicionários e o interesse for juntá-los
# temos o método .update(). Veja abaixo como funciona :

# Dicionário 1 contendo os nomes e respectivos pesos (kg)

pesos1 = {'paulo':57,'Priscila':65}

# Dicionários 2 contendo os nomes e respectivos pesos (kg)
pesos2 = {'Débora':68,'Jefferson':70}

# Agrupa dicionário pesos 2 em pesos1

pesos1.update(pesos2)

print(pesos1)

# Podemos deletar chaves e valores de um dicionário a partir da diretiva del :
del pesos1['paulo']
print(pesos1)

# Se o interesse for deletar todo o conteúdo do dicionário podemos
#utilizar o método .clear()

pesos1.clear()
print(pesos1
      )

# No entanto , se quisermos apagar/remover todo o tipo de dicionário com seu conteúdo , claro, podemos
# utilizar o del:

del pesos2 # deleta o dicionário pesos2 - não apenas o conteúdo
# como é feito com o método.clear()

print(pesos2)

Vale lembrar que os dicionários em sua estrutura aceitam diferentes tipos de dados. Em outras
palavras , podemos misturar os tipos de dados das chaves e valores . Veja abaixo um exemplo:


# Dicionário misto

dicionario = {'Maria':53, 77: 'João', 'nome':'Silva'}

print(dicionario)

# Acessando o valor a partir da chave Maria
print(dicionario['Maria'])

# Acessando o valor a partir da chave 77
print(dicionario[77])

print(dicionario['nome'])

Podemos criar dicionarios a partir de outras estruturas , por exemplo
dicionários de listas.

'''

dic1 = {'chave1':231, 'chave2':[3,4,5,3], 'chave3':['seg','ter','qua','qui','sex','sab','dom']}
print(dic1)


# dicionários dentro de outro dicionários
# dicionários aninhados

dic2 = {'c1':1,'c2':77,'c3':{'d1':10,'d2':5,'d3':17}}
print(dic2)


