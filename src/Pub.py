class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink

    def sell_drink_to_customer(self, name, customer):
        if customer.over_age() == True and customer.drunkenness <= 5:
            drink = self.find_drink_by_name(name)
            customer.decrease_wallet(drink.price)
            self.increase_till(drink.price)
            customer.add_drunkenness(drink)

