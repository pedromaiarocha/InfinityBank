from Banco import obterConta, banco


def depositar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(f"Saldo Anterior: {cliente['saldo']}")
        cliente["saldo"] = cliente["saldo"] + valor
        print("Depósito realizado com sucesso!")
        print(f"Novo Saldo: {cliente['saldo']}")
    else:
        print("Cliente não existe!")


if __name__ == "__main__":
    depositar(1, 30)
    print(banco)