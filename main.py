from Operacoes import consulta, deposito, saque, transferencia
from Banco import *

def Menu():
    while True:
        print("---- Bem vindo ao Menu ----")
        print('1 - Adicionar Conta')
        print('2 - Editar Nome')
        print('3 - Excluir Conta')
        print('4 - Consultar Conta')
        print('5 - Listar todas as Contas')
        print('6 - Consultar Saldo')
        print('7 - Fazer Deposito')
        print('8 - Fazer Saque')
        print('9 - Transferência')
        print('10 - Sair')
        opcao = int(input("Digite uma Opção: "))
        if opcao == 1:
            nome = input('Digite o nome do cliente: ')
            saldo = float(input('Digite o Saldo: '))
            adicionarConta(nome, saldo)

        elif opcao == 2:
            conta = int(input("Digite o número da conta: "))
            novo_nome = input("Digite o novo Nome: ")

        elif opcao == 3:
            conta = int(input("Digite o número da conta: "))
            deletarConta(conta)

        elif opcao == 4:
            conta = int(input('Digite o numero da conta: '))
            consultarCliente(conta)

        elif opcao == 5:
            listarTodasContas()

        elif opcao == 6:
            conta = int(input('Digite o numero da conta: '))
            consulta.consultarSaldo(conta)

        elif opcao == 7:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor de deposito: '))
            deposito.depositar(conta, valor)

        elif opcao == 8:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor de saque: '))
            saque.saque(conta, valor)

        elif opcao == 9:
            contaOrigem = int(input('Digite o número da conta: '))
            contaDestino = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor de transferencia: '))
            transferencia.transferir(contaOrigem, contaDestino, valor)

        elif opcao == 10:
            print('---- VOCÊ SAIU DO PROGRAMA ----')

        break

Menu()

