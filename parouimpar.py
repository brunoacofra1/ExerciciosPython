num =  input("Digite um numero: ")
try:
    num = int(num)
    if num % 2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é impar")
except ValueError:
    print(f"{num} não é um numero")