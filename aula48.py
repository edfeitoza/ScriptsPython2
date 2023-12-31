'''
Listas em Python
Tipo list - mutável

Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +

CRUD
Create, Read, Update e Delete => lista[i]

###########################################
#            01234
#           -54321
string =    'ABCDE'

#         0     1      2       3   4      -> indice da lista
#        -5    -4     -3      -2  -1      -> indice da lista negativo
lista = [123, True, 'Python', 1.4, []]
print(lista)
print(lista[3])
lista[2] = 'Pythonicos'
print(lista)

###############################################
lista = [10, 20, 30, 40]
print(lista)
lista.append(50)
lista.append(60)
lista.append(70)
print(lista)
ultimo_Valor = lista.pop(3)
print(lista, 'Removido: ', ultimo_Valor)
###############################################

lista = [10, 20, 30, 40]
print(lista)
lista.insert(0, 1)
print(lista)
###############################################

lista_a = [1,2,3]
lista_b = [4,5,6]

lista_c = lista_a + lista_b
print(lista_c)

lista_a.extend(lista_b)
print(lista_a)
###############################################

Cuidados com os dados mutáveis

= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutávesl)

'''
lista_a = ['Python', 'PHP', 'C']
lista_b = lista_a.copy()
print(lista_b)
lista_b = lista_a
lista_a[2] = 'Delphi'
print(lista_b)
