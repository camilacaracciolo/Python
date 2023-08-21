class Client:
    def __init__(self, name, email, address, cash):
        self.name = name
        self.email = email
        self.address = address
        self.cash = cash

    def buy(self, amount):
        if self.cash >= amount:
            self.cash -= amount
            print(f"{self.name} ha realizado una compra por ${amount}. cash restante: ${self.cash}")
        else:
            print(f"{self.name} no tiene cash suficiente para realizar la compra.")

    def recharge_cash(self, amount):
        self.cash += amount
        print(f"{self.name} ha recargado su cash con ${amount}. cash actual: ${self.cash}")

    def __str__(self):
        return self.name