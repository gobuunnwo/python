class planet:
    shape="round"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def orbit(self):
        return f"{self.name} age is {self.age}"

    def lohitmethod(self):

        return f"{self.name}ith"

　　@staticmethod
    def spin(speed="200 m/s speed"):
        return f"earth speed is {speed}"

naboo = planet("nabboo",23)
# @staticmethodはオブジェクト（インスタンス）（naboo = planet("nabboo",23)）なしに動かせる
# ここでは、naboo~なしでprint(planet.spin())を動かせる
print(planet.spin())
print(planet.spin("i can run more fast"))

    


