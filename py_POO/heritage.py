# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 19:05:20 2025

@author: Admin
"""

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        
    def printname(self):
        print(self.firstname,self.lastname)

x=Person("fatima","dihi")
x.printname()

class student(Person):
    pass #use the pass when you do not want to add any other properties or methods to the class

x=student("DIHI", "hanane")
x.printname()