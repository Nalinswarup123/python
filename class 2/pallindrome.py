#Pallindrome

n=int(input('enter a no'))
rev=0
x=n
while(x!=0):
    rev=(x%10)+rev*10
    x=x//10
print('reverse of the no is ',rev)
if(rev==n):
    print("n is pallindrome")
else:
    print("no is not pallindrome")
    
