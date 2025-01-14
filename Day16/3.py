class Car:
    def __init__(self,name,brand):
        self.name=name 
        self.brand=brand
        
    def display(self):
        print(f'car name:{self.name}, brand:{self.brand}')

car1=Car("BE6","Mahindra")
car1.display()
    