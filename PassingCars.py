"""

Uma matriz não vazia A que consiste em N números inteiros é fornecida. Os elementos consecutivos da matriz A
representam carros consecutivos em uma estrada.

A matriz A contém apenas 0s e / ou 1s:

0 representa um carro viajando para leste,
1 representa um carro viajando para o oeste.
O objetivo é contar carros que passam. Dizemos que um par de carros (P, Q), onde 0 ≤ P <Q <N, passa quando P
está viajando para o leste e Q está viajando para o oeste.

Por exemplo, considere a matriz A de modo que:

  A [0] = 0
  A [1] = 1
  A [2] = 0
  A [3] = 1
  A [4] = 1
Temos cinco pares de carros que passam: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Escreva uma função:

solução def (A)

que, dada uma matriz não vazia A de N números inteiros, retorna o número de pares de carros que passam.

A função deve retornar -1 se o número de pares de carros passantes exceder 1.000.000.000.

Por exemplo, dado:

  A [0] = 0
  A [1] = 1
  A [2] = 0
  A [3] = 1
  A [4] = 1
a função deve retornar 5, conforme explicado acima.

Escreva um algoritmo eficiente para as seguintes suposições:

N é um número inteiro dentro do intervalo [1..100.000];
cada elemento da matriz A é um número inteiro que pode ter um dos seguintes valores: 0, 1.
"""

def solution(A):
    pass


a = [0,1,0,1,1,1,0]
lista_0 = list()

for n in a:
    if n == 0:
        zero = a.pop(a.index(n))
        lista_0.append(zero)

print(a)
print(lista_0)

j = []

for n in zip(a, lista_0):
    j.append(n)

print(j)