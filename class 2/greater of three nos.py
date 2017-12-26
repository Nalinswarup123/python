#wap to find largest among three nos
print('enter three nos')
a,b,c=int(input()),int(input()),int(input())
if(b<a>c):
    print(a,'is largest')
elif(b>a and b>c):
    print(b,'is largest')
elif(c>a and c>b):
    print(c,'is largest')
