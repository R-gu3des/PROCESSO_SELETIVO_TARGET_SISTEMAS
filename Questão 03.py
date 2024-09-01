import pandas as pd

"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

def calcular_faturamento(caminho_arquivo):
    # Lê o arquivo JSON e cria um DataFrame
    df = pd.read_json(caminho_arquivo)
    
    # Filtra os dias com faturamento positivo
    df_filtrado = df[df['faturamento'] > 0]
    
    if df_filtrado.empty:
        return None, None, 0  # Retorna None para menor e maior, e 0 para dias acima da média se não há dados
    
    # Calcula o menor e o maior valor de faturamento
    menor_faturamento = df_filtrado['faturamento'].min()
    maior_faturamento = df_filtrado['faturamento'].max()
    
    # Calcula a média mensal, ignorando dias sem faturamento
    media_mensal = df_filtrado['faturamento'].mean()
    
    # Conta o número de dias com faturamento acima da média
    dias_acima_media = df_filtrado[df_filtrado['faturamento'] > media_mensal].shape[0]
    
    return menor_faturamento, maior_faturamento, dias_acima_media


# Caminho para o arquivo JSON com os dados de faturamento
caminho_arquivo = 'data/dados_faturamento.json'

# Calcula os valores necessários
menor_faturamento, maior_faturamento, dias_acima_media = calcular_faturamento(caminho_arquivo)

# Exibe os resultados
if menor_faturamento is not None and maior_faturamento is not None:
    print(f"Menor valor de faturamento: {menor_faturamento}")
    print(f"Maior valor de faturamento: {maior_faturamento}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
else:
    print("Não há dados de faturamento disponíveis para o cálculo.")