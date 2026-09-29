def criar_usuario():
    nome_usuario = "Eduardo"
    nivel_acesso = "Admin"
    print("--- DENTRO DA FUNÇÃO ---")
    print(f"Usuário criado: {nome_usuario} ({nivel_acesso})")
    return nome_usuario, nivel_acesso


nome, nivel = criar_usuario()

print("--- FORA DA FUNÇÃO ---")
print(nome)
