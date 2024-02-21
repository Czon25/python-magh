class House:
    window=10
    color="red"
    door=2
    
    #def set_window(self,window):
     #   self.window=window
        
    def get_window(self):
        return self.window
    def get_color(self):
        return self.color
    
ram_ko_ghar=House()
#print(ram_ko_ghar.door)
#print(ram_ko_ghar.color)
#ram_ko_ghar.set_window()
#print(ram_ko_ghar.window)

print(ram_ko_ghar.get_window())

print(ram_ko_ghar.get_color())
