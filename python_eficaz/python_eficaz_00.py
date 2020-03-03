
"""
Ao fatiar uma lista incluindo na fatia seu inicio, você deve suprimir o índice zero para reduzir a
poluição visual.
"""

lista1 = [1, 2, 3, 4, 5]

print(lista1[0:3])  # --> Errado
print(lista1[:3])  # --> Certo

print(lista1[3:len(lista1)])  # --> Errado
print(lista1[3:])  # --> Certo


# ---------------------------------------------------------------------------------------------------

"""
Use abrangência de lista em vez de mapa e filter. Elas são mais fáceis de ler que as funções map e filter
porque não precisam de expressões lambda auxiliares.
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista2 = map(lambda x: x, filter( lambda x: x > 0, my_list))

lista2_2 = [x for x in my_list if x > 0]

# ---------------------------------------------------------------------------------------------------

"""
Dica: Considere usar expressões geradoras em abrangências muito grandes. As abrangências podem causar
problemas quando o fluxo de dados na entrada for muito intenso, consumindo muita memória.
As geradoras evitam os problemas porque devolvem um iterador que produz apenas um valor por vez.
"""

# new_list = (x for x in open('arquivo.csv'))

# ---------------------------------------------------------------------------------------------------

"""
prefira enumerate em vez de range. Ele oferece uma sintaxe concisa para laços em iteradores e para obter
índice de cada item do iterador durante o andamento da varredura.
"""

my_list_2 = [x for x in range(1,21,2)]

for i, j in enumerate(my_list_2, 1):
    pass

# ---------------------------------------------------------------------------------------------------

"""
Use zíper para processar iteradores em paralelo. --> Retornará uma sequência de tuplas
"""

x = [1, 2, 3]
y = [6, 7, 8]

lista_zip_x_y = list(zip(x, y))

#print(lista_zip_x_y)

for i in zip(x, y):
    #print(i)
    pass

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}

# Exemplo demonstrando como inverter a ordem de um dict --> chave vira valor e vice-versa. Usando zip()
prices_invertido = dict(zip(prices.values(), prices.keys()))

print(prices_invertido)
print(prices)

# ---------------------------------------------------------------------------------------------------

"""
Dicionários --> Arrays associativos --> Key / Value
Podemos utilizar essa técnica para substituir muitos if, um dicionário pode ter Classes, Funções, Dados
e até outros dicionário. Utilize um dicionário de funções para substituir if/elifs quando necessário
determinar o valor de algum case para executar uma determinada função.
"""

# name = input("name: ")
#
#
# # -- Errado
# if name == "John":
#    print ("This is John, he is an artist")
# elif name == "Ted":
#    print ("This is Ted, he is an engineer")
# elif name == "Kennedy":
#    print ("This is Kennedy, he is a teacher")
#
# # -- Correto
# name_job_dict = {
#    "Josh": "This is John, he is an artist",
#    "Ted": "This is Ted, he is an engineer",
#    "Kenedy": "This is Kennedy, he is a teacher",
# }
# print(name_job_dict[name])

# ---------------------------------------------------------------------------------------------------

"""
Às vezes você precisa iterar sobre uma lista e ao mesmo tempo obter o índice de cada elemento. 
Em vez de fazer:
"""

mylist = [x for x in range(1,13)]

i = 0
for element in mylist: # --> Errado não tá, porém...
    # ....
    i += 1

print(i)

''' Podemos simplesmente fazer: '''

for i, j in enumerate(mylist): # --> Correto
    pass

# ---------------------------------------------------------------------------------------------------

"""
CLASSIFICAÇÃO DE LISTAS:

É bastante comum classificar uma lista com base em uma das características de seus elementos.
Aqui, por exemplo, criamos uma lista de pessoas:
"""

class Person(object):
    def __init__(self, age):
        self.age = age

p1 = Person(21)

persons = [Person(age) for age in (14, 78, 42)]

print(persons)

# https://lucasbiason.github.io/eficaz000-sequencias-conjunto-dados/