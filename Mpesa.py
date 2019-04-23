class MpesaAccount:
	def __init__(self,name,phone_no,balance):
		self.name=name
		self.phone_no=phone_no
		self.balance=balance
	def deposit(self,deposit_amount):
		deposit=deposit_amount
		self.balance=self.balance+deposit_amount
		customer="Hi {},deposited sh.{} to your account.Your balance is {}".format(self.name,deposit_amount,self.balance)
		return customer
	def withdraw(self,withdraw_amount):
		withdraw=withdraw_amount
		self.balance=self.balance-withdraw_amount
		customer="Hi {},withdrew sh.{} from your account.Your balance is {}".format(self.name,withdraw_amount,self.balance)
		return customer
	def check_balance(self):
		check_balance=self.balance
		customer="Hi {},your balance is sh.{}".format(self.name,self.balance)
		return customer
