# class Person:
#     def __init__(self):
#         self.name = "Patty Pie"
#         self.gender = "Female"
#         self.weight = "170 lbs"
#         self.height = "5 ft 8 inches"
#         self.race = "Black"

#     def walk():
#         print("Walk")


# woman = Person()
# print(woman)


# class Table:
#     def __init__(self, width, height):
#         self.width = "40 inches"
#         self.height = "20 inches"
#         self.color = ""
#         self.material = ""


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.vin = ""
        self.color = ""
        self.speed = 0
        self.current_gear = "N"

    def change_gear(self, gear):
        self.current_gear = gear

    def drive(self):
        self.speed = 40
        # calling change gear function from within a function
        self.change_gear("4")
        print("Drive")

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed = 0

    def change_color():  # private function only inside the class (this isnt needed)
        pass


car = Car("Honda", "Accord")
print(car.speed)
car.drive()
car.brake
