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
    sort_a = sorted(A)
    lista1 = [x for x in range(min(A), max(A) + 1)]
    if sort_a == lista1:
        return max(lista1) + 1
    pass


lista = [7,6,8,5,4]

print(solution(lista))
