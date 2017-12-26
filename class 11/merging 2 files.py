f1=open('myfile.txt','r')
f2=open('new_file.txt','r')
f3=open('merged.txt','w')
print('f1=  ',f1.read())
print('f2=  ',f2.read())
f1.seek(0)
f2.seek(0)
for i in f1:
    for k in range(len(i)):
        if(i[k]=='\n'):
            f3.write(' ')
        else:
            f3.write(i[k])
    for j in f2:
        f3.write(j)
        break
f1.close()
f2.close()
f3.close()
f3=open('merged.txt','r')
print('f3=  ',f3.read())
f3.close()
