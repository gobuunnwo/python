# new()メソッド

#③
class Planet:
    def __init__(self):
        self.name="Earth"
        self.age=12345
        self.gravity=9.8
        self.number=23456
#④
    def new(self):
        return f'Im {self.name} and my best friend is {self.gravity}..and my age {self.age}'
#①
name = Planet()
#②
print(name.new())