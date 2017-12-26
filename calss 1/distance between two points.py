#distance between two points
print('enter first point')
x,y=int(input()),int(input())
print('enter second point')
a,b=int(input()),int(input())

x=((x-a)**2+(y-b)**2)**0.5
print('distance between the given points=',x)
#print('{} is the required distance'.format(x))
