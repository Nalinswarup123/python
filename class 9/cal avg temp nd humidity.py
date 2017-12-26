#daily temp and humidity
'''suppose a station records the temp and humidity
at each hr of everyday nd stores the data
for d past 10 days . the task is to calculate the
average daily temp nd humidity for the 10 days'''

from random import*
t=[]
h=[]

for i in range(25):
    t.append(randint(35,50))
    h.append(randint(10,30))
print('avg temp=',sum(t)/24)
print('avg humidity=',sum(h)/24)

