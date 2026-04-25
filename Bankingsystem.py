class Account:   # class name is account
    # every class will have init method
    ## init method bolega jo bhi class ki propertiese hai une initilize karo
    # counstructor
    def __init__(self, account_number, account_holder, balance):
        # SELF KEYWORD IS USED AS CONNECTING LINE BETWEEN CURRENT OBJECT WE HAVE AND THE CLASS WE HAVE CREATED THE ATTRIBUTES OF THAT CLASS
        # self use karenge jab bhi object create karenge aur u object ki wagh se hame future me jaa ke values / function ko access krna hai
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        # These lines take the data you give to the "blueprint" (the Class) and permanently attach it to the "object" (the individual account).

    ## Add the money to the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposited {amount}. New balance is {self.balance}')

    ## polymorphism : withdraw the money from account
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit and amount > 0:
            self.balance -= amount
            print(f'Withdraw {amount}. New balance: {self.balance}')
        else:
            print('Overdraft limit exceeded')

    ## Display method to display account details with overdraft limit
    def display(self):
        print(f'Current Account Number: {self.account_number}')
        print(f'Account Holder: {self.account_holder}')
        print(f'Balance: {self.balance}')
        print(f'Overdraft Limit: {self.overdraft_limit}')



## inheritance: Savings account class inherited from the account class

# # super is used to  go to above class fetch the and take as it is attributes which are , account no , account ,holder, balance
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f'Added interest {interest}. New balance is {self.balance}')

    # polymorphism
    def display(self):
        return f"Savings Account Number: {self.account_number}, Balance: {self.balance}, Interest Rate: {self.interest_rate}%"
## inheritance
class CurrentAccount(Account):
 def __init__(self, account_number, account_holder, balance, overdraft_limit):
    super().__init__(account_number, account_holder, balance)
    self.overdraft_limit = overdraft_limit


# object creation
acc1 = Account('AC123', 'John Doe', 1000)
acc2 = Account('AC456', 'Jane Smith', 2000)
sa1 = SavingsAccount('AC789', 'Doe', 10000, 2)
ca1 = CurrentAccount('CA123' , 'Adarsh bhardwaj', 1000000 , 200000)

#Encapsulation

# print(acc1.balance)
# print(acc2.balance)
# print(acc2.deposit(20000))
# print(acc2.withdraw(1000))
# print(acc2.display())
# print(acc1.display())
#print(sa1.balance)
#print(sa1.add_interest())
#sa1.withdraw(1500)
# print(sa1.display())
# sa1.display()
# acc1.display()
ca1.withdraw(1100000)
ca1.display()