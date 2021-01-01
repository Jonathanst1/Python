'''
idade = int(input("Digite a sua idade : "))
nome = (input("Digite seu nome : "))

if idade < 13:
    print("Você é uma criança")

else:
    if idade > 13 and  idade <=18:
        print("Você é um adolescente/jovem")
    else:
        if  idade > 19 and  idade <=40:
            print('Você é um adulto jovem')

        else:
            if idade > 40:
                print("Você está chegando na Terceira idade ! Parabéns")



'''
valores = [ 55,56,59,90,110]

for v in valores:
    if v%3 == 0:
        print(v)



