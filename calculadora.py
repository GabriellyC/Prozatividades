def calculadora():

    calculo = int(input("Escolha a opção desejada( 1-soma, 2 - subtração, 3 - multiplicação, 4- divisão, 0 - sair): "))

    if calculo == 0:
        return

    n1 = float(input("Digite o primeiro número: "))
    if n1 == 0:
        return 'Digite um número válido!'
    n2 = float(input("Digite o segundo número: "))
    if n2 == 0:
        return 'Digite um número válido!'

    if calculo == 1:
        return n1 + n2
    elif calculo == 2:
        return n1 - n2
    elif calculo == 3:
        return n1 * n2
    elif calculo == 4:
        return n1 / n2
    else:
        return 0

while True:
    print(calculadora())