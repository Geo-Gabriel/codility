'''
Esta é uma tarefa de demonstração.

Escreva uma função:

solução def (A)

que, dada uma matriz A de N números inteiros, retorna o menor número inteiro positivo (maior que 0) que
não ocorre em A.

Por exemplo, dado A = [1, 3, 6, 4, 1, 2], a função deve retornar 5.

Dado A = [1, 2, 3], a função deve retornar 4.

Dado A = [−1, −3], a função deve retornar 1.

Escreva um algoritmo eficiente para as seguintes suposições:

N é um número inteiro dentro do intervalo [1..100.000];
cada elemento da matriz A é um número inteiro dentro do intervalo [-1.000.000..1.000.000].
'''

def solution(A):
    if not A or 1 not in A:
        return 1

    set_a = set(A)
    n = len(set_a)
    suma = sum(set_a)
    form = ((n +1) * ((n+1) + 1)) // 2
    return form - suma


def solution2(A):
    A.sort()
    min = 1
    for elem in A:
        if elem == min:
            min = min + 1
    return min

def solution3(A):
    set1 = set(range(1, len(A) + 2))
    set_a = set(A)
    diff = set1.difference(set_a)
    mini = min(diff)
    return mini

lista = [1,1,2,4,2,5]

set1 = {1,2,4}
set2 = {1,2,3}

print(solution3(lista))
