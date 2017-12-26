#f1=open('akk.txt','r')
#f2=open('abc.txt','w')
k=4
def call():
    k=k-1
    while k>0:
        print(k)
        call()
call()
