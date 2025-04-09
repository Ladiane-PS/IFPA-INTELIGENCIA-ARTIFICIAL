# =====================================================
# ATIVIDADE 3 - TRABALHANDO COM TUPLAS EM PYTHON
# =====================================================

# =====================================================
# PARTE A - Criar uma tupla e mostrar o resultado
# =====================================================

# Criamos uma tupla chamada "mensagens_motivacionais" com frases que não vão mudar (imutáveis)
mensagens_motivacionais = ("Você é capaz!", "Confie em si mesma", "Força vamos que vamos", "Não desista", "Você é luz!")

# Impressão do título com linha decorativa
print("\n" + "="*60)
print("PARTE A - Criar uma tupla e mostrar o resultado".center(60))  # Centraliza o texto no terminal
print("="*60)

# Exibindo a tupla completa
print("Tupla criada:")
print(mensagens_motivacionais)  # Mostra os elementos da tupla no terminal

# =====================================================
# PARTE B.1 - Método count()
# =====================================================

# Criamos outra tupla com alguns valores repetidos para testar o método count()
exemplo_count = ("Confie", "Você", "Confie", "Sorria", "Confie")

# Usamos o método count() para contar quantas vezes a palavra "Confie" aparece na tupla
quantidade_confie = exemplo_count.count("Confie")

# Impressão do título da parte B.1
print("\n" + "="*60)
print("PARTE B.1 - Método count()".center(60))  # Centraliza o texto
print("="*60)

# Mostrando o resultado da contagem
print("Usando count():")
print(f'A palavra "Confie" aparece {quantidade_confie} vezes na tupla.')  # Exibe a quantidade encontrada

# =====================================================
# PARTE B.2 - Método index()
# =====================================================

# Criamos uma nova tupla com palavras únicas
exemplo_index = ("Ame-se", "Sorria", "Acredite", "Brilhe")

# Usamos o método index() para descobrir em qual posição está o elemento "Brilhe"
posicao_brilhe = exemplo_index.index("Brilhe")

# Impressão do título da parte B.2
print("\n" + "="*60)
print("PARTE B.2 - Método index()".center(60))  # Centraliza o texto
print("="*60)

# Exibimos a posição onde "Brilhe" aparece na tupla
print("Usando index():")
print(f'A palavra "Brilhe" está na posição {posicao_brilhe} da tupla.')  # Mostra o índice

# Linha final para separar se tiver mais saída depois
print("="*60)

# =====================================================
# PARTE C - Diferença entre Lista e Tupla
# =====================================================

# Comentário explicativo com várias diferenças entre tupla e lista
"""
Diferença entre lista e tupla:

- Tupla:
  * É imutável (não dá pra alterar depois de criada)
  * Usa parênteses: exemplo = (1, 2, 3)
  * É mais rápida e consome menos memória
  * Ideal para dados fixos, como coordenadas ou configurações

- Lista:
  * É mutável (podemos adicionar, remover ou alterar elementos)
  * Usa colchetes: exemplo = [1, 2, 3]
  * Ideal quando os dados mudam com frequência

Exemplo prático:
"""

# Lista (estrutura mutável)
lista_exemplo = ["Brilhe", "Sonhe", "Vença"]
lista_exemplo.append("Supere")  # Adiciona um novo item à lista
print("Lista após append():", lista_exemplo)  # Exibe a lista modificada

# Tupla (estrutura imutável)
tupla_exemplo = ("Brilhe", "Sonhe", "Vença")
# tupla_exemplo.append("Supere")  # Isso daria erro, pois tuplas não aceitam append()

# Mostramos que a tupla continua igual, sem alterações
print("Tupla original (imutável):", tupla_exemplo)
