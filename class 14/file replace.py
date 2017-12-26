f=open('file1.txt','w')
l=['I is Delhi\n','This is I London\n']
f.writelines(l)
f.close()
g=open('file1.txt','r')
print(g.read())
g.close()
w=open('file1.txt','w')
for i in w:
    if(i=='I'):
        i.replace('I','We')
w.close()
o=open('file.txt','r')
print(o.read())
o.close()
        
