import meu_modulo_calculadora

def main(): 
    a = 10
    b = 5
    print("Soma:", meu_modulo_calculadora.somar(a, b))
    print("Subtração:", meu_modulo_calculadora.subtrair(a, b))
    print("Multiplicação:", meu_modulo_calculadora.multiplicar(a, b))
    print("Divisão:", meu_modulo_calculadora.dividir(a, b))

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: ")) 
    operacao = input("Digite a operação (+, -, *, /): ")

    match operacao:
        case "+":
            res = num1 + num2
        case "-":
            res = num1 - num2
        case "*":
            res = num1 * num2
        case "/":
            res = num1 / num2
        case _:
            res = "Operação inválida"

    print(f"Resultado é igual a {res}")

if __name__ == "__main__":
    main()