# ③
class Planet:
    def __init__(self,name,age,taste,friend):
        self.name=name
        self.age=age
        self.taste=taste
        self.friend=friend

#① creating a new method
    def new(self):
        return f'Im {self.name} and my best friend is {self.taste}..and my age {self.age}'

# ②
megumi=Planet('megumi','2000','sweet',34)
print(f'{megumi.name}')
print(f'{megumi.age}')
print(f'{megumi.taste}')
print(f'{megumi.friend}')

# ④
lohit=Planet('lohit','2000','sweet',34)
print(f'{lohit.name}')
print(f'{lohit.age}')
print(f'{lohit.taste}')
print(f'{lohit.friend}')

#②method
obj=Planet("raghu",20,390,120)
print(obj.new())


    