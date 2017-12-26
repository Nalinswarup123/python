import pickle
l=[1,2]
f1=open('pick.asd','wb')
pickle.dump(l,f1)
f1.close()
f2=open('pick.asd','rb')
nl=pickle.load(f2)
print(nl)
f2.close()
