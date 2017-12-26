#wap to display element at odd position in a word

s=(input('Enter a word'))
def cal(a):
    l=len(a)
    for i in range(0,l):
        if(i%2==0):
            print(a[i])
        

cal(s)
