def calcular(numero1, operacao, numero2):
    if operacao == "+":
        return numero1 + numero2
    if operacao == "-":
        return numero1 - numero2
    if operacao == "*":
        return numero1 * numero2
    if operacao == "/":
        if numero2 == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        return numero1 / numero2
    raise ValueError("Operação inválida.")


def main():
    print("Calculadora")
    print("Operações disponíveis: +, -, *, /")
    print("Digite 'sair' no lugar da operação para encerrar.\n")

    while True:
        operacao = input("Escolha a operação: ").strip()
        if operacao.lower() == "sair":
            print("Até mais!")
            break

        if operacao not in {"+", "-", "*", "/"}:
            print("Operação inválida. Escolha +, -, * ou /.\n")
            continue

        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            resultado = calcular(numero1, operacao, numero2)
            print(f"Resultado: {resultado:g}\n")
        except ValueError as erro:
            print(f"Entrada inválida: {erro}\n")
        except ZeroDivisionError as erro:
            print(f"Erro: {erro}\n")


if __name__ == "__main__":
    main()
