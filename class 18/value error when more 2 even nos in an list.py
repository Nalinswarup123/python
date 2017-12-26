
def contains(l):
    c=0
    for  i in l:
        if (i%2==0):
            c+=1
        if(c==2):
            raise ValueError
    
try:
    contains([1,2,3,4])
except ValueError:
    print('abc')
   # raise ValueError('value error occured')
