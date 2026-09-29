def soma_ate(n):
    # 1. CASO BASE: se n for 1, retorna 1
    if n == 1:
        return 1
    # 2. PASSO RECURSIVO: n + soma_ate(n - 1)
    else:
        return n + soma_ate(n - 1)


# Teste seu programa:
resultado = soma_ate(5)
print(f"A soma acumulada é: {resultado}")
