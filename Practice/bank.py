class bank:
    def __init__(self):
        self.customer={}
    def create_account(self,account_no,initial_bal=0):
        if account_no in self.customer:
            print("Account already")
        else:
            self.customer[account_no]=initial_bal
            print("Account created succesfully")

    def deposit(self,account_no,amount):
        if account_no in self.customer:
            self.customer[account_no]+=amount
            print("Amount deposited successfully")
        else:
            print("Account doesnt exist")

    def withdrawal(self,account_no,amount):
        if account_no in self.customer:
            if self.customer[account_no]>=amount:
                self.customer[account_no]-=amount
                print("withdrawal successfully")
            else:
                print("Insufficient balance")
        else:
            print("Account doesnt exist")
    def check_balance(self,account_no):
        if account_no in self.customer:
            balance=self.customer[account_no]
            print(f"account balance is {balance}")
        else:
            print("Account doesnt exist")

newcustomer=bank()
newcustomer.create_account("sagar",1000)
newcustomer.check_balance("sagar")
newcustomer.deposit("sagar",1000)
newcustomer.check_balance("sagar")