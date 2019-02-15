
class Employee:
    def __init__(self,name,address):
        self.name = name
        self.address = address

    # 古い書き方
    def fullname(self):
        return "{}{}".format(self.name,self.address)

emp1 = Employee("A","a")
emp12= Employee("B","b")

print(emp1)
print(emp12)
print(emp1.name)
print(emp12.name)
print(emp1.address)
print(Employee.fullname(emp12))



