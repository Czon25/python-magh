class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    #def __str__(self)-> str:
     #   return self.name
    def __ne__(self,obj):
        return self.age!=obj.age
    
ram=Person("ram",12)
shyam=Person("shyam",12)
print(ram!=shyam)
    
    