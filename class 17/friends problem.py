#nth ugly no
#no of combination of 4 friends of being in couple or single
#f(n)=f(n-1)+(n-1)*f(n-2)
def count(n):
    dp=[]
    for i in range(n):
        if(i<=2):
            dp.append(i)
            print(dp)
        else:
            dp.append(dp[i-1]+(i-1)*dp[i-2])
            print(dp)
    return dp[n-1]
print(count(5))
