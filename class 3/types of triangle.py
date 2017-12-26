#wap to check the type of a triangle

print("enter sides of a triangle")
a,b,c=int(input()),int(input()),int(input())

if(a==b and b==c):
    print('triangle is equilateral')
elif(a!=b and b!=c):
    print('triangle is scalene')
else:
    print('traingle is isosceles')
