class empl:
    ec=0
    def __init__(self,n,s):
        self.name=n
        self.salary=s
        empl.ec=s
        print('wakka')
    def disp(s):
        print('Name=',s.name)
        print('Salary=',s.salary)
    def emp(self):
        print('total emp=%d'%empl.ec)
emp1=empl('sun',2000)
emp2=empl('moon',1000)
emp1.disp()
print(emp1.name)
emp1.emp()
print(empl.ec)


#The self parameter in the init metthod is automatically set t reference the object that was just created

    
