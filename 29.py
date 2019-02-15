class employee:

    increase=2
    def __init__(self,pay,name,age):
        self.pay=pay
        self.name=name
        self.age=age

    def fullname(self):
        return "{}{}".format(self.name,self.age)

    def salary_hike(self):
        self.pay=int(self.pay*employee.increase)

lohit=employee(2,"lohit",21)
rekha=employee(3,"rekha",23)

print(lohit.pay)
# payの値が変化する
lohit.salary_hike()
print(lohit.pay)

# __dict__はdictionary
print(lohit.__dict__)

lohit.increase=10
print(lohit.__dict__)

print(lohit.increase)
print(lohit.name)

