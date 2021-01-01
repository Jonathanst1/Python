'''
-------- Funções--------
 Muitas etatapas de umm algoritmo podem ser aglommeradas/aglutinadas e representaadas por funções
 quando  uma mesma ação aparece repetidas vezes no decorrer do nosso algoritmo, uma
 maneira interessante de simplificar as estruturas dos códigos é a partir da criação de funções.

 E o que são funções para a linguagem Python?
 Funções são agrupamentos de instruções que são executadas a partir de um conjunto de informações de entradas
 gerando saídas processadas .

 Com as funções podemos executar diversar vezes um conjunto de instruções em códigos mais complexos
 sem a necessidade de reescrever essas instruções rotineiras.

 até o presente momento fizemos o uso de diversas funções úteis tais como : len() , range(),list(),int(),
 dentre outras

 vamos agora aprender a criar nossas próprias funções em python

 De modo geral , em Python, as funções são representadas da seguinte maneira:

 def nom_fun(arg1,arg2,argn):
 < corpo_Da_funcao>
 <retorno_da_funcao>

As funções são muito importantes pois podemos condensar códigos que frequetemente precisamos utilizar
em diversas etapas da solução dos nossos problemas.

Veja abaixo um esquema que mostra o princípio de funcionamento das funções :


Argumentos -------->         Função   ---->Resultado

Variáveis globais ----->     variáveis locais -----> Variáveis globais

Arquivos ou stream de dados ----->           ------->  Arquivos ou stream de dados


As funções também nos ajudam a tornar nosso código mais legível e intuitivo. Vamos aos exemplos práticos

Suponhamos que estamos interessados em criar uma calculadora e para isso precisamos desenvolver as funções
para as quatro operações básicas : soma,subtração, multiplicação e divisão.

# exemplo

def soma(a,b):
    return a+b


def subtrai(a,b):
    return a - b


def multiplica(a,b):
    return a*b


def divide (a,b):
    if b !=0:
        return a/b
    else:
        return'Erro divisão por zero!'


# Agoraa qque temos nossas funções criadas , ou sseja , elas esttão armazenadass na memória do computtador ,vamos utiliza-las:

x = 10
y= 20

print('Soma de x comm y :',soma(x,y))
print('Subtração de x com y:',subtrai(x,y))
print('Multiplicação de x com y',multiplica(x,y))
print('Divisão de x com y :',divide(x,y))


Podemos uttilizar ttannttos parãmetros de entrada quanntos forem nnecessários para o processamento de nossa função.

A função podde também não ter nenhumm parâmetro de entrada e retorno . Veja um exemplo abaixo:

def ola_mundo():
    print('Olá mundo!')

Notou a utilidade e flexibilidade das funções ? Pois bem a partir de agora passe sempre
que possivel a utilizar essa facilidade nos seus códigos.

--------------Variáveis locais e globais - funções

Quando começamos a trabalhar com funções , o conceito de variável local e glgobbal se torna útil .

# Exemplo


# variavel global

var_resp = 7

def soma_dois_numeros(a,b):
    #var_resp = variável local
    # serve apenas para o contexto da função
    var_resp = a + b
    return(var_resp)

print(soma_dois_numeros(3,20))

# Mostrar a var_resp
print(var_resp)

# Para fixar melhor o conceito , devemos perceber que a 'var_resp' dentro da função' soma_dois_numeros()
# é local e , portanto , é compreendida pela Python apenas dentro do escopo da função.No entanto
# a 'var_resp'fora da função tem a abrangência global e quando pedimos para imprimir com o 'print' o valor dela é retornado.


Bastante atenção agora. Não é uma boa práticaa de programação utilizar o mesmo nome para variáveis
locais e globais, pois podemos nos confundir na uttillização. Esse tipo de cuidado certamente evitará diversos
erros dde compilação, inclusive erros que muitas vezes são difíceis de serem encontrados.

Vamos a outro exemplo :

'''

#variável global
var_resp = 7

def soma_dois_numeros(a,b):
    #var_resp
    # serve apenas para o contexto da função
    var_resp_loc = a + b
    return(var_resp_loc)

# Mostraar a variável local : var_resp_loc

print(var_resp_loc)

# Ao tentarmos imprimir a variável local'var_resp_loc' obtivemos uma mensagem de variável não dedfinida,
# uma vez que estamos no escopo global pedindo que seja impressa uma variável local.