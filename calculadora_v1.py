# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

operacao_desejada = 0
resultado = 0

def calcular(n1, n2, operacao):
    if operacao == "1":
        resultado = f"{n1} + {n2} = {(n1 + n2):.2f}"
        return resultado
    elif operacao == "2":
        resultado = f"{n1} - {n2} = {(n1 - n2):.2f}"
        return resultado
    elif operacao == "3":
        resultado = f"{n1} * {n2} = {(n1 * n2):.2f}"
        return resultado
    else:
        if n2 == 0:
            return "\nNão é possível dividir por 0."
        else:
            resultado = f"{n1} / {n2} = {(n1 / n2):.2f}"
            return resultado
    
print("\n******************* Calculadora em Python *******************\n")

print("Selecione o número da operação desejada:")

print("\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")

operacao_desejada = input("Digite sua opção (1/2/3/4): ").strip()

if operacao_desejada.isnumeric():
    if int(operacao_desejada) in range(1, 5):
        primeiro_numero = input("\nDigite o primeiro número: ").strip()
        segundo_numero = input("\nDigite o segundo número: ").strip()

        if primeiro_numero.isnumeric() and segundo_numero.isnumeric():
            primeiro_numero = float(primeiro_numero)
            segundo_numero = float(segundo_numero)

            print(calcular(primeiro_numero, segundo_numero, operacao_desejada))
        else:
            print("\nDigite apenas números!")
    else:
        print("Opção inválida!")
else:
    print("\nDigite apenas números!")
