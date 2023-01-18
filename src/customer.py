class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def decrease_wallet(self, amount):
        self.wallet -= amount

    def over_age(self):
        if self.age >= 18:
            return True
        else:
            return False

    def add_drunkenness(self, drink):
        self.drunkenness += drink.level

    