class account:
    def __init__(self,s_id,balance,interest):
        self.__s_id=s_id
        self.__balance=balance
        self.__interest=interest
        print('account has been created')
    def getmonthlyinterest(self):
        print('interest rate=',self.__interest)
    def checkbalance(self):
        print('available amount=',self.__balance)
    def deposite(self,m):
        self.__balance+=m
        print('amount deposited=',m)
    def withdrawal(self,m):
        self.__balance-=m
        print('amount withdrawal=',m)
l=[]
for k in range(10):
    l.append(account(k,100,2))
l[1].deposite(25)
l[1].checkbalance()
l[0].checkbalance()

