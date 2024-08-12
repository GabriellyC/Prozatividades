def obter_nome():
    return input("Digite o seu nome completo: ")

def nascimento():
    while True:
        try:
            ano = int(input("Digite o seu ano de nascimento (entre 1922 e 2023): "))
            if 1922 <= ano <= 2023:
                return ano
            else:
                print("Ano inválido. Digite um ano entre 1992 e 2023.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def calculo_idade(ano_nascimento, ano_atual=2024):
    return ano_atual - ano_nascimento

def main():
    nome = obter_nome()
    ano_nascimento = nascimento()
    idade = calculo_idade(ano_nascimento)
    print(f"{nome}, você terá {idade} anos em 2024.")

while True:
    print(main())