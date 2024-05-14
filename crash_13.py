class Account:
  def __init__(self,balance,account_no):
    self.balance=balance
    self.account_no=account_no

  def debit(self,debit_value):
    self.balance=self.balance-debit_value
    return self.balance
  def credit(self,credit_value):
    self.balance=self.balance+credit_value
    return self.balance
  def print_value(self):
    print(self.balance)
a1=Account(500,12345)
a1.debit(100)
a1.credit(200)
a1.print_value()