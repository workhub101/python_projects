class BankAccount:
    def __init__(self,name,balance) -> None:
       self.name=name
       self.balance=balance
    def withdraw(self):
        amount=int(input("how much do you want to withdraw"))
        if amount>0 and amount<= self.balance:
            self.balance=self.balance-amount
            print("the amount has been withdrawn")
        else:
            print("invalid amount")
    def deposit(self):
        amount=int(input("how much do you want to deposit"))
        if amount>0 :
            self.balance= self.balance+amount
            print("the amount has been deposited")
        else:
            print("the deposit failed to process")
    def viewaccount(self):
        print(f"You have {self.balance} dollars in your bank account")
    
    
flag=True
myaccount=BankAccount(name="Aditya",balance=0)

while(flag):
  
    
    print("Press 1 : If you want to withdraw your money")
    print("Press 2 : if you want to deposit  money")
    print("Press 3 : If you want to look at you total money")
    print("Press 4 : If you want to end you account")
    question=int(input("Please choose a option"))
    if question == 1:
        myaccount.withdraw()
              
    if question == 2:
        myaccount.deposit()
    
    if question == 3:
        myaccount.viewaccount()
            
    if question == 4:
        flag=False

    
