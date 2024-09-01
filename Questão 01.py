"""

1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?

"""

# Define o valor do índice até o qual a soma será calculada
INDICE = 13

# Inicializa a variável SOMA para acumular o total e K para iterar
SOMA = 0
K = 0

# Enquanto K for menor que o índice definido
while K < INDICE:
    # Incrementa K em 1
    K = K + 1
    # Adiciona o valor de K à variável SOMA
    SOMA = SOMA + K

# Imprime o resultado da soma total
print(SOMA)
