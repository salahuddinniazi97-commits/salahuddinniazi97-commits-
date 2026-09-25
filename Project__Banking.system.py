

#    ****** ..... Banking System ..... ******

class Acount():
    def __init__(self,balance,acount_no):
        self.balance = balance
        self.acount = acount_no

    def cradit(self,amount):
        self.balance += amount
        print("Rs.", amount ," was added")
        print("total amount was --" ,self.total_bal())

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount," was removing")
        print("total amount was --",self.total_bal())

    def total_bal(self):
        return self.balance


acc1 = Acount(10000 , 12345)
print(acc1.balance)
acc1.cradit(2000)
acc1.debit(3000)

