# =====================================================
# ATIVIDADE 6 – MÉTODOS DE STRING (STR)
# =====================================================

# =====================================================
# 1. upper() – Deixa tudo em MAIÚSCULO
# =====================================================
texto1 = "python é incrível"
print("\n1. Método upper()")
print("Original:", texto1)
print("Maiúsculas:", texto1.upper())

# =====================================================
# 2. lower() – Deixa tudo em minúsculo
# =====================================================
texto2 = "PROGRAMAÇÃO É LEGAL"
print("\n2. Método lower()")
print("Original:", texto2)
print("Minúsculas:", texto2.lower())

# =====================================================
# 3. strip() – Remove espaços no início e fim
# =====================================================
texto3 = "   Olá, mundo!   "
print("\n3. Método strip()")
print("Original com espaços:", repr(texto3))
print("Sem espaços:", repr(texto3.strip()))

# =====================================================
# 4. replace() – Substitui partes da string
# =====================================================
texto4 = "Aprender Python é divertido"
print("\n4. Método replace()")
print("Original:", texto4)
print("Substituindo 'divertido' por 'poderoso':", texto4.replace("divertido", "poderoso"))

# =====================================================
# 5. split() – Divide uma string em partes (lista)
# =====================================================
texto5 = "banana,maçã,pera,laranja"
print("\n5. Método split()")
print("Original:", texto5)
print("Separado por vírgulas:", texto5.split(","))

# =====================================================
# 6. isdigit() – Verifica se a string contém apenas dígitos
# =====================================================
texto6 = "12345"
texto6b = "123a"
print("\n6. Método isdigit()")
print(f"'{texto6}' só tem números?", texto6.isdigit())
print(f"'{texto6b}' só tem números?", texto6b.isdigit())

# =====================================================
# 7. capitalize() – Primeira letra maiúscula, o resto minúsculo
# =====================================================
texto7 = "bom DIA!"
print("\n7. Método capitalize()")
print("Original:", texto7)
print("Capitalizado:", texto7.capitalize())

