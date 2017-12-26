from random import*
p=0
c=0
for i in range(1,6):
    a=int(input('enter 1 for rock, 2 for paper and 3 for scissor'))
    b=randrange(1,4)
    print('computer  enters:',b)
    if(a==b):
        p=p
        c=c
    elif(a>b):
        p=p+1
    else:
        c=c+1

if(c>p):
    print('you lost')
elif(c<p):
    print('you won')
else:
    print('match draw')
