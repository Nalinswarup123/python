un='nalin'
ps='squad'
u=str(input('Enter user name'))
p=str(input('Enter password'))

if(u!=un):
    print('invalid user')
else:
    if(p==ps):
        print('login successful')
    else:
        for i in range(1,4):
            p=str(input('enter correct pwd'))
            if(p==ps):
                print('login successful')
                break
        if(i==3):
            print('not allowed')
