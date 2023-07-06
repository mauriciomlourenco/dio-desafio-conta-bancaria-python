#Desafio melhorando a conta bancária, adição de mais funções
def menu():
    return """\n
    ===================MENU===================
    [d]\t\tDepositar
    [s]\t\tSacar
    [e]\t\tExtrato
    [nu]\tNovo usuário(a)
    [nc]\tNova conta
    [lu]\tListar usuários
    [lc]\tListar contas    
    [q]\t\tSair

    => """

def sacar(*, saldo, valor, extrato ,limite, numero_saques, limite_saques):  
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1    
        
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques 

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def emitir_extrato( saldo, **kwargs):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not kwargs["extrato"] else kwargs["extrato"])
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuario(cpf, usuarios):
    usuario_existe = False

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_existe = True

    return usuario_existe

def formatar_cpf(cpf):
    cpf_formatted = ''

    for letra in cpf:
        if letra =='.' or letra =='-':
            continue

        cpf_formatted += letra
    
    return cpf_formatted

def criar_usuario(nome, data_nascimento, cpf, logradouro, nro, bairro, cidade, estado, usuarios):
    cpf_formatted = formatar_cpf(cpf)    
    
    usuario_existe = filtrar_usuario(cpf_formatted, usuarios)

    if(not usuario_existe):    
        endereco = f"{logradouro} - {nro} - {bairro} - {cidade}/{estado}"    
        user = { "nome": nome, "data_nascimento": data_nascimento, "cpf": cpf_formatted, "endereco": endereco}
        usuarios.append(user)
        print("Usuário(a) cadastrado com sucesso!")
        print(usuarios)
    else:
        print("Usuário(a) já cadastrado no sistema do banco, somente é permitido um cadastro por usuário.")

def criar_conta_corrente(cpf, contas, usuarios, AGENCIA):
    cpf_formatted = formatar_cpf(cpf)
    user_existe = filtrar_usuario(cpf_formatted, usuarios)

    if(user_existe):
        numero_conta = len(contas) + 1
        nova_conta = {"agencia": AGENCIA, "numero_conta": numero_conta, "cpf_usuario_conta": cpf_formatted}
        contas.append(nova_conta)
        print("Conta criada com sucesso!")
    else:
        print("Usuário não cadastrado, por favor faça o cadastro do usuário(a) primeiro para depois criar a conta.")

def listar_contas(contas):
    if len(contas) > 0:
        for conta in contas:
            print("==============================================================")
            for chave, valor in conta.items():
                print(f"{chave}: {valor}")
            print("==============================================================")
    else:
        print("Nenhuma conta cadastrada!")

def listar_usuarios(usuarios):
    if len(usuarios) > 0:
        for usuario in usuarios:
            print("==============================================================")
            for chave, valor in usuario.items():
                print(f"{chave}: {valor}")
            print("==============================================================")
    else:
        print("Nenhum usuário(a) cadastrada!")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios= []
    contas = [] 
    AGENCIA = "0001"   

    while True:
        opcao = input(menu())

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
            

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))      
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato = extrato ,limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
            

        elif opcao == "e":
            emitir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            #criar_usuario(nome, data_nascimento, cpf, logradouro, nro, bairro, cidade, estado, usuarios):
            print("Digite as informações do usuário(a)...")
            nome = input("Nome do Usuario(a): ")
            data_nascimento = input("Data de nascimento: ")
            cpf = input("CPF: ")
            logradouro = input("Logradouro: ")
            nro_end = input("Número endereço: ")
            bairro= input("Bairro: ")
            cidade = input("Cidade: ")
            estado = input("Estado: ")
            criar_usuario(nome, data_nascimento, cpf, logradouro, nro_end, bairro, cidade, estado, usuarios)
        elif opcao == "nc":
            cpf_user_conta= input("Digite o CPF do usuário para a conta a ser criada: ")
            criar_conta_corrente(cpf_user_conta, contas, usuarios, AGENCIA)
        elif opcao == "lu":
            listar_usuarios(usuarios)
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()