'''
Um sapo pequeno quer chegar ao outro lado de um rio. O sapo está inicialmente localizado em uma margem
do rio (posição 0) e deseja chegar à margem oposta (posição X + 1). As folhas caem de uma árvore na
superfície do rio.

Você recebe uma matriz A que consiste em N números inteiros representando as folhas que caem. A [K]
representa a posição em que uma folha cai no tempo K, medida em segundos.

O objetivo é encontrar o primeiro momento em que o sapo possa pular para o outro lado do rio. O sapo pode
atravessar apenas quando as folhas aparecem em todas as posições do rio, de 1 a X (ou seja, queremos
encontrar o momento inicial em que todas as posições de 1 a X são cobertas por folhas). Você pode supor
que a velocidade da corrente no rio é insignificante, ou seja, as folhas não mudam de posição quando
caem no rio.

Por exemplo, você recebe o número inteiro X = 5 e a matriz A de modo que:

  A [0] = 1
  A [1] = 3
  A [2] = 1
  A [3] = 4
  A [4] = 2
  A [5] = 3
  A [6] = 5
  A [7] = 4
No segundo 6, uma folha cai na posição 5. É a primeira vez que as folhas aparecem em todas as posições
do outro lado do rio.

Escreva uma função:

solução def (X, A)

que, dada uma matriz não vazia A que consiste em N números inteiros e número inteiro X, retorna o
primeiro tempo em que o sapo pode pular para o outro lado do rio.

Se o sapo nunca for capaz de pular para o outro lado do rio, a função deve retornar -1.

Por exemplo, dado X = 5 e matriz A de modo que:

  A [0] = 1
  A [1] = 3
  A [2] = 1
  A [3] = 4
  A [4] = 2
  A [5] = 3
  A [6] = 5
  A [7] = 4
a função deve retornar 6, conforme explicado acima.

Escreva um algoritmo eficiente para as seguintes suposições:

N e X são números inteiros dentro do intervalo [1..100.000];
cada elemento da matriz A é um número inteiro dentro do intervalo [1..X].
'''

# def solution(X, A):
#     if sum(A) == X * len(A):
#         return -1
#
#     if A:
#         for n in A:
#             if X == n:
#                 return A.index(n)
#     return -1

l1 = [2,2,2,2,2]
l2 = [1,3,5,7,9,10]
l3 = [1,2,3,45,6,7,8]
l4 = [1,3,1,5,8,1,5,9]

def solution(X, A):
    pos = set()
    for i, j in enumerate(A):
        pos.add(j)
        if len(pos) == X:
            return i
    return -1

print(solution(2, l2))
