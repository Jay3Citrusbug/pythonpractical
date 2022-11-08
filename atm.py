import random
history_list=[]
class atm():
    
    def __init__(self,username,acco_number,balance=0):
        self.name = username
        self.account_number = acco_number
        self.balance = balance
    
    def user_account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available balance: Nu.{self.balance}\n")
         
    
    def deposite(self):
        amount=int(input("enter deposite amount : "))
        self.balance=self.balance+amount
        history_list.append("credit amount {}".format(self.balance))
        print("your total balance is",self.balance)
        
    def withdraw(self):
        amount=int(input("enter the withdraw amount : ")) 
        
        if amount>self.balance:
            print(f"your balance is {self.balance} so withdraw low amount")   
    
        else:    
            self.balance=self.balance-amount
            history_list.append("debit amount {}".format(self.balance))
            print("after withdraw your balance is",self.balance)
    
    def check_balance(self):
        print("your acount balance is ",self.balance)
        history_list.append("your balance amount is {}".format(self.balance))
         
    def history(self):
        global history_list
        for i in history_list:
            print(i)
        
    def transaction(self):
        
        print("""
            TRANSACTION 

            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
            6. History
        """)
        
        while True:
            try:
                opt=int(input("enter the number from menu: "))
            except:
                print("please enter valid number in menu")
            else:
                if opt==1:
                    obj.user_account_detail()
                elif opt==2:
                    obj.check_balance()
                elif opt==3:
                    obj.deposite()
                elif opt==4:
                    obj.withdraw()
                elif opt==6:
                    print("your history is")
                    obj.history()
                    
                
                elif opt == 5:
                    print(f"""
                printing receipt..............
          ******************************************
              Transaction is now complete.                         
              Transaction number: {random.randint(10000, 1000000)} 
              Account holder: {self.name.upper()}                  
              Account number: {self.account_number}                
              Available balance: Nu.{self.balance}                    
 
              Thanks for choosing us as your bank                  
          ******************************************
          """)
                    

    
        
        
        
        
        
name=input("enter your name :")
number=int(input("enter your account number :"))        
        
obj=atm(name,number)     


while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        obj.transaction()
    elif trans == "n":
        print("""Thanks for choosing us as your bank  Visit us again! 
        """)
        break
    
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")
        
        
        
        
        
        
        

          
        