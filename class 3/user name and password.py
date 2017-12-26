i=0
un='Nalin'
pwd='ssquad'
u=str(input('Enter user name'))

def val():
    p=str(input('Enter password'))
    if(p==pwd):
        print('Login successful...')
    else:
        val()
        i=i+1
        if(i==3):
            print('you are not allowed to login!!!')
           
if(u!=un):
    print('invalid user')
else:
    val()
    
   

    
            
