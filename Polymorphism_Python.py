#Function Overloading
def add(a,b):
    return a+b


def add(a,b,c):
    return a+b+c

#add(2,3) will throw an error


def check(a:str):
    print(a)
def check(a:int):
    print(a)

#check("2") WILL GIVE ERROR

#Then how to achive Function Overloading

def add(*args):
    result=0
    for item in args:
        result+=item
    return result
print(add(6,7,8,9))

#OR you can achieve method overloading using

def add_variables(a,b,c=0,d=0):
    print(a+b+c+d)

add_variables(1,2,3,5)   #will result in 11
add_variables(1,2)       #will result in 3


# Function Overriding

class Car:
    def __init__(self, SeatingCapacity, Speed, make, model):
        self.SeatingCapacity = SeatingCapacity
        self.Speed = Speed
        self.make = make
        self.model = model
        print("Constructor of Class")

    def run(self):
        print("Parent Car is running")

    def __str__(self):
        return f"This car has seating capacity of {self.SeatingCapacity} and Speed of {self.Speed}"

    def __del__(self):
        print("Deleting Car")
class FuelCar(Car):
    def __init__(self,SeatingCapacity,Speed,Make,Model,FuelCapacity):
        print("Constuctor of Fuel Car")
        super().__init__(SeatingCapacity,Speed,Make,Model)
        self.FuelCapacity=FuelCapacity

    def run(self):
        print("Fuel Car is running")
    def __del__(self):
        print("Deleting Fuel Car")
class ElectricCar(Car):
    def __init__(self,SeatingCapacity,Speed,Make,Model,BatteryCpacity):
        print("Constructor of Electric Car")
        super().__init__(SeatingCapacity,Speed,Make,Model)
        self.BatteryCapacity=BatteryCpacity
    def __del__(self):
        print("Deleting Electric Car")

    def run(self):
        print(self.Speed)
        print(self.make)
        print("Electric Car is running")


EC = ElectricCar(2, 300, "Ferrari", 2023, 50)
FC = FuelCar(4, 300, "Land Cruiser", 2023, 50)

EC.run()
FC.run()