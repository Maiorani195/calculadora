num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operação = int(input("Escolha a operação (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))
if operação == 1:
    resultado = num1 + num2
    print(f"A soma de {num1} e {num2} é {resultado}")
elif operação == 2:
    resultado = num1 - num2
    print(f"A subtração de {num1} e {num2} é {resultado}")
elif operação == 3:
    resultado = num1 * num2
    print(f"A multiplicação de {num1} e {num2} é {resultado}")
elif operação == 4:
    resultado = num1 / num2
    print(f"A divisão de {num1} por {num2} é {resultado}")
else:
    print("Operação inválida!")
