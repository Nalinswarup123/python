n=7
k=0

while(n!=0):
    for l in range(0,n-1):
        print(' ',end='')
    n=n-1
    print("*",end='')
    for j in range(1,k*2):
        if(n==3):
            if((j%2)!=0):
                print(' *',end='')
        else:
            print(" ",end='')     
    k=k+1
    if(k>1 and n!=3):
        print('*')
    else:
        print('')
  
    
    
    
     
        

    
        
    
    
    

