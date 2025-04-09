# =====================================================
# ATIVIDADE 5 – ALGORITMO USANDO CONJUNTO E STRING
# =====================================================

# Objetivo: Criar um conjunto com nomes de frutas,
# padronizar todos para letras maiúsculas e mostrar
# apenas os nomes que começam com a letra "M".

# Criando um conjunto com nomes de frutas variados
frutas = {"maçã", "banana", "melancia", "morango", "kiwi", "manga"}

# Exibindo o conjunto original (sem ordem garantida)
print("\nConjunto original de frutas:")
print(frutas)

# Usamos set comprehension para:
# - Converter cada fruta para MAIÚSCULAS (upper)
# - Filtrar apenas as que começam com "M"
frutas_com_m = {f.upper() for f in frutas if f.upper().startswith("M")}

print("\nFrutas que começam com 'M' (em maiúsculas):")
print(frutas_com_m)  # Resultado: {'MELANCIA', 'MANGA', 'MAÇÃ', 'MORANGO'}


print("\n" + "="*60)

# =====================================================
# ATIVIDADE 5 – ALGORITMO USANDO DICIONÁRIO E STRING
# =====================================================

# Objetivo: Criar um dicionário de pessoas com nome e telefone.
# Formatar os nomes com title() e os telefones com zfill().

# Criando um dicionário onde:
# - chave: nome da pessoa (sem formatação)
# - valor: número de telefone (sem zeros à esquerda)
contatos = {
    "ana": "91234",
    "bruno": "87541",
    "carla": "78123"
}

print("\nContatos formatados:")

# Iteramos sobre o dicionário original para formatar os dados
for nome, telefone in contatos.items():
    nome_formatado = nome.title()         # Primeira letra maiúscula
    telefone_formatado = telefone.zfill(9)  # Preenche com zeros até ter 9 dígitos
    print(f"Nome: {nome_formatado} | Telefone: {telefone_formatado}")

