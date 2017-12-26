#copying one file into another
f1=open('myfile.txt','r')
f2=open('new_file.txt','w')
for i in f1:
    f2.write(i)
f1.close()
f2.close()

f2=open('new_file.txt','a+')
print(f2.read())
l=['#h i']
f2.writelines(l)    #writelines is used to write list as well as string in a file but    
f2.seek(0,0)        #write is used to insert string in a file but not list
print(f2.read())
f2.close()

#copying file and skip if "#" or " "
f3=open('#file.txt','w')
f2=open('new_file.txt','r')
for i in f2:
    for j in range(len(i)):
        if(i[j]=='#' or i[j]==' '):
            continue
        else:
            f3.write(i[j])
f2.close()
f3.close()
f3=open('#file.txt','r')
print(f3.read())
f3.close()
