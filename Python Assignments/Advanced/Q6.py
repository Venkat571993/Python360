class car:
    def __init__(self):
        self.wheels = 4
        self.colours = ["red","blue","green"]
        self.type =["Hatchback","Sedan","Suv"]


    def price(self,cost):
        self.cost = cost
        if cost >100000 :
            return  "Luxury"
        elif cost > 60000:
            return "Mid-range"
        else:
            return "Basic"




class Hyundai(car):

    def accessories(self):
        self.rim = "Alloy"
        self.key ="Keyless"

class Audi(Hyundai):
    pass

class Countries:

    def class_check(self):
        print("USA,Canada")

class BMW(car,Countries):
    pass


##### Single Inheritance

car1 =Hyundai()
print(car1.price(50000))
print(car1.colours)

##### Multiple Inheritence
car2 = BMW()
print(car2.wheels)
car2.class_check()
# print(car2.countries_name)


##### Multilevel Inheritence
car3 = Audi()

print(car3.type)

