import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Dan", 50.00)

    def test_customer_has_name(self):
        self.assertEqual("Dan", self.customer.name)

    def test_decrease_wallet(self):
        expected = 46.50
        self.customer.decrease_wallet(3.50)
        actual = self.customer.wallet
        self.assertEqual(expected,actual)