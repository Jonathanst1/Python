"""
VARIAVEIS E TIPOS

As variáveis são espaços em memória utilizados paara a armazennar
determinados valores de um tipo específico.Toda variável deve possuir um nome
 e um valor com a atribuição de um determinado tipo.

 Palavras que não devemos usar  como variáveis .
 False      True         as
 class      def         elif
 finally    from        if
 is         nonlocal    Or
 return     while      yield
 None      and        Assert
 continue   del       Else
 for        global   import
 lambda     not     Pass
 try       with      break
 :except    in      raise

 #exemplo variável

a = 77 # variavel 'a' com valor atribuido 77
print(77) # imprime o valor 77

print(a) # imprime o valor da variável ' a '

VARIAVEL INTEIRA

Vamos criar algumas variáveis com o tipo inteiro .
O python possui uma tipagem dinâmca, isto é
não precisamos especificar os tipos de variáveis como nas linguagens Java,C++,C#
por exemplo.
Assim para declararmos variáveis do tipo inteiro , basta fazermos:

#Exemplo variaveis inteiras

var_a = 7

print(var_a)

#Constantemente,iremos utilizar a função
#type() para checar o tipo das nossas variáveis.
#VEJAMOS ABAIXO UM EXEMPLO

#>>> var_c = 20
#>>> type(var_c)
<class 'int'>
#>>> print(var_c)
20

A variável do tipo float aloca um espaço de 4 bytes de memória enquanto a
do tipo double 8 bytes

Como a tipagem em Python é dinâmica, automaticamente é identificado que estamos
utilizando uma variável float ou double quando utilizamos
ponto decimal.Veja exemplo abaixo :


#Exemplo
var_d = 3.14
 type(var_d)
<class 'float'>
var_e = 11.
 type(var_e)
<class 'float'>

    VARIAVEL STRING
Quando estamos precisando armazenar caracters alfanuméricos(letras)
oalavras ou frases podemos utilizar a variável do tipo string.
devemos utilizar as aspas simples(apóstofro) ou duplas.Veja abaixo como devemos proceder

#Exemplos
str_var_1 = 'A'
print(type(str_var_1))
print(str_var_1)

str_var_2 = 'Python'
print(type(str_var_2))
print(str_var_2)

str_var_3 = "Python uma excelente lingua!"
print(type(str_var_3))
print(str_var_3)

Podemos concatenar as variáveis do tipo string da seguinte manera:
Exemplo:

nome1 = "Maria"
nome2 = " luiza"

total = nome1 + nome2

print(type(total))
print(total)

Variável booleana****

Variáveis que podemos admitir os valores verdadeiro e falso ou seja
True  ou False são chamadas do tipo booleana.Em Python a declaração
desse tipo de variável é feita da seguinte maneira:


# Exemplos

a = True # OBS : True tem que iniciar com a letra maiuscula
print(type(a))
b = False #OBS : False deve iniciar com a letra maiúscula
print(type(b))

      DECLARAÇÕES MULTIPLAS
Algo muito p´ratico é que no Python podemos declarar diversas variáveis de uma vez
No entanto , devemos ter bastante cuidado para não confundirmos valores nas declarações
veja os exemplos abaixo:


 # Exemplos

disciplina1, disciplina2,disciplina3 = "Quimica","Estatistica","Matematica"
#print(disciplina1,disciplina2,disciplina3)
print(disciplina1)
print(disciplina2)
print((disciplina3))


Podemos também misturar os tipos de variáveis

# Exemplos
identidade = idade, nome, vivo = 30 , "renata",True
print(identidade)
    OPERAÇÕES COM VARIÁVEIS

"""
# EXEMPLOS

var1 = 10
var2 = 3
total = var1 + var2
print(total)

total1 = var1 * var2
print(total1)