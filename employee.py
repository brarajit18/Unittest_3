# -*- coding: utf-8 -*-
class Employee:
    
    raise_amount = 1.05
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    def show_email(self):
        return "{}.{}@email.com".format(self.first,self.last)
    
    def show_full_name(self):
        return "{} {}".format(self.first, self.last)
    
    def show_pay(self):
        return (self.pay * self.raise_amount)
    
if __name__=='__main__':
    emp1 = Employee('Ajit','Brar',80000)
    emp2 = Employee('Sam','Brar',90000)
    emp3 = Employee('John','Park',50000)
    
    print (emp1.show_email())
    print (emp2.show_full_name())
    print (emp3.show_pay())
