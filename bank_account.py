class BankAccount:
    
    Bank_name = "BigBank"
    
    def __init__(self, int_rate = .01, balance = 1):
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if BankAccount.sufficient_funds(self.balance, amount):
            self.balance-=amount
            return self
        else:
            print("Insufficint Funds: Charging a $5 fee!") 
            self.balance -= 5
            return self
        


    def display_account_info(self):
        print(f"Account Balance:${self.balance}")
        return self
    
    def yield_interest(self):
        print(f"Interst Yielded: ${self.balance*self.int_rate}")
        return self
    
    @staticmethod
    def sufficient_funds(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

Carl = BankAccount(.03, 12)
Alan = BankAccount( .05, 500000)
jin = BankAccount(.01, 1)


Carl.deposit(600000).deposit(200000).deposit(50000).withdraw(20).yield_interest().display_account_info()

Alan.deposit(1000000).deposit(300000).withdraw(250000).withdraw(20000).withdraw(7000).withdraw(10000).yield_interest().display_account_info()

jin.deposit(1).withdraw(10).display_account_info()