class Employee:

    add_emp=0
    increase=2

    def __init__(self,pay,name,age):
        self.pay=pay
        self.name=name
        self.age=age

        Employee.add_emp+=1

    def fullname(self):
        return"{}{}".format(self.name,self.age)

    def salary_hike(self):
        self.pay = int(self.pay*self.increase)
    
print(Employee.add_emp)

lohit=Employee(2,"lohit",21)
print(Employee.add_emp)

rekha=Employee(3,"rekha",23)
print(Employee.add_emp)

lohit=Employee(3,2,43)

print(Employee.add_emp)