
print("Escolha uma das operações abaixo para continuar")
op = str(input("Soma...(+) Subtracão...(-) Divisão...(/) Multiplicação...(*) Sair...(0) "))

prog = int(1)

while prog == 1:
    
    if op == "+":
        a = int(input("Insira o primeiro número a ser somado: "))
        b = int(input("Insira o segundo número a ser somado: "))
        print("--------------------------------------------------")
        print("O resultado da soma é: ", a + b)
        print("Escolha uma das operações abaixo para continuar")
        op = str(input("Soma...(+) Subtracão...(-) Divisão...(/) Multiplicação...(*) Sair...(0) "))

    elif op == "-":
        a = int(input("Insira o primeiro número a ser subtraido: "))
        b = int(input("Insira o segundo número a ser subtraido: "))
        print("--------------------------------------------------")
        print("O resultado da subtração é: ", a - b)
        print("Escolha uma das operações abaixo para continuar")
        op = str(input("Soma...(+) Subtracão...(-) Divisão...(/) Multiplicação...(*) Sair...(0) "))

    elif op == "*":
        a = int(input("Insira o primeiro número a ser multiplicado: "))
        b = int(input("Insira o segundo número a ser multiplicado: "))
        print("--------------------------------------------------")
        print("O resultado da subtração é: ", a * b)
        print("Escolha uma das operações abaixo para continuar")
        op = str(input("Soma...(+) Subtracão...(-) Divisão...(/) Multiplicação...(*) Sair...(0) "))

    elif op == "/":
        a = int(input("Insira o primeiro número a ser dividido: "))
        b = int(input("Insira o segundo número a ser dividido "))
        print("--------------------------------------------------")
        print("O resultado da subtração é: ", a / b)
        print("Escolha uma das operações abaixo para continuar")
        op = str(input("Soma...(+) Subtracão...(-) Divisão...(/) Multiplicação...(*) Sair...(0) "))

    elif op == "0":
        prog = 0


    































