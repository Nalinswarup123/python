class employee:
    def __init__(self,n,s,a):
        self.name=n    #public
        self.salary=s  #public
        self.__age=a   #private
    def disp(self):
        print('name=',self.name)
        print('salary=',self.salary)
        print('age=',self.__age)

emp1=employee('sun',2000,35)
emp1.disp()
print(emp1.name)
print(emp1.salary)
print(emp1._employee__age)
