def busca_linear(lista, valor_procurado):
    """
    Função que realiza uma busca linear em uma lista.
    Retorna o índice do valor procurado ou -1 se não for encontrado.
    """
    for indice, valor in enumerate(lista):  # Percorre a lista obtendo índice e valor
        if valor == valor_procurado:  # Se encontrar o valor procurado
            return indice  # Retorna o índice onde o valor foi encontrado
    return -1  # Retorna -1 se o valor não estiver na lista

# Definição da lista de números
numeros = [10, 20, 30, 40, 50]

# Valor que queremos encontrar na lista
alvo = 30

# Chamada da função e armazenamento do resultado
resultado = busca_linear(numeros, alvo)

# Impressão do resultado da busca
print(f"O valor {alvo} foi encontrado no índice {resultado}" if resultado != -1
      else f"O valor {alvo} não foi encontrado")
