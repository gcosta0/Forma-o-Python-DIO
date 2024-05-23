extrato = []
saldo = 0
limite_de_saques = 3
print("BEM VINDO AO BANCO CAMARADA!\nO que podemos fazer por você hoje?\n")
while True:
    menu = str(input("SELECIONE UMA DAS OPÇÕES A SEGUIR:\n 1: DEPOSITO\n 2: SAQUE\n 3: EXTRATO\n 4: SAIR \n"))
    while menu not in "1234":
        print("OPÇÃO INCORRETA!")
        menu = str(input("SELECIONE UMA DAS OPÇÕES A SEGUIR:\n 1: DEPOSITO\n 2: SAQUE\n 3: EXTRATO\n 4: SAIR \n"))
    if menu == "1":
        print("DEPOSITO")
        valor_deposito = float(input("Digite o valor que deseja depositar: R$"))
        if valor_deposito > 0:
            print(f"COMPROVATIVO DE DEPOSITO \n O valor de R${valor_deposito:.2f} foi depositado em sua conta bancaria")
            extrato.append(f"+ R${valor_deposito:.2}")
            saldo += valor_deposito
        else:
            print("NÃO É POSSIVEL DEPOSTAR VALORES NEGATIVOS!")
    elif menu == "2":
        print("SAQUE")
        valor_saque = float(input("Digite o valor do saque que deseja efetuar: R$"))
        if valor_saque > saldo:
            print("SALDO INSUFICIENTE")
        elif valor_saque > 500:
            print("O VALOR EXCEDE O SAQUE MAXIMO.")
        else:
            if limite_de_saques > 0:
                print(f"COMPROVATIVO DE SAQUE\nO valor de R${valor_saque:.2f} foi sacado de sua conta bancaria")
                extrato.append(f"- R${valor_saque:.2f}")
                saldo -= valor_saque
                limite_de_saques -= 1
            else:
                print("LIMITE DE SAQUE DIARIO ATINGIDO!")
    elif menu == "3":
        print("EXTRATO")

        for i in extrato:
            print(i)
        print(f"Seu saldo atual é R${saldo:.2f}")
    elif menu == "4":
        print("OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS. VOLTE SEMPRE!")
        break
