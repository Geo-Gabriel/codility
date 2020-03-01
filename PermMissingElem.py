'''
É fornecida uma matriz A que consiste em N números inteiros diferentes. A matriz contém números inteiros
no intervalo [1 .. (N + 1)], o que significa que exatamente um elemento está ausente.

Seu objetivo é encontrar esse elemento que está faltando.

Escreva uma função:

solução def (A)

que, dada uma matriz A, retorna o valor do elemento ausente.

Por exemplo, dada a matriz A de modo que:

  A [0] = 2
  A [1] = 3
  A [2] = 1
  A [3] = 5
a função deve retornar 4, pois é o elemento que falta.

Escreva um algoritmo eficiente para as seguintes suposições:

N é um número inteiro dentro do intervalo [0..100.000];
os elementos de A são todos distintos;
cada elemento da matriz A é um número inteiro dentro do intervalo [1 .. (N + 1)].
'''

# def solution(A):
#     for number in A[:-1]:
#         if (number + 1) not in A:
#             return number + 1


'''Method: Sum formula'''

def solution(a):
    if a:
        for numero in a:
            pass


def dominant(n):
    result = 0
    for i in range(n):
        result += 1
    return result

def linear(n , a):
    for i in range(n):
        if a[i] == 0:
            return 0
    return 1

def quadratic(n):
    result = 0
    for i in range(n):
        for j in range(i, n):
            result += 1
        return result

print(quadratic(1))

test = [0,1,2,3,4]




# for numero in lista[:-1]:
#     if (numero + 1) not in lista:
#         print(numero + 1)

