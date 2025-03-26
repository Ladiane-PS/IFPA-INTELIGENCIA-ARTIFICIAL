# algoritmo de busca linear para IA

def busca_linear(lista, alvo):
    """
    Realiza uma busca linear em uma lista para encontrar um alvo.

    Args:
        lista: A lista para pesquisar.
        alvo: O valor a ser procurado na lista.

    Returns:
        O índice do alvo na lista se encontrado, caso contrário, -1.
    """

    # Percorre cada elemento da lista usando seu índice
    for i in range(len(lista)):
        # Compara o elemento atual com o alvo
        if lista[i] == alvo:
            # Se o elemento for igual ao alvo, retorna o índice
            return i  
    # Se o alvo não for encontrado após percorrer toda a lista, retorna -1
    return -1  


# Exemplo de uso:
minha_lista = [2, 5, 7, 1, 9, 4, 6]  # Define a lista para busca
alvo = 9  # Define o valor a ser procurado

indice = busca_linear(minha_lista, alvo)  # Chama a função de busca

# Verifica o resultado da busca e imprime a mensagem correspondente
if indice != -1:
    print(f"O alvo {alvo} foi encontrado no índice {indice}.")
else:
    print(f"O alvo {alvo} não foi encontrado na lista.")
