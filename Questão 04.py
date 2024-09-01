import pandas as pd

"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
"""


# Dados de faturamento mensal por estado
dados = {
    'Estado': ['SP', 'RJ', 'MG', 'ES', 'Outros'],
    'Faturamento': [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
}

# Cria um DataFrame a partir dos dados
df = pd.DataFrame(dados)

# Calcula o faturamento total
total_faturamento = df['Faturamento'].sum()

# Calcula o percentual de representação de cada estado
df['Percentual'] = (df['Faturamento'] / total_faturamento) * 100


# Exibe o resultado
print(df)