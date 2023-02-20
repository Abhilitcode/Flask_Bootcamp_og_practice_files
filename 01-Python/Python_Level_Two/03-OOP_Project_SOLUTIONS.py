####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.



class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')

    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)




# 3. Show the account owner attribute
acct1.owner




# 4. Show the account balance attribute
acct1.balance




# 5. Make a series of deposits and withdrawals
acct1.deposit(50)




acct1.withdraw(75)




# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)


#mycode

class bank_acc():
    def __init__(self,owner,balance =0):
        self.owner=owner
        self.balance=balance

    def __str__(self):
        return f'Owner:{self.owner}\n Account balance:{self.balance}'

    def deposit(self,dep_amt):
        self.balance+=dep_amt
        print("Amount Deposited")

    def withdrawal(self,withdraw_amt):
        if self.balance>=withdraw_amt:
            self.balance-=withdraw_amt
            print("Amount Withdraw")
        else:
            print("Funds unavailable!")

acc1 = bank_acc('Abhi',200)

print(acc1)

acc1.owner

acc1.balance

acc1.deposit(50)

acc1.withdrawal(35)

acc1.withdrawal(500)

print(acc1)
