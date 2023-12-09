# ex-1 ,2 ,3 and 4 combined
import random


class Car:
    def __init__(self,regPlate, maxSpeed):
        self.regPlate = regPlate
        self.maxSpeed = maxSpeed
        self.speed = 0
        self.odometer = 0

    def accelerate(self,acceleration):

        # if 0 <= (self.speed+ acceleration) <= self.maxSpeed:
        #    self.speed += acceleration #can use these two lines or line 13, it is the same

        self.speed = min(max(self.speed+acceleration, 0),self.maxSpeed )


    def drive(self,time):
        self.odometer += self.speed * time



porsche = Car("ABC-313", 240)
print(f"Register plate {porsche.regPlate}, Max speed {porsche.maxSpeed} km/h,"
      f"Current speed {porsche.speed} km/h, Odometer {porsche.odometer} km")

porsche.accelerate(30)
porsche.accelerate(70)
porsche.accelerate(50)
print(f"Current speed is {porsche.speed} km/h")
porsche.accelerate(-200)
print(f"Current speed is {porsche.speed} km/h")

porsche.accelerate(60)
porsche.drive(1.5)
print(f"Distance travelled {porsche.odometer} km")

cars = []
# cars.append(Car("ABC-1", random.randint(100,200))) #can change ABC-2,3 and so on but we loop now
for i in range(10):
    cars.append(Car("ABC-" + str(i + 1), random.randint(100, 200)))

odomax = 0.
while odomax < 10000.:
    for car in cars:
        car.accelerate(random.randint(-10,15))
        car.drive(1.)
        odomax = max(car.odometer, odomax)

for car in cars:
    print(f"{car.regPlate:6s}: {car.maxSpeed}, {car.odometer}")
