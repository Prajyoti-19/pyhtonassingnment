class Bank:
    def __init__(self,accno,name,balance):
        self.accno=accno
        self.name=name
        self.balance=balance
        
    def debit(self,amt):
        self.amt=amt
        if (self.balance >= self.amt):
            self.balance-=self.amt
        else:
            print('You had insufficient balance\n')
            
        
    def credit(self,amt):
        self.amt=amt
        self.balance+=self.amt
    
    def showbalance(self):
        print(f'Account No : {self.accno}, Name : {self.name}, Your Total balance is : {self.balance}\n')
            


b1=Bank(910, 'Prajyoti', 5000)


option=1 

while option==1:
    print(f'1. Debit\n 2.Credit\n 3.Show Balance\n 4.Exit\n')
    n=int(input('Select Option : '))
    if n==1:
        d1=int(input('Enter amount for Debit : '))
        b1.debit(d1)
    elif n==2:
        d1=int(input('Enter amount for Credit : '))
        b1.credit(d1)
    elif n==3:
        b1.showbalance()
    elif n==4:
        print('Exit\n')
    else:
        print('Invalid option selected\n')
    
    print('Do you want to continue ? \n 1. Yes\n 0. No')
    n1=int(input('Enter 1 or 0 : '))
    option=n1
    if option==0:
        print('Bye Bye\n')













# class Bank:
#     availbal=None
#     def __init__(self,accno,name,balance):
#         self.accno=accno
#         self.name=name
#         self.balance=balance
#         self.availbal=balance
        
#     def debit(self,amt):
#         self.amt=amt
#         if (self.balance >= self.amt):
#             self.availbal=self.balance-self.amt
#         else:
#             self.availbal=self.balance
#             print('You had insufficient balance\n')
            
        
#     def credit(self,amt):
#         self.amt=amt
#         self.availbal=self.balance+self.amt
    
#     def showbalance(self):
#         print(f'Your Total balance is : {self.availbal}\n')
            


# b1=Bank(910, 'pogo', 5000)


# option=1 

# while option==1:
#     print(f'1. Debit\n 2.Credit\n 3.Show Balance\n')
#     n=int(input('Select Option : '))
#     if n==1:
#         d1=int(input('Enter amount for Debit : '))
#         b1.debit(d1)
#     elif n==2:
#         d1=int(input('Enter amount for Credit : '))
#         b1.credit(d1)
#     elif n==3:
#         b1.showbalance()
#     else:
#         print('Invalid option selected\n')
    
#     print('Do you want to continue ? \n 1. Yes\n 0. No')
#     n1=int(input('Enter 1 or 0 : '))
#     option=n1














