class Shape:
    def area(self, a, b=10):
        return a*b
    
p = Shape()
print(p.area(10))
print(p.area(10, 20))


class PrivateThing:
    def __init__(self):
        self.__sallay = 1000
    
    def get_sallary(self):
        return self.__sallay
    
    def set_sallary(self, sallary):
        self.__sallay = sallary

class PublicThing(PrivateThing):
    def __init__(self):
        super().__init__()
    
    def get_sallary_from_private(self):
        print(self._PrivateThing__sallay)

p = PublicThing()
p.get_sallary_from_private()

privateThing = PrivateThing()
print(privateThing.get_sallary())
privateThing.set_sallary(2000)
print(privateThing.get_sallary())


