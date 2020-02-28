def solution(a, k):
    n_bin = bin(a)[2:]
    list_bin = [x for x in n_bin]
    rotate = ''

    for times in range(k):
        n = list_bin.pop(-1)
        list_bin.insert(0, n)

    for number in list_bin:
        rotate = rotate + number

    return f'{a} = {n_bin} --> rotação de {k} vezes resultou em {rotate} que equivale a {int(rotate, 2)}'

# Example test.
# Output : 20 = 10100 --> rotação de 2 vezes resultou em 00101 que equivale a 5
print(solution(20, 2))
