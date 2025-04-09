def busca_binaria(lista_ordenada, alvo):  
    # Define a função que realiza a busca binária em uma lista ORDENADA.
    
    esquerda, direita = 0, len(lista_ordenada) - 1  
    # Define os limites da busca:
    # 'esquerda' começa no primeiro índice (0)
    # 'direita' começa no último índice (len(lista) - 1)

    while esquerda <= direita:  
        # Enquanto ainda houver elementos dentro do intervalo de busca...

        meio = (esquerda + direita) // 2  
        # Calcula o índice do meio da lista.
        # O operador // faz divisão inteira (descarta os decimais).

        valor_meio = lista_ordenada[meio]  
        # Obtém o valor que está no meio da lista.

        if valor_meio == alvo:  
            return meio  
            # Se o valor do meio for o procurado, retorna o índice.

        elif valor_meio < alvo:  
            esquerda = meio + 1  
            # Se o valor do meio for menor que o procurado,
            # ajusta 'esquerda' para ignorar a metade esquerda da lista.

        else:  
            direita = meio - 1  
            # Se o valor do meio for maior que o procurado,
            # ajusta 'direita' para ignorar a metade direita da lista.

    return -1  
    # Se o loop terminar sem encontrar o valor, retorna -1 (valor não encontrado).

# Exemplo de uso:
dados_ordenados = [1, 3, 5, 7, 9, 11, 13, 15]  
# Lista ordenada onde será feita a busca.

valor_procurado = 9  
# Define o valor que queremos encontrar.

posicao = busca_binaria(dados_ordenados, valor_procurado)  
# Chama a função e armazena o resultado na variável 'posicao'.

print(f"Valor {valor_procurado} encontrado na posição {posicao}" if posicao != -1 else "Valor não encontrado")  
# Se o valor foi encontrado, imprime a posição; caso contrário, avisa que não foi encontrado.



# algoritmo de busca binária só é recomendado em listas  ordenadas,