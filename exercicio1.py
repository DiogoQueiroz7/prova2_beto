"""
Exercício 1 – Identificando Quadrados Perfeitos

Objetivo:
Crie uma função chamada `classificar_quadrados` que receba uma lista de números inteiros e retorne um dicionário com duas chaves:
    - 'quadrados_perfeitos': contendo os números que são quadrados perfeitos (por exemplo, 1, 4, 9, 16, …);
    - 'nao_quadrados': contendo os demais números.

Requisitos:
- Utilize laços de repetição para percorrer a lista.
- Adicione uma docstring explicando o funcionamento da função.

Exemplo de chamada:
    resultado = classificar_quadrados([1, 2, 3, 4, 8, 9, 15])
    print(resultado)
    # Saída esperada: {'quadrados_perfeitos': [1, 4, 9], 'nao_quadrados': [2, 3, 8, 15]}
    
Importante:
- Não se preocupe com números negativos.
"""
# Sua solução aqui

def classificar_quadrados(lista):
    quadrados = []
    not_quadrado = []
    for i in lista:
        if int(i ** 0.5) ** 2 == i:
            quadrados.append(i)
        else: 
            not_quadrado.append(i)

    return {
        "Quadrados Perefeitos": quadrados,
        "Não Quadrados": not_quadrado
    }

lista = [1, 2, 3, 4, 8, 9, 15]
print(classificar_quadrados(lista))

'''
criei a função para classificar se é ou não é um quadrado perfeito
criei duas variaveis com uma lista vazia
usei um loop com for para verificar todos os elementos (i) na lista
usei condicionais para verificar se o elemento elvado a metade dele e depois ao quyadrado é igual ao proprio elemento
os que sobraram deixei em outra nao lista chamda não é quadrado
depois retornei os resultados em um dicionario
e depois printei a função
'''