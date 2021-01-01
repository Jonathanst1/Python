'''
t1 = ('João 25','Maria 35',' Pedro 40')

print(t1)
print(type(t1))


l1 = ['Carne ',' peixe',' aveia',' prestigio',' flores','carro','']
l1.append('Ovos')
print(l1)

l1.count('Carne')
print(l1)

l1.reverse()
print(l1)

D1 = {'Patricia':24 ,'Victor':24,'Carlos':25}
print(D1)
print(type(D1))


print(D1.keys()) # Conhecendo as chaves presentes em um dicionário

print(D1.values()) # Tendo acesso aos valores

D2 = {'Paty' : 32,'Lima':33}
D1.update(D2)

print(D1)

'''
# -------------------------Vetores e Matizes -------------


import numpy as np

vt1 = np.array([1,0,5],[-2,-5,7])

v2 = np.array([1,0,5])

sva = vt1 + v2
print(sva)
