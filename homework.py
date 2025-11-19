import time 
class Clinet:
    def __init__(self,cin,firstName,lastName,Tel=''):
        self.__cin = cin
        self.__firstName = firstName
        self.__lastName = lastName
        self.__Tel = Tel
        self.Accounts = [] 
    def get_cin(self):
        return self.__cin
    def get_firstName(self):
        return self.__firstName
    def get_lastName(self):
        return self.__lastName
    def get_Tel(self):
        return self.__Tel
    def set_Tel(self,Tel):
        self.__Tel = Tel
    
    def Display(self):
        print(f"CIN: {self.__cin}, NAME: {self.__firstName} {self.__lastName}, TEL: {self.__Tel}")
    
    def MultipleAccontes(self):
        NewAccontes = Account(self)
        self.Accounts.append(NewAccontes)
        return NewAccontes
    def My_Accounts(self):
        try:  
            if self.Accounts == []:
                 raise ValueError 
            else:
                print(f" Accounts of {self.get_firstName()} {self.get_lastName()}")
                for i, NewAccontes in enumerate (self.Accounts, start=1):
                 print(f"{i}.:") 
                 NewAccontes.Display()
        except ValueError:
            print(f" Accounts of {self.get_firstName()} {self.get_lastName()}")
            print ("There is no Account for this Client")

            
class Account:
    __nbAccounts = 0
    def __init__(self, Owner):
        Account.__nbAccounts +=1
        self.__code = Account.__nbAccounts
        self.__balance = 0.0
        self.__owner = Owner
        self.History = [] # list for the transactions

    def get_code(self):
        return self.__code
    def get_balance(self):
        return self.__balance
    def get_owner(self):
        return self.__owner
    def credit (self,amount,account=None):
        if amount>0:
          if account is None:
                self.__balance += amount
          else:
              self.__balance += amount
              account.debit(amount)
        else:
           print("The Operation Is NOT VALID")

    def debit (self,amount,account=None):
        if amount>0:
            if self.__balance >= amount:
                self.__balance -= amount
                if account is not None:
                    account.credit(amount)
            else:
                    print("Insufficient balance.")
        else:
           print("The Operation Is NOT VALID")       

    def Display(self):
        print(f"Account Code: {self.__code}")
        print(f"Owner: {self.__owner.get_firstName()} {self.__owner.get_lastName()}")
        print(f"Balance: {self.__balance} DA")
    
    @staticmethod
    def displayNbAccounts ():
        print ("Total account created:", Account.__nbAccounts)
    
    def display_history(self):  
        for i in self.History:
            i.display()

class Transaction:
    counter = 00
    def __init__(self,account,TRtype,amount):
        Transaction.counter += 1
        self.__id = f"TR-{Transaction.counter}"
        self.__date = time.strftime("%Y/%m/%d %H:%M:%S")
        self.__account = account
        self.__TRtype = TRtype 
        self.__amount = amount
        account.History.append(self)

    def get_id (self):
        return self.__id
    def get_date (self):
        return self.__date
    def get_account (self):
        return self.__account
    def get_amount (self):
        return self.__amount
    def get_TRtype (self):
        return self.__TRtype
    def display (self):
       print(f"{self.__id} , Account {self.__account.get_code()} ,{self.__TRtype} , Amount: {self.__amount} DA , Date: {self.__date}")

class Credit (Transaction):
    def __init__(self, account, amount):
        super().__init__(account,"credit", amount)
        account.credit(amount)

class Debit (Transaction):
    def __init__(self, account, amount):
        super().__init__(account,"debit", amount)
        account.debit(amount)

class Transfer (Transaction):
    def __init__(self,source_account,target_account, amount):
        self.__source = source_account
        self.__target = target_account
        super().__init__(source_account,"transfer", amount)
        self.transfer()
    def get_source(self):
        return self.__source
    def get_target(self):
        return self.__target
    
    def transfer (self):
        amount = self.get_amount()
        if self.__source.get_balance() >= amount :
            self.__source.debit (amount)
            self.__target.credit (amount)
        else:
            print ("Insufficient Balance.")
