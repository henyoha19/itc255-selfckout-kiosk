import unittest
from customer import Customer
from scanning import Scanning
from item import Item
import datetime

class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.customer=Customer(1 ,'George','Tom','3906 S Kenyon street')
      
    def test_getcustomerId(self):
        self.assertEqual(self.customer.getcustomerId(), 1)
        
    def test_getcustomerLname(self):
        self.assertEqual(self.customer.getcustomerLname(), 'George')

    def test_getcustomerFname(self):
        self.assertEqual(self.customer.getcustomerFname(), 'Tom')

    def test_getcustomerAddress(self):
        self.assertEqual(self.customer.getcustomerAddress(), '3906 S Kenyon street')

class scanningTest(unittest.TestCase):
    def setUp(self):
        self.scanning=Scanning(2,'02-08-2020')

    def test_getscanningnum (self):
        self.assertEqual(self.scanning.getScanningnum(), 2)
        
    def test_getscanningDate (self):
        self.assertEqual(self.scanning.getScanningdate(), '2020-02-02')
        

class itemTest(unittest.TestCase):
    def setUp(self):
        self.item=Item(3, 'computer', 450)

    def test_getitemNum (self):
        self.assertEqual(self.item.getItemNum(), 3)
        
    def test_getitemName (self):
        self.assertEqual(self.item.getItemName(), 'computer')
    
    def test_getitemPrice (self):
        self.assertEqual(self.item.getItemPrice(), 450)
        
