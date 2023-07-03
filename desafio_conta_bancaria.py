menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        print("Deposito")
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f} \n"

    elif opcao == 's':
        if(numero_saques <= LIMITE_SAQUES):
            valor_saque = float(input("Digite o valor a ser depositado:"))

            if valor_saque > limite:
                print("Valor de saque maior que o limite de saque permitido de R${limite}.00")
            elif valor_saque < 0:
                print("Valor de saque inválido")
            elif numero_saques == 3:
                print("Número de saques diários excedido!")
            elif valor_saque > saldo:
                print("Não foi possível realizar o saque, saldo indisponível.")
            else: 
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Saque: R$ {valor_saque:.2f} \n"
    elif opcao == 'e':
        if extrato == '':
            print("Não foram realizadas movimentações.")
        else:
            print(extrato + f"**************************************\nSaldo da conta: R$ {saldo:.2f}")
    elif opcao == 'q':
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")