#wap which copy content from one file to another excluding the
#line containing '#'

x=input('enter content\n')
a=open('a.txt','w')
while x:
    a.write(x)
    a.write('\n')
    x=input()
a.close()

a=open('a.txt','r')
b=open('a2.txt','w')
x=a.readline()
while x:
    if x.find('#')>-1:
        p=x.find('#')
        x=x[:p]
        b.write(x)
        b.write('\n')
        x=a.readline()
    elif x.find('#')==0:
        x=a.readline()
    else:
        b.write(x)
        b.write('\n')
        x=a.readline()
    
