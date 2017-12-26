'''wap to display prime no bw 1 to 100'''
for i in range(1,100):
    c=0
    for j in range(2,i//2+1):
        if(i%j==0):
            c=c+1
    if(c==0):
        print(i,'is prime')
    else:
        print(i,'is not prime')
