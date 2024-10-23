
#Create a new file called "bank_account.py"
#Create a class called "Account" that has the following attributes:
class Account:
    def __init__(self,account_number,account_holder, account_balance=0):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

#Define the deposit() method. It should take in one argument, the amount to be deposited, and add it to the account balance.
    def deposit(self,deposit_amount):
        self.account_balance += deposit_amount
        print (f" Credit Alert!!{self.account_holder} {deposit_amount} was creditted to your account!" )
        

#Define the withdraw() method. It should take in one argument, the amount to be withdrawn, and subtract it from the account balance. 
# The method should only execute the withdrawal if the account balance is greater than or equal to the amount to be withdrawn.

    def withdrawals(self,withdrawal_amount):
        if self.account_balance >= withdrawal_amount:
            self.account_balance -= withdrawal_amount
        print(f"{self.account_holder} you have insufficient funds!")
        
#Define the check_balance() method. It should return the current account balance.

    def check_balance(self):
        print(f" {self.account_holder} your current balance is {self.account_balance}")
    

#Create an instance of the Account class, and assign it to a variable called "my_account".

my_account = Account("082994848358","Kester")

#Use the methods of the class to deposit and withdraw money from the account, and check the account balance.
my_account.deposit(150)
my_account.check_balance()
my_account.withdrawals(200)
my_account.check_balance()
