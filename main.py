from view.menu import Menu
from model.conta import Conta

def depositar(menu, conta):
    valor = menu.ler("\nInforme o valor do depósito: ")
    if not conta.validar_valor(valor):
        menu.exibir('\nOperação cancelada. O valor informado é inválido.')
    else:
        conta.depositar(valor)
        menu.exibir('\nDepósito realizado com sucesso.')

def sacar(menu, conta):
    valor = menu.ler("\nInforme o valor do saque: ")
    if not conta.validar_valor(valor):
        menu.exibir('\nOperação cancelada. O valor informado é inválido.')
    elif not conta.validar_saque(valor):
        menu.exibir('\nOperação cancelada. Saldo insuficiente para efetuar o saque.')
    elif not conta.validar_limite(valor):
        menu.exibir('\nOperação cancelada. O valor informado excede o valor máximo de R$ {:.2f}.'.format(Conta.VALOR_MAXIMO))
    elif not conta.validar_quantidade():
        menu.exibir('\nOperação cancelada. A quantidade de saques excede o número máximo permitido por dia.')
    else:
        conta.sacar(valor)
        menu.exibir('\nSaque realizado com sucesso.')

def extratificar(conta):
    conta.extrato()

def operacao(opcao, menu, conta):
    if opcao == 'd':
        depositar(menu, conta)
    elif opcao == 's':
        sacar(menu, conta)
    elif opcao == 'e':
        extratificar(conta)
    else:
        menu.exibir('\nOpção Inválida.')

def main():
    conta = Conta()
    while True:        
        menu = Menu()
        opcao = menu.selecionar()
        if opcao != 'q':
            operacao(opcao, menu, conta)
        else:
            break
        
if __name__ == "__main__":
    main()
