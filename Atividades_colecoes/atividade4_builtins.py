# =====================================================
# ATIVIDADE 4 – BUILT-INS EM COLEÇÕES (PYTHON)
# =====================================================

# =====================================================
# 1. Built-in len() com SET
# =====================================================
animais = {"gato", "cachorro", "pássaro", "peixe"}
print("\n1. Usando len() com um conjunto (set)")
print("Conjunto de animais:", animais)
print("Quantidade de animais:", len(animais))  # Conta quantos elementos há no set

# =====================================================
# 2. Built-in sum() com SET
# =====================================================
numeros = {10, 20, 30, 40}
print("\n2. Usando sum() com um conjunto de números")
print("Conjunto de números:", numeros)
print("Soma total:", sum(numeros))  # Soma todos os valores do set

# =====================================================
# 3. Built-in sorted() com SET
# =====================================================
cores = {"vermelho", "azul", "amarelo", "verde"}
print("\n3. Usando sorted() para ordenar elementos do set")
print("Cores desordenadas (set):", cores)
print("Cores ordenadas (lista):", sorted(cores))  # Retorna lista ordenada

# =====================================================
# 4. Built-in keys() com DICT
# =====================================================
pessoa = {"nome": "Ana", "idade": 30, "cidade": "São Paulo"}
print("\n4. Usando keys() para acessar as chaves de um dicionário")
print("Dicionário da pessoa:", pessoa)
print("Chaves do dicionário:", list(pessoa.keys()))  # Retorna as chaves como nome: , idade: , cidade:

# =====================================================
# 5. Built-in values() com DICT
# =====================================================
print("\n5. Usando values() para acessar os valores de um dicionário")
print("Dicionário da pessoa:", pessoa)
print("Valores do dicionário:", list(pessoa.values()))  # Retorna os valoreas como Ana, 30, São Paulo

