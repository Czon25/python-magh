#OOP

class Burger:
    def bun(self):
        print("bun")
        return self
    def cheese(self):
        print("cheese")
        return self
    def patty(self):
        print("patty")
        return self
    
burger=Burger()
burger.bun().cheese().patty().bun()

