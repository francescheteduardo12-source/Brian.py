def funcao_infinita(contador):
    print(f"Chamada número: {contador}")
    # ERRO: Não existe 'if' para parar!
    funcao_infinita(contador + 1)


funcao_infinita(1)
