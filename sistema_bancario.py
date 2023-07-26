menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
"""
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor para depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
            print("Depósito realizado com sucesso!")

        else:
            print("Falha na operação! Valor informado inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor para saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= LIMITE_SAQUE

        print("Saque realizado com sucesso!")

        if excedeu_saldo:
            print("Falha na operação! Saldo insuficiente.")

        elif excedeu_limite:
            print("Falha na operação! Limite de saque excedido.")

        elif excedeu_saque:
            print("Falha na operação! Você excedeu o numero de saque máximo.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Falha na operação! Valor informado inválido.")

    elif opcao == "3":
        print("\n =================== EXTRATO ===================\n")
        print("Não houve movimentações." if not extrato else extrato)
        print (f"\nSaldo: R$ {saldo:.2f} \n")
        print("=================================================")

    elif opcao == "4":
        break

    else:
        print("Falha na operação, opção informada inválida. \n Por favor selecione novamente a operação desejada.")
