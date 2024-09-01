"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

def inverte_texto(texto):
    return texto[::-1]

# Solicita ao usuário que insira um texto
entrada = input('Digite um texto para ver como ele fica de trás para frente: ').strip()

# Inverte e exibe o texto inserido pelo usuário
print(inverte_texto(entrada))