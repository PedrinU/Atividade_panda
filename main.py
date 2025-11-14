import pandas as pd

# ---ARQUIVO CSV ---
NOME_ARQUIVO = 'Jogadores.csv'

try:
    # Lendo o arquivo CSV diretamente da mesma pasta
    df = pd.read_csv(
        NOME_ARQUIVO,
        sep=';',
        na_values=['null'],
        skipinitialspace=True,
        encoding='utf-8'
    )

    # --- LIMPEZA DE DADOS
    df['salario_do_jogador'] = pd.to_numeric(
        df['salario_do_jogador'], errors='coerce')

    # 1. Nome e time dos jogadores que possuem salário acima de R$ 200.000,00
    filtro_salario_alto = df['salario_do_jogador'] > 200000.00
    jogadores_salario_alto = df[filtro_salario_alto][[
        'nome_do_jogador', 'nome_time_jogador']]

    print("\n" + "="*50 + "\n")
    print("1. Jogadores com salário acima de R$ 200.000,00:")
    print(jogadores_salario_alto.to_string(index=False))
    print("\n" + "="*50 + "\n")

    # 2. Nome e salário dos jogadores dos times de Minas Gerais (MG)
    filtro_estado = df['nome_estado_jogador'] == 'MG'
    jogadores_mg = df[filtro_estado][['nome_do_jogador', 'salario_do_jogador']]

    print("2. Jogadores dos times de Minas Gerais (MG):")
    print(jogadores_mg.to_string(index=False))
    print("\n" + "="*50 + "\n")

    # 3. Nome e time dos jogadores cujo nome contenha a letra 'u'
    filtro_letra_u = df['nome_do_jogador'].str.contains(
        'u', case=False, na=False)
    jogadores_com_u = df[filtro_letra_u][[
        'nome_do_jogador', 'nome_time_jogador']]

    print("3. Jogadores cujo nome contém a letra 'u':")
    print(jogadores_com_u.to_string(index=False))
    print("\n" + "="*50 + "\n")

    # 4. Nome, salário e time dos jogadores, ordenados pelo salário (decrescente)
    ordenado_por_salario = df.sort_values(
        by='salario_do_jogador',
        ascending=False,
        na_position='last'
    )[['nome_do_jogador', 'salario_do_jogador', 'nome_time_jogador']]

    print("4. Jogadores ordenados por Salário (Decrescente):")
    print(ordenado_por_salario.to_string(index=False))
    print("\n" + "="*50 + "\n")

    # 5. Nome, salário e time dos jogadores, ordenados pelo nome do time (crescente)
    ordenado_duplo = df.sort_values(
        by=['nome_time_jogador', 'salario_do_jogador'],
        ascending=[True, False],
        na_position='last'  # Coloca NaNs de time ou salário por último
    )[['nome_do_jogador', 'salario_do_jogador', 'nome_time_jogador']]

    print("5. Jogadores ordenados por Time (Crescente) e Salário (Decrescente):")
    print(ordenado_duplo.to_string(index=False))
    print("\n" + "="*50 + "\n")

    # 6. A quantidade de jogadores por time
    contagem_por_time = df.groupby('nome_time_jogador')[
        'nome_do_jogador'].count().reset_index(name='Quantidade_Jogadores')
    print("6. Quantidade de jogadores por time:")
    print(contagem_por_time.to_string(index=False))
    print("\n" + "="*50 + "\n")

    # 7. A média salarial por time
    media_salarial_por_time = df.groupby('nome_time_jogador')[
        'salario_do_jogador'].mean().reset_index(name='Media_Salarial')

    print("7. Média salarial por time:")
    # Formatação para BRL com separador de milhares e duas casas decimais
    print(media_salarial_por_time.to_string(index=False, float_format='R$ {:,.2f}'.format).replace(
        '.', '_').replace(',', '.').replace('_', ','))

except FileNotFoundError:
    print(f"ERRO: Arquivo '{NOME_ARQUIVO}' não encontrado.")
    print("Certifique-se de que o arquivo CSV está na mesma pasta do script Python.")
except Exception as e:
    print(f"Ocorreu um erro ao processar os dados: {e}")
