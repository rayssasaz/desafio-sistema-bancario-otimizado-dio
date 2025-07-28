import textwrap
def menu():
    menu = """\n

        1 - Depositar
        2 - Sacar
        3 - Ver extrato
        4 - Novo usuário
        5 - Nova conta
        6 - Listar contas
        0 - Sair

    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nFalha na operação! Informe umm valor válido")

    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, num_saques, limite_saques):
    if saque > saldo:
        print("Erro: saldo insuficiente!")
    elif saque > limite:
        print(f"Erro: o saque ultrapassa o valor limite de R${limite:.2f}")
    elif num_saques >= limite_saques:
        print("Erro: limite de saques diários atingido")
    elif saque > 0:
        saldo -= saque
        extrato += f"Saque: R${saque:.2f}\n"
        num_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Falha na operação! Informe umm valor válido")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("=========EXTRATO=========")
    print("Nenhuma operação realizada." if not extrato else extrato)
    print(f"\nSaldo atual: R${saldo:.2f}\n")
    print("=========================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n ERRO: Já existe usuário com esse CPF! ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nERRO: Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0.0
    limite = 500.0
    extrato = ""
    num_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            print("Depósito")
            valor = float(input("Valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            print("Saque")
            saque = float(input("Valor a ser sacado: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=num_saques,
                limite_saques=LIMITE_SAQUE,
            )
        elif opcao == "3":
              exibir_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            criar_usuario(usuarios)
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "6":
            listar_contas(contas)
        elif opcao == "0":
            break
        else:
            print("Erro! Informe uma operação válida.")



main()