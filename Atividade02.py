# 1. Função que retorna os números ímpares de uma lista
def numeros_impares(lista):
    return [x for x in lista if x % 2 != 0]

# 2. Função que retorna os números primos de uma lista
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def numeros_primos(lista):
    return [x for x in lista if eh_primo(x)]

# 3. Função que retorna elementos únicos entre duas listas
def elementos_unicos(lista1, lista2):
    return list(set(lista1) ^ set(lista2))

# 4. Função para encontrar o segundo maior valor de uma lista
def segundo_maior(lista):
    lista_unica = list(set(lista))
    lista_unica.sort()
    return lista_unica[-2] if len(lista_unica) >= 2 else None

# 5. Função que ordena lista de tuplas (nome, idade) pelo nome
def ordenar_por_nome(lista_tuplas):
    return sorted(lista_tuplas, key=lambda x: x[0].lower())

# 6. Como identificar e tratar outliers em uma coluna numérica usando desvio padrão ou quartis?
# Outliers podem ser identificados usando o desvio padrão ou os quartis. Com desvio padrão, considera-se como outliers os valores que estão fora de 3 desvios padrão da média. Com quartis, utiliza-se o IQR (intervalo interquartil), e valores fora de 1.5x o IQR abaixo do primeiro quartil ou acima do terceiro quartil são considerados outliers. Esses valores podem ser removidos ou tratados (ex: substituídos por média/mediana).

# 7. Como concatenar vários DataFrames (empilhando linhas ou colunas), mesmo que tenham colunas diferentes?
# Para concatenar DataFrames em pandas, utiliza-se a função pd.concat(). Quando axis=0, os DataFrames são empilhados por linhas (um embaixo do outro). Quando axis=1, são empilhados por colunas (um ao lado do outro). Se os DataFrames tiverem colunas diferentes, os valores ausentes serão preenchidos com NaN automaticamente.

# 8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?
# A leitura de um arquivo CSV em pandas é feita com a função pd.read_csv('caminho_do_arquivo.csv'). Após carregado, as primeiras linhas podem ser visualizadas com o método .head(), que exibe por padrão os 5 primeiros registros do DataFrame.

# 9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um DataFrame com base em uma condição?
# Para selecionar uma coluna específica, basta usar a notação df['nome_coluna']. Para filtrar linhas, aplica-se uma condição lógica como df[df['coluna'] > valor], retornando apenas as linhas que satisfazem essa condição.

# 10. Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?
# Valores ausentes (NaN) podem ser tratados de várias formas: removendo as linhas com df.dropna(), preenchendo com um valor específico usando df.fillna(valor), ou analisando sua ocorrência com df.isna().sum(). A escolha do tratamento depende do contexto dos dados e do impacto da ausência de valores.
