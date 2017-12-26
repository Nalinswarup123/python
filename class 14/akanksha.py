import os
'''f1=open('akko.txt','r')
#f1.write('sb chutiye hai')
'''
'''f1.close()
f1=open('akki.txt','r')'''
'''
print(f1.read())
f1.close()'''

f2=open('akko.txt','w')
l=['hum +','sath ','sath ','hai ']
f2.writelines(l)


f2.close()

f2=open('akki.txt','a+')
print(f2.readlines())
print(f2.seek(10,0))
print(f2.readlines())
print(f2.tell())
f2.close()
#os.rename("akki.txt","akkkkkk.txt")

os.remove("file1.txt")

