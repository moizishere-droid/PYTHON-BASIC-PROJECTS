# ATM Simulator - Simulate basic ATM functionalities (check balance, deposit, withdraw)

class ATM:

    def __init__(self):
        self.total_amount=2000

    def Check_balance(self):
        print(f"THE TOTAL BALANACE IS : {self.total_amount} ")

    def Deposit(self,money):
        self.total_amount+=money
        self.Check_balance()

    def Withdraw(self,money):
        self.total_amount-=money
        self.Check_balance()

    @staticmethod
    def print_list():
        print("ENTER 1 to check balance")
        print("ENTER 2 to deposite")
        print("ENTER 3 to with draw")
        print("ENTER 4 to exit")
        print("\n")

muobj = ATM()
muobj.print_list()
i = int(input("enter your choice: "))
while(i!=4):

    muobj.print_list()
    if(i==1):
        muobj.Check_balance()
    elif(i==2):
        money = int(input("enter the money: "))
        muobj.Deposit(money)
    elif(i==3):
        money = int(input("enter the money: "))
        muobj.Withdraw(money)
    elif(i==4):
        break
    i = int(input("enter your choice again: "))
