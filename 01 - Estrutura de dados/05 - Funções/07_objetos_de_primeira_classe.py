def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def teste(a, b):
    return a*2 + b*3

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")


exibir_resultado(20, 10, somar)  # O resultado da operação é = 30
exibir_resultado(20, 10, subtrair)  # O resultado da operação é = 10
exibir_resultado(20, 10, teste)  # O resultado da operação é = 70

operacao = somar

print(operacao(2, 30)) # 32