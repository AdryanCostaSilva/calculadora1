opcao = ''
while opcao != 5:
    print("Opções: \n [1] SOMAR\n [2] SUBTRAIR\n [3] MULTIPLICAR\n [4] DIVIDIR\n [5]SAIR")
    opcao = int(input("Sua escolha: "))
    if opcao == 5:
        break
    elif opcao < 1 or opcao > 5:
        print("Opção inválida tente novamente")
        continue
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if opcao == 1:
        print(f"A soma entre {num1} e {num2} é {num1 + num2}")
    elif opcao == 2:
        print(f"A subtração entre {num1} e {num2} é {num1 - num2}")
    elif opcao == 3:
        print(f"A multiplicação entre {num1} e {num2} é {num1 * num2}")
    elif opcao == 4:
        print(f"A divisão entre {num1} e {num2} é {num1 / num2} ")
print(f"Você saiu do programa, até mais!")
