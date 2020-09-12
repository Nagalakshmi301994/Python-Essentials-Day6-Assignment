#!/usr/bin/env python
# coding: utf-8

# # create a bank account class that has two attributes ownerName,Balance And two methods deposit,withdraw As an added requirement,withdrawals may not exceed the available balance.Instantiate your class,make several deposits and withdrawals,and test to make sure the account cant be overdrawn.

# In[1]:


class Bank_Account: 
    def __init__(self):
        self.ownername='Kishor'
        self.balance=0
        print("Hello Kishor!!! Welcome to the Deposit & Withdrawal Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdraw:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 

s = Bank_Account() 
s.deposit() 
s.withdraw() 
s.display() 


# In[2]:


class Bank_Account: 
    def __init__(self):
        self.ownername='Kishor'
        self.balance=0
        print("Hello Kishor!!! Welcome to the Deposit & Withdrawal Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdraw:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 

s = Bank_Account() 
s.deposit() 
s.withdraw() 
s.display() 


# # create a cone class that has two attributes: R=Radius,h=Height And two methods:volume and surface area.Make only one class with functions,as in where required import Math.

# In[3]:


import math 
pi = math.pi 

def volume(r, h): 
    return (1 / 3) * pi * r * r * h 
  
def surfacearea(r, s): 
    return pi * r * s + pi * r * r 
  
radius = float(5) 
height = float(12) 
slat_height = float(13) 
print( "Volume Of Cone : ", volume(radius, height) ) 
print( "Surface Area Of Cone : ", surfacearea(radius, slat_height) ) 


# In[ ]:




