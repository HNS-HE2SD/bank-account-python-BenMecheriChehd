class Clinet:
    def __init__(self,cin,firstName,lastName,tel=""):
        self.__cin = cin
        self.__firstName = firstName
        self.__lastName = lastName
        self.__tel = tel
        self.Acconts = [] #list for the acconts
  
    def get_cin(self):
        return self.__cin
    def get_firstName(self):
        return self.__firstName
    def get_lastName(self):
        return self.__lastName
    def get_tel(self):
        return self.__tel
    def set_tel(self,tel):
        self.__tel = tel
   
    def display(self):
        print(f"cin:{self.__cin},Name:{self.__firstName} {self.__lastName}, Tel:{self.__tel}")
    
    # to Allow a client to have multiple accounts and list them.
    def MultipleAccontes(self):
        NewAccontes = Account(self)
        self.Acconts.append(NewAccontes)
    def My_Accounts(self):
        print(f"\n Acconts of {self.get_firstName()} {self.get_lastName()}")
        print("-" * 10)
        for i, NewAccontes in enumerate (self.Acconts, start=1):
            print(f"{i}.:") 
            NewAccontes.display()
            print("-" * 10)

class Account:
    __nbAcconts = 0
    def __init__(self, owner):
        Account.__nbAcconts += 1
        self.__code = Account.__nbAcconts
        self.__balance = 0.0
        self.__owner = owner
        self.records = [] # list for the transfers 
  
    def get_code(self):
        return self.__code
    def get_balance(self):
        return self.__balance
    def get_owner(self):
        return self.__owner
   
    def __AddRecord(self,type,amount,other=None):  # I made this function private so that it can only be modified within the class.
        record = { "type":type,"amount":amount,"other":other}  # this records is dictionary to stor the history in organized way.
        self.records.append(record)
   
    def credit (self,amount,account=None):
       if amount>0: # check that all add amounts are positive.
           if account is None:
             self.__balance += amount
             self.__AddRecord("credit",amount)

           if account is not None:
             self.__balance += amount
             self.__AddRecord("transfer in",amount,account)
       else:
           print("The Operation Is NOT VALID")
   
    def debit(self,amount,account=None): 
        if amount >0:  # check that all add amounts are positive.
           if self.__balance >= amount:
                 if account is None:
                     self.__balance -= amount
                     self.__AddRecord("debit",amount)
                 if account is not None:
                     self.__balance -= amount
                     account.credit(amount, account)
                     self.__AddRecord("transfer out",amount,account)
                     

           else:
                 print (" Insufficient balance. ")
        else:
           print("The Operation Is NOT VALID")
   
    def display(self):
        print(f"Account Code:{self.__code}")
        print(f"Owner:{self.__owner.get_firstName()} {self.__owner.get_lastName()}")
        print(f"Balance:{self.__balance} DA")
   
    @staticmethod
    def displayNBAccounts():
        print("Total accounts created:", Account.__nbAcconts)
    
    # display the Transaction History including operation type and amount.
    def displayTransactions(self):
        print(f"The Transaction History of The Account{self.__code}, the owner {self.__owner.get_firstName()} {self.__owner.get_lastName()}")
        print("--"*10)
        for i, record in enumerate(self.records,start=1):
            operation_type = record["type"]
            the_amount= record["amount"]
            other=record["other"]
            if other is None:
                print(f"{i}.{operation_type} of {the_amount}DA")
            else:
                if operation_type == "transfer in":
                    print(f"{i}. transfer in of {the_amount}DA from the Account {other.get_code()}")
                if operation_type == "transfer out":
                    print(f"{i}. transfer out of {the_amount}DA to the Account {other.get_code()}")
        print("--"*10)

# TEST
client1 = Clinet("C123", "Ali", "Karim", "0550-123-456")
client1.display()

client1.MultipleAccontes()
client1.MultipleAccontes()

client1.My_Accounts()

acc1 = client1.Acconts[0]
acc2 = client1.Acconts[1]

acc1.credit(1000)         
acc1.debit(300)          
acc2.credit(500)          
acc2.debit(100)          

print("\nTesting transfer ")
acc1.debit(200, acc2)     
acc2.debit(150, acc1)    
   

print("\nBalances ")
acc1.display()
acc2.display()

print("\nTransactions of Account 1 ")
acc1.displayTransactions()

print("\nTransactions of Account 2 ")
acc2.displayTransactions()

print("\nTotal Accounts Created ")
Account.displayNBAccounts()