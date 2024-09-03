
def calculadora ():
    

    print ("1 - Soma")
    print ("2 - subtração:")
    print ("3 - multiplicação")
    print ("4 - divisão")
    print ("0 - sair")
    calculo = input("Escolha a opção desejada: 1, 2, 3, 4")
    n1 = float(input("Digite o primeiro número:"))
    n2 = float(input("Digite o segundo número:"))
    
    if calculo == 1:
        return n1 + n2
    elif calculo == 2:
        return n1 - n2
    elif calculo == 3:
        return n1 * n2
    elif calculo == 3:
        return n1 / n2 if n2 != 0 else '0'
    
    else:
        return 0
    
    