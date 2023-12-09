# ex-1
'''
class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(self.name, end = " ")

    def x(self):
        print("This is Mr. X")

class Book(Publication):
    def __init__(self,name,author,pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        super().print_information()
        print("(author" + self.author + "," + str(self.pages) + "pages)")


class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor



    def print_information(self):
        super().print_information()
        print("(Chief editor"+ self.editor + ")")




pubs = []
pubs.append(Magazine("Donald Duck", "Aki Hyppa"))
pubs.append(Book("Compartment No. 6", "Rosa Liksom", 192))

for pub in pubs:
    pub.print_information()
    pub.x()
'''

# ex-2

class Car:
    def __init__(self, max_speed, reg_number):
        self.max_speed = max_speed
        self.reg_number = reg_number
        self.distance = 0
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, time):
        distance = self.speed * time / 60
        self.distance += distance

class ElectricCar(Car):
    def __init__(self, max_speed, reg_number, battery_capacity):
        super().__init__(max_speed, reg_number)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, max_speed, reg_number, tank_volume):
        super().__init__(max_speed, reg_number)
        self.tank_volume = tank_volume

electric_car = ElectricCar(180, "ABC-15", 52.5)
gasoline_car = GasolineCar(165, "ACD-123", 32.3)

electric_car.accelerate(150)
gasoline_car.accelerate(140)

electric_car.drive(180)
gasoline_car.drive(180)

print(f"Electric car {electric_car.reg_number} drove {electric_car.distance} km.")
print(f"Gasoline car {gasoline_car.reg_number} drove {gasoline_car.distance} km.")