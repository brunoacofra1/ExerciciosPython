numbers = []
for _ in range(4):
    while True:
        x = input("Digite um numero: ")
        try:
            x = int(x)
            break
        except ValueError:
            print(f"{x} não é um numero")

    numbers.append(x)
soma = sum(numbers)
print(f'A soma de todos os numeros é {soma}')
print(numbers)