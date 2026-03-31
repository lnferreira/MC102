n = int(input("Digite um número inteiro positivo : "))
fator = 2
# Enquanto n for diferente de 1, continua a fatoração
while n != 1:
    # Verifica se o fator é primo
    for divisor in range(2, int(fator**0.5) + 1):
        # Se o fator for divisível por algum número entre 2 e a raiz quadrada do fator, ele não é primo
        if fator % divisor == 0:
            break
    # Se o fator for primo
    else:
        # Verifica se o fator é um divisor de n
        while n % fator == 0:
            print(fator)
            n = n / fator
    fator = fator + 1
