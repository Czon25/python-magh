class Person:
    def __init__(self,name,password):
        self.name=name
        #self._age=age
        self.__password=password
        
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,password):
        self.__password=password
        
person=Person("name","password")
person.password="naya wala"
print(person.password)

    
    