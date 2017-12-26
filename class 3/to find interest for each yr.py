'''an invester deposite 1000 with lic policy and receive the statement on
an annual rate of 6% annually for 5 yrs.wap to find the interest and principal
for each year '''

p=10000
print('initial principal=',p)
for i in range(5):
    k=(5*6*p)/100
    p=p+k
    print('interest for',i+1,'year=',k)
