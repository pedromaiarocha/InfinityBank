from Banco import obterConta, banco

def consultarSaldo(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(f'Conta: {cliente["nome"]}')
        print(f'Saldo: {cliente["saldo"]}')
    else:
        print("Conta não existe")

if __name__ == "__main__":
    consultarSaldo(1)
    print(banco)