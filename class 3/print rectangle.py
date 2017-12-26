n=8
while(n!=0):
    
        if(n==8):
            for i in range(1,14):
                if(i%2==0):
                    print('*',end='')
                else:
                    print(' ',end='')
            print('')
        elif(n==1):
            for j in range(1,14):
                if(j%2==0):
                    print('*',end='')
                else:
                    print(' ',end='')
            print('')
        else:
            print(' ',end='')
            print('*',end='')
            for k in range(1,12):
                print(' ',end='')
            print('*')
        n-=1
        
