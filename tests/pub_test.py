import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.drink_1 = Drink("Lager", 3.50)
        self.drink_2 = Drink("Whiskey", 4.00)

        drinks = [self.drink_1, self.drink_2]
        self.pub = Pub("The Clansman", 200.00, drinks)


    def test_pub_has_name(self):
        self.assertEqual("The Clansman", self.pub.name)

    def test_increase_till(self):
        expected = 203.50
        self.pub.increase_till(3.50)
        actual = self.pub.till
        self.assertEqual(expected,actual)

    def test_can_find_drink_by_name(self):
        drink = self.pub.find_drink_by_name("Lager")
        self.assertEqual("Lager", drink.name)

    def test_can_sell_drink_to_customer(self):
        customer = Customer("Dan", 50.00)
        self.pub.sell_drink_to_customer("Lager", customer)
        self.assertEqual(46.50, customer.wallet)
        self.assertEqual(203.50, self.pub.till)
