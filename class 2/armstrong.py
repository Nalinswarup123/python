n=int(input('enter a no'))
i=n
sum=0
while(i!=0):
    x=i%10
    i=i//10
    sum=sum+x**3

if(sum==n):
    print('no is armstrong')
else:
    print('no is not armstrong!!')


# 153, 370, 371, 407
