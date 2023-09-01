from Banco import obterConta, banco


def transferir(contaOri: int, contaDes: int, valor: float) -> None:
    contaOrigem = obterConta(contaOri)
    contaDestino = obterConta(contaDes)

    if contaDestino and contaOrigem:
        if contaOrigem["saldo"] >= valor:
            contaDestino["saldo"] += valor
            contaOrigem["saldo"] -= valor
            print("Transferência realizada com sucesso!")

        else:
            print("Saldo insuficiente!")

    else:
        print("Um ou mais Clientes não existem!")


if __name__ == "__main__":
    print(banco)
    transferir(1, 2, 30)
    print(banco)