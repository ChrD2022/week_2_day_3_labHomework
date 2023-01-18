import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Clansman", 200.00)

    def test_pub_has_name(self):
        self.assertEqual("The Clansman", self.pub.name)

    def test_increase_till(self):
        expected = 203.50
        self.pub.increase_till(3.50)
        actual = self.pub.till
        self.assertEqual(expected,actual)