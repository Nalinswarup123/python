hr,mint,a=int(input('Enter time:   hr:min am/pm')),int(input()),str(input())
h,m=int(input('Enter total time you want to in future:  hr:min')),int(input())
mn=mint+m
ho=hr+h
n=mn
if(mn>=60):
    n=mn%60
    x=mn//60
    ho=ho+x
if(ho>12):
    ho=ho%12


print('YOur new time is',ho,' : ',n,end='')
if(a=='am'):
    if(hr+h>=12 or ho==12):
        a='pm'
    else:
        a='am'

if(a=='pm'):
    if(hr+h>=12 or ho==12):
        a='pm'
    else:
        a=a
print(' ',a)
        
    


