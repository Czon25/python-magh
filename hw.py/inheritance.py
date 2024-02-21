class GrandFather:
    house="good house"
class Father(GrandFather):
    car="lambo"
    def __init__(self):
        print(self.car)
        super().__init__()
class Mother:
    jewllary="gold"
    def __init__(self):
        print("I am mother")
class Son(Father):
    console="PS5"
    def __init__(self):
        print(self.console)
        super().__init__()
son=Son()
#print(son.jewllary,son.car)

