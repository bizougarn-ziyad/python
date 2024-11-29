import random
class bank:
    deposit=0
    def __init__(self, name,balance):
        self.name = name
        self.balance = balance
        self.number=random.sample(range(1, 11), 10)

name1=""
while name1=="" or not all(c.isalpha() or c.isspace() for c in name1) or name1.strip() == "":   
    name1=input("Enter your full name -> ")

balance1=float(input("Enter your balance ->"))

user1=bank(name1,balance1)

choises=input("Enter 1 to deposit\nEnter 2 to withdraw\nEnter 3 to show your account number\n")

if choises=="1":
    amount=float(input("enter the amount of deposit -> "))
    while amount <= 0:
        amount=float(input("enter the a valid amount of deposit -> "))
    user1.balance=user1.balance+amount
    print("you deposited succefully  ", amount,"$ \n your balance is now : ",user1.balance)
        
elif choises=="2":
    amount=float(input("enter the amount to withdraw  -> "))
    while amount <= 0:
        amount=float(input("enter the a valid amount to withdraw -> "))
    user1.balance=user1.balance-amount
    print("you withdrew succefully ", amount,"$ \n your balance is now : ",user1.balance)
elif choises=="3":
    print("Your account number is : ", *user1.number,sep="")
