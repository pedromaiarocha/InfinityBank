from Banco import obterConta, banco


def saque(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        if cliente["saldo"] >= valor:
            cliente["saldo"] = cliente["saldo"] - valor
            print("Saque realizado com sucesso!")
            print(f"Novo Saldo: {cliente['saldo']}")
        else:
            print("Saldo insuficiente!")

    else:
        print("Cliente não existe!")


if __name__ == "__main__":
    saque(1, 3)
    print(banco)