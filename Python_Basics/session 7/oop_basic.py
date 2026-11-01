class Atm:
    #constructor(Special Function)/// No need to call function explicitly Automatically called by creating its object 
    def __init__(self):
        self.accountno=0
        self.pin=''
        self.balance=10000
        self.menu()
    def menu(self):
        user_input=input("""
        Hi How Can I help You?
        1. Press 1 To Create Pin
        2. Press 2 To Change Pin
        3. Press 3 To Check Balance
        4. Press 4 To Withdraw
        5. Anything Else to Exit
        """)
        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.change_pin()
        elif user_input=='3':
            self.check_balance() 
        elif user_input=='4':
            self.withdraw()
        else:
            exit()
    def create_pin(self):
        user_accountnum=input("Enter Account No. : ")
        user_pin=input("Enter Pin: ")
        self.pin=user_pin
        self.accountno=user_accountnum

        print("Pin Created Successfully")
        self.menu()
    def change_pin(self):
        user_accountnumber=input("Enter Account No. : ")
        if(user_accountnumber==self.accountno):
            old_pin=input("Enter old Pin: ")
            if(old_pin==self.pin):
                self.pin=input("Enter New Pin: ")
            else:
                print("Access Denied")
        else:
            print("Account Not Found ")
        self.menu()     
    def check_balance(self):
        user_account=input("Enter Account No.")
        if(user_account==self.accountno):
            pin_cb=input("Enter Pin ")
            if(pin_cb==self.pin):
                print(self.balance)
            else:
                print("Access Denied")
        else:
            print("Account Not Found ")
        self.menu()
    def withdraw(self):
        user_accountn=input("Enter Account No. : ")
        if(user_accountn==self.accountno):
            pin_wd=input("Enter Pin ")  
            if(pin_wd==self.pin):
                with_amt=int(input("Enter Withdrawl Amount "))
                if(with_amt<=self.balance):
                    self.balance=(self.balance)-with_amt
                    print("Withdrawl Sucessfull ")
                    print("Remaining Amount: ",self.balance)
                else:
                    print("Not Enough Money in your Account ")
            else:
                print("Access Denied")            
        else:
            print("Account Not Found ")
        self.menu()


obj = Atm()
print(type(obj))