"""
Exercício 2 – Agrupando Argumentos por Tipo

Objetivo:
Crie uma função chamada `separar_tipos` que receba um número arbitrário de argumentos posicionais e retorne um dicionário com duas chaves:
    - 'numeros': contendo uma lista com todos os argumentos que são do tipo int ou float;
    - 'strings': contendo uma lista com todos os argumentos que são do tipo str.
    
Observação:
- Argumentos de outros tipos devem ser ignorados.

Exemplo de chamada:
    resultado = separar_tipos(10, 'Python', 3.14, True, 'Teste', 42)
    print(resultado)
    # Saída esperada: {'numeros': [10, 3.14, 42], 'strings': ['Python', 'Teste']}
    
Requisitos:
- Use estruturas condicionais e funções built-in (como isinstance) para classificar os argumentos.
"""
# Sua solução aqui

def separar_tipos(*args):
    numeros = 0
    strings = 0
    for i in args:
        if isinstance(i, int):
            numeros += separar_tipos(i)
    for a in args:
        if isinstance(i, str):
            strings += separar_tipos(a)
    total = {
        "numeros": numeros,
        "strings": strings
    }
    return total

lista = 10, 'Python', 3.14, True, 'Teste', 42
print(separar_tipos(lista))