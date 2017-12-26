# make a calculator
print('1.Add')
print('2.Sub')
print('3.Mul')
print('4.Div')
y,z=int(input('Enter two nos')),int(input())
x=int(input('Enter your choice'))

def sum():
    print('Sum=',y+z)
def sub():
    print('sub=',y-z)
def mul():
    print('mul=',y*z)
def div():
    print('div=',y//z)
    
if(x==1):
    sum()
elif(x==2):
    sub()
elif(x==3):
    mul()
elif(x==4):
    div()
else:
    print('Enter valid choice')
