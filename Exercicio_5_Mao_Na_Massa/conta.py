#conta.py
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito de R${valor:.2f} realizado. Saldo atual:R${self.saldo:.2f}") 
        else:
            print("O valor do deposito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}")    
            else:
                print("Saldo insuficiente para saque.") 
        else:
            print("O valor do saque deve ser positivo.")

conta = Conta("Thais",2000)

conta.depositar(200)
conta.sacar(500)
conta.sacar(1900)
conta.depositar(-200)
conta.sacar(-50)