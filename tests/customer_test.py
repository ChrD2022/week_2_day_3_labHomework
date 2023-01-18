import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Dan", 50.00, 31)
        self.drink = Drink("Lager", 3.50, 1)

    def test_customer_has_name(self):
        self.assertEqual("Dan", self.customer.name)

    def test_decrease_wallet(self):
        expected = 46.50
        self.customer.decrease_wallet(3.50)
        actual = self.customer.wallet
        self.assertEqual(expected,actual)
    
    def test_over_age(self):
        expected = True
        age_check = self.customer.over_age()
        self.assertEqual(age_check, expected)

    def test_add_drunknness(self):
        self.customer.add_drunkenness(self.drink)
        self.assertEqual(1, self.customer.drunkenness)
