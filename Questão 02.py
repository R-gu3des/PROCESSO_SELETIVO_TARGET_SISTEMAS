"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

def verifica_numero_fibonacci(numero_analisado):

    # Inicializa os dois primeiros números da sequência de Fibonacci
    num_a, num_b = 0, 1

    # Loop para verificar se o número está na sequência
    while num_a <= numero_analisado:
        if num_a == numero_analisado:
            return True  # O número pertence à sequência de Fibonacci
        # Avança para o próximo número na sequência
        num_a, num_b = num_b, num_a + num_b

    return False  # O número não pertence à sequência de Fibonacci


# Solicita ao usuário um número para verificar
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: ").strip())

# Verifica se o número pertence à sequência de Fibonacci
e_fibonacci = verifica_numero_fibonacci(numero)

# Exibe o resultado com base na verificação
if e_fibonacci:
    print(f'O número {numero} pertence à sequência de Fibonacci.')
else:
    print(f'O número {numero} não pertence à sequência de Fibonacci.')