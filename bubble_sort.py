def bubble_sort(lista):
    """
    Ordena uma lista usando o método Bubble Sort.
    
    Args: 
    lista (list): Lista a ser ordenada.
    
    Returns: 
    list: Lista ordenada.
    """
    n = len(lista)  # Obtém o tamanho da lista, que é necessário para definir o número de iterações do algoritmo
    for i in range(n):  # Laço externo que repete o processo de comparação e troca várias vezes
        # Flag para otimização - verifica se houve troca
        trocou = False  # Variável usada para verificar se ocorreu troca na iteração
        
        # Laço interno que percorre a lista até o penúltimo elemento não ordenado
        for j in range(0, n-i-1):  # A cada iteração do laço externo, o número de elementos a serem comparados diminui
            if lista[j] > lista[j+1]:  # Se o elemento atual for maior que o próximo
                # Troca os elementos de posição, colocando o maior à direita
                lista[j], lista[j+1] = lista[j+1], lista[j]  
                trocou = True  # Marca que houve uma troca
        
        # Se nenhuma troca foi realizada, significa que a lista já está ordenada
        if not trocou:  
            break  # Interrompe o laço externo, pois a lista já está ordenada
    
    return lista  # Retorna a lista ordenada após as iterações

# Exemplo de uso
dados = [64, 34, 25, 12, 22, 11, 90]  # Lista de números desordenada
print("Lista original:", dados)  # Exibe a lista antes da ordenação

# Chama a função bubble_sort para ordenar a lista
dados_ordenados = bubble_sort(dados)

# Exibe a lista ordenada após o algoritmo
print("Lista ordenada:", dados_ordenados)

