"""
Exercício 4 – Debugging Avançado com map, filter e reduce

Objetivo:
O código a seguir tem a intenção de:
    1. Solicitar ao usuário uma lista de números separados por vírgula.
    2. Converter essa entrada em uma lista de inteiros.
    3. Utilizar a função map para calcular o quadrado de cada número.
    4. Utilizar a função filter para selecionar apenas os quadrados que são pares.
    5. Utilizar a função reduce para somar todos os quadrados pares.
    6. Calcular e exibir a média dos quadrados pares (esta parte está ausente e deve ser implementada).


Contudo, o código apresenta diversos erros que impedem sua execução correta.

Tarefas:
    - Identifique e corrija os erros de conversão de tipos, sintaxe e lógica presentes.
    - Adicione 2 ou 3 linhas de código para calcular a média dos quadrados pares e exiba esse resultado.
    - Insira comentários explicando as correções e as novas linhas adicionadas.


Código com erros:
--------------------------------------------------

numbers_input = input("Digite uma lista de números separados por vírgula: ")

# O código a seguir tenta processar a entrada do usuário,
# mas não converte os elementos para inteiros.
numbers_list = numbers_input.split(",")

squared_numbers = map(lambda x: x ** 2, numbers_list)

even_numbers = filter(x % 2 == 0, squared_numbers)

total = functools.reduce(lambda x, y: x + y) even_numbers

print "Soma dos quadrados pares:", total
--------------------------------------------------

Após corrigir os erros e adicionar as linhas para calcular a média, o programa deverá:
    - Exibir a soma dos quadrados pares.
    - Exibir a média dos quadrados pares (soma dividida pelo número de elementos filtrados).

Boa sorte e bons estudos!
"""

from functools import reduce

numbers_input = input("Digite uma lista de números separados por vírgula: ")

numbers_list = numbers_input.split(",")

squared_numbers = map(lambda x: x ** 2, numbers_list)

even_numbers = list(filter(lambda x: x % 2 == 0, squared_numbers)) #filter sem lambda

total = reduce(lambda x, y: x + y, even_numbers) #reduce com erros nos paranteses



