import random
import os
class bank:
    deposit=0
    def __init__(self, name,balance):
        self.name = name
        self.balance = balance
        self.number=random.sample(range(1, 11), 10)

name1=""
while name1=="" or not all(c.isalpha() or c.isspace() for c in name1) or name1.strip() == "":   
    name1=input("Enter your full name -> ")
    os.system('cls')

balance1=float(input("Enter your balance ->"))
os.system('cls')

user1=bank(name1,balance1)
choises=0

while 1:
    try:
        choises=int(input("Enter 1 to deposit\nEnter 2 to withdraw\nEnter 3 to show your account number\n"))
        if choises == 1 or choises == 2 or choises == 3:
            os.system('cls')  
            break  
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    except ValueError:
        os.system('cls') 

if choises==1:
    amount=float(input("enter the amount of deposit -> "))
    os.system('cls')
    while amount <= 0:
        amount=float(input("enter the a valid amount of deposit -> "))
        os.system('cls')
    user1.balance=user1.balance+amount
    print("you deposited succefully", amount,"$ \nyour balance is now :",user1.balance,"$")
        
elif choises==2:
    amount=float(input("enter the amount to withdraw  -> "))
    os.system('cls')
    if user1.balance<0:
        print("You don't have the fundes to withdraw")
        exit(1)
    else:    
        while amount <= 0 or amount>user1.balance:
            amount=float(input("enter the a valid amount to withdraw -> "))
            os.system('cls')
    user1.balance=user1.balance-amount
    print("you withdrew succefully ", amount,"$ \n your balance is now : ",user1.balance)
elif choises==3:
    print("Your account number is : ", *user1.number,sep="")
