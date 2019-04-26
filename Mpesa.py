class MpesaAccount:
    def __init__(self,name,phone_no):
        self.name=name
        self.phone_no=phone_no
        self.balance=0
        self.deposits=[]
        self.withdraws=[]
        self.loan=0
    def deposit(self,deposit_amount):
        deposit=deposit_amount
        self.balance=self.balance+deposit_amount
        self.deposits.append(deposit_amount)
        customer="Hi {},deposited sh.{} to your account.Your balance is {}".format(self.name,deposit_amount,self.balance)
        print(customer)
    def withdraw(self,withdraw_amount):
        withdraw=withdraw_amount
        if self.balance>withdraw_amount:
            self.balance=self.balance-withdraw_amount
            self.withdraw.append(withdraw_amount)
            customer="Hi {},withdrew sh.{} to your account.Your balance is {}".format(self.name,withdraw_amount,self.balance)
            print(customer)
        else:
            print("insufficient balance")
    def check_balance(self):
        check_balance=self.balance
        customer="Hi {},your balance is sh.{}".format(self.name,self.balance)
        print(customer)
    def my_deposits(self):
        for deposit_amount in self.deposits:
            print(deposit_amount)
    def my_withdrawals(self):
        for withdraw_amount in self.withdraw:
            print(withdraw_amount)
    def give_loan(self,amount):
        loan=amount
        if len(self.deposits)>=5 and amount<1/3*sum(self.deposits) and self.loan==0:
            self.loan=self.loan+amount
            print("successful!Your loan has been approved")
        else:
            print("loan not approved")
    def loan_repayment(self,money):
        repayment=money
        if self.loan>money:
            self.loan=self.loan-money
            customer="Hi {},you have paid a loan of {}.Your remaining loan balance is{}".format(self.name,money,self.loan)
            print(customer)
        elif self.loan<money:
            over_payment=money-self.loan
            self.balance=self.balance-self.loan
            self.balance=self.balance+over_payment
            customer="Hi {}, you have paid sh.{}.Your have fully paid your loan.Your over_payment added to balance of sh.{}".format(self.name,money,self.balance)
            print(customer)
        
        else:
            print("not applicable")



