'''
Laços de Repetição for e while

Atividades repetitiva são muito frequentes nos algoritimos
por isso as estruturas de repetição representam a base de vários programas.
Utilizamos essas estruturas quando precisamos que alguma atividade seja executada
um número específico de vezes (FOR) ou até que uma condnição lógica seja atingida
(while_

Por exemplo, vamos supor que precisamos imprimir na tela os
números de UM a DEZ . poderiamos fazer o seguinte:

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# Isso não pareceu ser algo prático de ser feito , né verdade?
# Podemos fazer isso de maneira mais inteligente com o laço de repetição FOR.

    loop for
Uma maneira muito mais p´ratica de fazer a mesma coisa é a partir do uso do 'for'
A forma geral do uso do loop for é a seguinte :

for item in conjunto de itens :
    execute comandos

Lembre - se sempre da indentação . Para ajudar fique esperto(A) que
toda vez que utilizammos os dois pontos ':' depois de alguma diretiva os códigos que virão
na linha seguinte deverão possuir indentação

Veja o exemplo abaixo e perceba que programar é basicamente conversar com o
computtaador :

for i in range(10):
    print(i +1)

O laço 'for' em Python é algo que empodera em muitto a vida de um programador . Utilizando'for'
a linguagem python permite iterações dentro de listas de uma maneira bastante intuitiva e
simplles


Perceba que utilizamos o range (10) para gerar um intervalo de valores
de 0 a 9 (lembrando que a indexação  sempre começa com zero)
Por isso foi necessário somar uma unidade no pront( i+1)
Poderiamoms tter utilizado o range (1,11) e enncontrar o mesmo resultado:

for i in range (1,11):
    print(i)

Muitas vezes precisamos de um range de valores
dentro de um determinado intervalo com incremento especificado. Veja abaixo um exemplo
de vaalores entre 0 a 20 com incrementto de 3 unidades


for i in range(0,20,3): # zero a 20 com incremento de 3
    print(i)

Poddemos fazer com que Python faça um passeio por dentro dos valores de uma lista/dicionários/tuplas
quaisquqer. Veja como funciona :


lista = [10,77,88,32,100]

for i in lista:
    print(i)

Também podemos colocar esttruturaas condicionais dentro dos nossos loops.
vamos fazer um exemplo no qual apenas os números paress de uma listta de valores irão ser impressos na tela :

valores = [11,55,22,16,10,7,9,68]

for v in valores:
    if v%2 ==0: # se resto da divisão por 2 fofr nula
        print(v)

O interessante é que podemos executar diversas operações matemáticas
ecom cada um dos elementos das listas:

lista = [10,77,88,32,100]

for i in lista:
    # fafzer alguma operação matemáticaa com os elementos
    # da lista:
    resp = ( i+2)/10
    print(resp)

Veja abaixo um exemplo de loop ' for' aplicacdo a dicionários:

# dicionário :
dic = {'var1':10,'var2':20,'var3':30,'var4':40}

for i in dic:
    print(i)

# Notet que o iteraando 'i' para uma estrutura de dicionário retorna apenas a chaave.
# Por vezes , podedmos precisar das chaves e dos valores dentro de uma estrutura de dicionário.
# Veja abaixo como fazer isso :

for c, v in dic.items():
    print(c,v) # mostra c- chave - v = valor

Agora um exeplo utilizando tuplas:

# tupla

tupla = (11,22,33,44,55)

for i in tupla:
    print(i)

Vamos estudar loops aninhados , ou seja , loop dentro de outro loop
Esse tipo de estrutura de repetição é muito utilizado quando estamos trabalhando com
vetores e matrizes , por exemplo.

lista = [[1,2,3],[4,5,6,7,7,8],[11,12,13,14,15,16,17,18]]

for i in lista:
    print(i)

# Podemos observar que o valor do iterando 'i' agora é uma lista e não mais um valorr apenas
#Assim podemos fazer outro loop dentro de cada um desses elementos da lista'i'

for i in lista :
    for j in i:
        print(j)
    print('------------------')

# Estamos fazendo uma nova itteração 'j' onde cada valor deste iterando está contido dentro de cada uma das listas 'i'
#Vale ressaltar que podemos chamar as variáveis iteradoras dentro dos loops 'for' da maneira
# melhor que nos agrade. Vejamos o exemplo abaixo com o mesmo resultado :
for li in lista:
    for var in li:
        print(var)
    print('------------')



         Loop while

Quando for necessária uma condição de repetição baseada em algum critério lógico, a melhor estratégia
para isso pode ser atraves do uso do loop 'while'

Vejamos abaixo a estrutura geral de funcionamento desse loop

while condicao-logica:
    <bloco de instruçções>

Nesse tipo de estrutura temos que ter bastante cuidado para não gerarmos um
loop infinito
nosso código precisa estar esttruturado para terminaar a execução doloop uma vez que determinada condição lógica for
atingida

Contudo , a instrução while será executatda de modo repetittivo, uma única vez ou inúmeras vezes
até que uma condição lógica estetja verdadeira.

Veja como imprimir valores de 1 a 10 como fizemos com o loop ' for ':

cont = 1

while cont <=10:
    print(cont)
    cont = cont + 1 # temos que add essa linha paraa
                    # não termos um loop infinito

Vamos estudar agora algo muito útil. Dentro dos nossos comandos loops ' for ' ou ' while' ´pde,ps ,idar
seiu comportamento a partir das diretivas: pass,break ou continue.

pass : não executta nada na esttrutura , dando continuidade ao laço de repetição

break : ttermimna com o laço de repettição

continue : pula uma iteração passando para a próxima seguinte .


A diferença enntre o pass e o conttinue é bastante sutil , todavia importante .
Fique atento(a) no exemplo a seguir para compreender melhor essa diferença;

for letra in ' programador':
    if letra == 'a':
        pass
    print(letra)

# Note que quando if é executado , ou seja,, quando encontramos a primeira letra igual a 'a'
# o pass faz com que prossigamos com o loop sem entrarmos mais na estruttura if no príxumo iterando .

# Por outro lado, se utilizarmos no lugar do pass a diretiva 'continue' sempre iremos avaliar a estrutura ' if '
# e toda vez que a letra for encontrada iremos passa para a iteração seguinte antes de imprimir a letra na tela.

for letra in ' programador':
    if letra == 'a':
        continue
    print(letra)


# Caso coloquemos um break no lugar do continue teremos uma interrupção no lop quando o if for verdadeiro, ou seja , letra == 'a'.

for letra in "programador":
    if letra =='a':
        break
    print(letra)


'''

