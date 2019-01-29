# -*- coding: utf-8 -*-
import unittest
from employee import Employee

class Test_Employee(unittest.TestCase):
    
    def setUp(self):
        print ('setUp')
        self.emp1 = Employee('Ajitpal','Brar',80000)
        self.emp2 = Employee('John','Dier',60000)
    
    def tearDown(self):
        print ('tearDown')
    
    def test_show_email(self):
        print ('test_show_email')
        self.assertEqual(self.emp1.show_email(),'Ajitpal.Brar@email.com')
        self.assertEqual(self.emp2.show_email(),'John.Dier@email.com')
        
        self.emp2.first = 'James'
        
        self.assertEqual(self.emp2.show_email(),'James.Dier@email.com')
    
    def test_show_full_name(self):
        print ('test_show_full_name')
        self.assertEqual(self.emp1.show_full_name(),'Ajitpal Brar')
        self.assertEqual(self.emp2.show_full_name(),'John Dier')
        
        self.emp1.first = 'Ajit'
        self.emp2.first = 'James'
        
        self.assertEqual(self.emp1.show_full_name(),'Ajit Brar')
        self.assertEqual(self.emp2.show_full_name(),'James Dier')
    
    def test_show_pay(self):
        print ('test_show_full_name')
        self.assertEqual(self.emp1.show_pay(),84000.0)
        self.assertEqual(self.emp2.show_pay(),63000.0)
        

if __name__ == '__main__':
    unittest.main()
