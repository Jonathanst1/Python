'''
Condicionais, Laços de repetição e listas

Antes de prosseguirmos com este capítulo, vamos a um breve resumo do que já foi estudado
até o presente momento :

- Estruturas básicas do python;
- Ostipos de variáveis ;
- Os principais operadores lógicos e matemáticos;
- Estruturas de dados: listas, dicionários,tuplas e v etores e matrizes.


É isso aí programador . já estamos ficando ex-perts na linguagem python

iremos agora conectar tudo o que foi aprendido dentro de estruturas lógicas
mais elaboras.

O principal poder fornecido por uma linguagem de programação será representado
nesse capitulo .

Nós como programadores precisamos rotneiramente trabalhar com estruturas de condições
lógicas para modificar a direção de andamento de um programa.

Também é frequente a necessidade de efetuar operações repetitvas e para isso temos os laços de repetição

Contudo , vamos começar estudando as condifionais IF/ELSE / ELIF


Condicional if

Muitas vezes precisamos determinar um conjunto de ações para que as máquinas solucionem
algum problema. Nisso, a estrutura 'if' (SE) nos ajuda de forma simples e r[apida

Essa diretiva faz a seguinte ordem : se (if) determinada condição logica for verdadeira, execute uma ação.

Temos a seguinte estrutura de declaração if no Python :

if (condição a ser avaliada):

   Bloco (indentado) de execução de comandos(executar algo)

# Exemplo

# Entrada de valores

A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))

if(A > B):
    print('A é maior que B!:')

if(A < B):
    print('B é maior que A !')


Condicional else
Podemos melhorar nosso código do ultimo exemplo acima, deixando - o mais
legivel e menos verboso a partir do uso de 'else'(que pode ser traduzido como
:caso contrario) ou seja,'if' (se determinada condição for aceita execute a estrutura)
'else'(caso contrário ) execute esta outra estrutura de comandos .
# Exemplo

# Entrada de valores

A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))

if(A > B):
    print('A é maior que B!:')

else:
    print('B é maior que A !')
# Podemos fazer aninamentos (estruturas dentro de outras estruturas com IF E ELSE .

idade = 80
sexo = 'F'



if idade < 9:
    print('É uma criança')
    if sexo =='M':
        print('Sexo Masculino')
    else:
        print('Sexo Feminino')

else:
    print('Não é uma criança!')
    if sexo =='M':
        print('Sexo Masculino')

    else:
        print('Sexo Feminino')


# Veja no outro caso

idade = 7
sexo = 'M'

if idade < 9:
    print('É uma criança')
    if sexo =='M':
        print('Sexo masculino')
    else:
        print('Sexo feminino')

else:
    print('Não é uma criança!')
    if sexo =='M':
        print('Sexo masculino' )
    else:
        print('Sexo feminino ')

# Vamos a outro exemplo, preste muita atenção neste:

nota = int(input("Digite a nota: "))
if nota <= 1 and nota > 0:
    print('Nota muito baixa !')

else:
    if nota > 1 and nota <=4:
        print('Nota baixa.')
    else:
        if nota > 4 and nota <=7:
            print('Nota média! ')

        else:
            if nota > 7 and nota <=10:
                print('Nota alta')
            else:
                print('Nota Inválida')

Condicional elif

Se precisarmos fazer múltiplas avaliações de blocos lógicos
sem ter que ficar criaando outros níveis de if e else podemos utilizar a elif.

Vejamos como funciona esse elemento condicional a parttir de modificações do
últtimo exemplo apresentado :

exemplo:

#Exemplo

nota = 8

if nota <= 1 and nota >0:
    print('Nnota muito baixaa!')
elif nota > 4 and nota <= 7:
    print('Nota média')
elif nota > 7 and nota <=10:
    print('Nota alta')

else :
    print('Nota inválida')

Desse modo, com o uso do elif nosso código ficou muito mais enxuto e legível.

Temos um ganho significativo com a estrutura de indentação
onde não precisamos fazer aninhamento que possam atrapalhar no entendimento
do código.
'''







