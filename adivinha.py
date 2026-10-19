import random

numero = random.randint(1,20)

for _ in range(3):
    escolha = input("Digite um numero e tente adivinhar o numero: ")
    while True:
        try:
            escolha = int(escolha)
            break
        except ValueError:
            print(f"{escolha} Não é um numero")
    print(numero)
    if escolha == numero:
        print(f"Parabens Você acertou o numero, era{numero}")
        break
    elif escolha > numero:
        print(f"{escolha} é maior que o numero")
    else:
        print(f"{escolha} é menor que o numero")
else:
    print(f"Acabaram as tentativas o numero era {numero}")