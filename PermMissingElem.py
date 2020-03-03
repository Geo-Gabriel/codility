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


def solution(A):
    elemento_perdido = len(A) + 1
    for i, j in enumerate(A):
        elemento_perdido = elemento_perdido ^ j ^ (i + 1)
    return elemento_perdido


# sum of first N natural numbers = (N * (N + 1))/2.
# Detected time complexity: --> O(N) or O(N * log(N))


def solution(A):
    N = len(A)
    formula = ((N + 1) * ((N + 1) + 1)) // 2
    soma = sum(A)
    return formula - soma


lista1 = [x for x in range(1,21)]
print(lista1)
lista1.pop(11)
print(lista1)


N = len(lista1)
formula = ((N + 1) * ((N + 1) + 1)) // 2
print(formula)
soma = sum(lista1)
print(soma)
print(formula - soma)


# for numero in lista[:-1]:
#     if (numero + 1) not in lista:
#         print(numero + 1)
