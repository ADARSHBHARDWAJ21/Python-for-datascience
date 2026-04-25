#ENCAPSULATION - PROTECTS THE DATA FROM UNAUTHORIZED ACCESS
class Account:   # class name is account
    # every class will have init method
    ## init method bolega jo bhi class ki propertiese hai une initilize karo
    # counstructor
    def __init__(self, account_number, account_holder, balance):
        # SELF KEYWORD IS USED AS CONNECTING LINE BETWEEN CURRENT OBJECT WE HAVE AND THE CLASS WE HAVE CREATED THE ATTRIBUTES OF THAT CLASS
        # self use karenge jab bhi object create karenge aur u object ki wagh se hame future me jaa ke values / function ko access krna hai
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance
        # These lines take the data you give to the "blueprint" (the Class) and permanently attach it to the "object" (the individual account).

    ## Add the money to the account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposited {amount}. New balance is {self.__balance}') #made attributr (__.balance) private

    ## polymorphism : withdraw the money from account
    def withdraw(self, amount):
        if amount <= self.__balance + self.overdraft_limit and amount > 0:
            self.__balance -= amount
            print(f'Withdraw {amount}. New balance: {self.__balance}')
        else:
             print('Overdraft limit exceeded')

acc1 = Account('AC123', 'John Doe', 1000)
acc2 = Account('AC456', 'Jane Smith', 2000)

print(acc1.balance)
print(acc2.balance)


##ABSTRACTION- HIDES THE IMPLEMENTATION PART 

