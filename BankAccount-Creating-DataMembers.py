class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount  

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance)             


class Checking(Account):   #Passing base class as a parameter
    """ This class generates checking account objects """
   
    type = "checking"      #Class variables also called data members are shared by all instances of the class
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath) 
         self.fee = fee    #Data members
 
    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
 

jacks_checking = Checking("account\\jack.txt", 1) #Instantiation of the class
jacks_checking.deposit(10)
jacks_checking.transfer(100)                   
print(jacks_checking.balance)  #Instance variable are shared by only its object instance
jacks_checking.commit()
print(jacks_checking.type)

johns_checking = Checking("account\\john.txt" , 1)
johns_checking.deposit(20)
johns_checking.transfer(200)
print(johns_checking.balance)
johns_checking.commit()
print(johns_checking.type)

print(johns_checking.__doc__)  #Accessing Doc strings




