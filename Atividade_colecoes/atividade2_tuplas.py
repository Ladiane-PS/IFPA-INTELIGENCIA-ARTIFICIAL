# Criando uma tupla com elementos duplicados
mensagens = ("Coragem", "Fé", "Amor", "Coragem", "Gratidão", "Fé")

# Usando o método count() para contar quantas vezes uma palavra aparece
quantidade_coragem = mensagens.count("Coragem")

# Usando o método index() para encontrar o índice da primeira ocorrência de uma palavra
indice_fe = mensagens.index("Fé")

# Mostrando os resultados
print("Tupla original:", mensagens)
print("Quantidade de vezes que 'Coragem' aparece:", quantidade_coragem)
print("Índice da primeira ocorrência de 'Fé':", indice_fe)

# Comentários:
# Linha 2: Criamos uma tupla chamada 'mensagens' com palavras motivacionais, incluindo algumas repetidas.
# Linha 5: Usamos o método count() para saber quantas vezes a palavra 'Coragem' aparece na tupla.
# Linha 8: Usamos o método index() para descobrir em que posição aparece pela primeira vez a palavra 'Fé'.
# Linhas 11-13: Exibimos a tupla e os resultados dos métodos count() e index() no terminal.
