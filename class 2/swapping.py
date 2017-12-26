#wap a programme to swap using two nos using three variables

print("enter value of x and y")
x,y=int(input()),int(input())
print("before swapping x={0} and y={1}".format(x,y))
z=x
x=y
y=z
print("after swapping x={0} and y={1}".format(x,y))


print("enter value of a and b")
a,b=int(input()),int(input())
print("before swapping a={0} and b={1}".format(a,b))
a=a+b
b=a-b
a=a-b
print("after swapping a={0} and b={1}".format(a,b))
