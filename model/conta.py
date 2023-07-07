class Conta:

    QUANTIDADE_MAXIMA = 3
    VALOR_MAXIMO = 500

    def __init__(self):
        self.__saldo = 0.0
        self.__movimentacoes = []
        self.__quantidade = 0

    @property
    def saldo(self):
        return self.__saldo
    
    def validar_valor(self, valor):
        if valor > 0:
            return True
        return False    
    
    def validar_saque(self, valor):
        if valor <= self.__saldo:
            return True
        return False 
    
    def validar_limite(self, valor):
        if valor <= Conta.VALOR_MAXIMO:
            return True
        return False
    
    def validar_quantidade(self):
        if self.__quantidade < Conta.QUANTIDADE_MAXIMA:
            return True
        return False

    def depositar(self, valor):
        self.__movimentacoes.append(('Depósito', valor))
        self.__saldo += valor

    def sacar(self, valor):
        self.__movimentacoes.append(('Saque', valor))
        self.__saldo -= valor
        self.__quantidade += 1

    def extrato(self):
        print('\n====================== EXTRATO ======================\n')
        if len(self.__movimentacoes) > 0:
            for mov in self.__movimentacoes:
                print(f'{mov[0]}: R$ {mov[1]:.2f}')
        else:
            print('\nNão foram efetuadas movimentações na conta bancária.\n')
        print(f'\nSaldo atual: R$ {self.saldo:.2f}')
        print('\n=====================================================\n')   
            