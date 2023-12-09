# ex-1 and 2 and 3 and 4
'''
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom


    def floor_up(self):
        if self.current < self.top:
            print(f"Moving up from {self.current} to {self.current + 1}")
            self.current += 1
            return True
        else:
            return False

    def floor_down(self):
        if self.current > self.bottom:
            print(f"Moving down from {self.current} to {self.current - 1}")
            self.current -= 1
            return True
        else:
            return False

    def go_to_floor(self,floor):
        if floor > self.current:
            for n in range(floor - self.current):
                self.floor_up()
        elif floor < self.current:
            for n in range(self.current - floor):
                self.floor_down()
        else:
            print(f"We are currently on the floor {self.current}")

# h = Elevator(1,6)
# target_floor = int(input("To what floor you want to go?"))
# h.go_to_floor(target_floor)
# h.go_to_floor(1)

# ex-2
class Building:
    def __init__(self,bottom,top,elevators):
        self.elevators = []
        for n in range(elevators):
            self.elevators.append(Elevator(bottom, top))


    def run_elevator(self, elevator, floor):
        print(f"Moving elevator {elevator}:")
        self.elevators[elevator-1].go_to_floor(floor)


    def fire_alarm(self):
        print("Fire alarm!")
        for e in self.elevators:
            e.go_to_floor(e.bottom)

building = Building( 1, 6, 3)
building.run_elevator(1, 5)
building.run_elevator(1, 5)
building.fire_alarm()
'''
import random
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

class Race:
    def __init__(self, name, kilometers, car_list):
        self.name = name
        self.kilometers = kilometers
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(60)

    def print_status(self):
        print(f"Status of {self.name}:")
        print("| Reg. Number | Speed | Distance |")
        for car in self.car_list:
            print(f"| {car.reg_number}       | {car.speed} km/h |   {car.distance} km |")
        print()

    def race_finished(self):
        for car in self.car_list:
            if car.distance >= self.kilometers:
                return True
        return False

cars = []
for i in range(10):
    max_speed = random.randint(100, 200)
    reg_number = "ABC-" + str(i + 1)
    car = Car(max_speed, reg_number)
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)
hour = 0
winner = None
while not winner:
    hour += 1
    race.hour_passes()
    if race.race_finished():
        winner = max(cars, key=lambda x: x.distance)
    if hour % 10 == 0 or winner:
        race.print_status()

print("The race is over!")
print(f"The winner is {winner.reg_number} with a distance of {winner.distance} km.")

