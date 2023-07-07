class Menu:
   
    def selecionar(self):
        opcoes = ['d', 's', 'e', 'q']
        opcao = input("\n[d] - Depositar\n[s] - Sacar\n[e] - Extrato\n[q] - Sair\nDigite sua opção: ")
        if opcao in opcoes:
            return opcao
        return None

    def ler(self, msg):
        try:
            return float(input(msg))
        except ValueError:
            pass

    def exibir(self, msg):
        print(msg)
