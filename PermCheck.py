'''
Uma matriz não vazia A que consiste em N números inteiros é fornecida.

Uma permutação é uma sequência que contém cada elemento de 1 a N uma vez e apenas uma vez.

Por exemplo, matriz A de modo que:

    A [0] = 4
    A [1] = 1
    A [2] = 3
    A [3] = 2
é uma permutação, mas a matriz A é tal que:

    A [0] = 4
    A [1] = 1
    A [2] = 3
não é uma permutação, porque o valor 2 está ausente.

O objetivo é verificar se a matriz A é uma permutação.

Escreva uma função:

solução def (A)

que, dada uma matriz A, retorna 1 se a matriz A for uma permutação e 0 se não for.

Por exemplo, dada a matriz A de modo que:

    A [0] = 4
    A [1] = 1
    A [2] = 3
    A [3] = 2
a função deve retornar 1.

Dada matriz A, de modo que:

    A [0] = 4
    A [1] = 1
    A [2] = 3
a função deve retornar 0.

Escreva um algoritmo eficiente para as seguintes suposições:

N é um número inteiro dentro do intervalo [1..100.000];
cada elemento da matriz A é um número inteiro dentro do intervalo [1..1.000.000.000].
'''

def solution1(A): #41 % Score
    if len(A) < max(A):
        return 0
    return 1


def solution2(A): #100 % Score
    set_a = set(A)
    set_b = set(range(1, len(A) + 1))
    if set_a == set_b:
        return 1
    else:
        return 0
