class Planet:
    shape = "round"

    def __init__(self,name,radius,gravity):
        self.name = name
        self.radius = radius
        self.graavity = gravity

    def orbit(self):
        return f"{self.name} is orbiting in the {self.name}"

    @classmethod
    def commons(cls):
        return f"All planets are {cls.shape} because of gravity"

    @staticmethod
    def spin(speed="200 m.s"):
        return f"speed of the planet is {speed}"