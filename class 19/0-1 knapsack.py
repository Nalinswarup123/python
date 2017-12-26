def knapsack(val, wt, W, n):
    K = [[0] * (W + 1) for i in range(n)]
    print(K)
    for i in range(n):
        for j in range(W + 1):
            if j == 0:
                K[i][j] = 0
            elif wt[i] <= j:
                K[i][j] = max(val[i] + K[i - 1][j - wt[i]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]
    print(K)
    return K[n-1][W]


wt = list(map(int, input().split()))
val = list(map(int, input().split()))
W = int(input())

val = [x for _,x in sorted(zip(wt,val))]
#wt=list(wt)
wt.sort()

print(wt)
print(val)
print(knapsack(val, wt, W, len(wt)))
