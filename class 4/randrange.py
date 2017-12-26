from random import*
for x in range(1,11):
    a=randint(1,9)
    b=randrange(12,19)
    print(a,'*',b)
    c=int(input())
    if(c==(a*b)):
        print('correct')
    else:
        print('wrong')
