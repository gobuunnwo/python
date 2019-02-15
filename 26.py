class planet:
    shape="round"
    
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def orbit(self):
        return f"{self.name} age is {self.age}"

# クラスメソッドはインスタンス化しなくても呼び出すことができますが、
# インスタンスからでも呼び出すことができます。
# クラス直下のshape="round"（def~の外）に接続するための@classmethod。
    @classmethod
    def commons(cls):
        return f"All the planets are {cls.shape}"

# naboo is instance
naboo=planet("naboo",400)
print(planet.shape)
print(planet.commons())
print(naboo.commons())

