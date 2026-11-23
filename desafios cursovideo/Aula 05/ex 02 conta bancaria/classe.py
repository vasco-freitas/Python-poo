class ContaBancaria:
    """
    Cria conta bancaria que permite fazer saques e deposito
    """
    def __init__(self, pin, nome, saldo = 0):
        self.pin = pin
        self.nome = nome 
        self.saldo = saldo
        print(f'Ola! O seu codigo {self.pin} foi criado com sucesso.')
        
    def depositar(self, valor):
        self.saldo += valor 
        print(f'Depósito de {valor:,.2f}€ Autorizado!')
        
    def levantar (self):
        valor = int(input('Levantamento: '))
        if valor > self.saldo:
            print(f'Saldo insuficiente. Não pode levantar {valor:,.2f}€')
        else:
            self.saldo -= valor
            print(f'Levantamento de {valor:,.2f}€ Autorizado!')
    
    def __str__(self):
        return f'Código: {self.pin} \n Nome: {self.nome} \n Saldo: {self.saldo:,.2f}€' 
        
#    def __str__(self):
#        return f'A conta {self.pin} de {self.nome} tem neste momento {self.saldo:,.2f}€'

    
c1 = ContaBancaria(6257, 'Vasco', 20000)
c1.levantar()
c1.depositar(1000)
print(c1)
        