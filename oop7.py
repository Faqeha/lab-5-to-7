#Lab7:
#Task no 1:
#Qno1:
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f'Make: {self.make}')
        print(f'Model: {self.model}')
if __name__ == "__main__":
    vehicle = Vehicle("Honda", "Audi")
    vehicle.display_info()

#Qno2:


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f'Make: {self.make}')
        print(f'Model: {self.model}')


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def additional_info(self):
        print(f'Number of Doors: {self.num_doors}')

if __name__ == "__main__":
    car = Car("Honda", "Audi", 5)
    print("Car Information:")
    car.display_info()
    car.additional_info()

#Qno3:
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f'Make: {self.make}')
        print(f'Model: {self.model}')


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def additional_info(self):
        print(f'Number of Doors: {self.num_doors}')


class LuxuryCar(Car):
    def __init__(self, make, model, num_doors, features):
        super().__init__(make, model, num_doors)
        self.features = features

    def additional_info(self):
        super().additional_info()  
        print(f'Luxury Features: {", ".join(self.features)}')

if __name__ == "__main__":
    luxury_car = LuxuryCar("Audi e-tron", "E-Class", 5, ["Leather seats", "Sunroof", "Advanced sound system"])
    print("Luxury Car Information:")
    luxury_car.display_info()
    luxury_car.additional_info()

#Task no 2:
#Qno1:
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f'Name: {self.name}')
        print(f'Position: {self.position}')


if __name__ == "__main__":
    employee = Employee("Alice Johnson", "Software Engineer")
    employee.display_info()

#Qno2:

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f'Name: {self.name}')
        print(f'Position: {self.position}')


class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)
        self.department = department

    def additional_info(self):
        print(f'Department: {self.department}')


class Worker(Employee):
    def __init__(self, name, position, hours_worked):
        super().__init__(name, position)
        self.hours_worked = hours_worked

    def additional_info(self):
        print(f'Hours Worked: {self.hours_worked}')

if __name__ == "__main__":
    manager = Manager("Joge", "Director", "SE")
    worker = Worker("Stephen", "Technician", 40)

    print("Manager Information:")
    manager.display_info()
    manager.additional_info()

    print("\nWorker Information:")
    worker.display_info()
    worker.additional_info()


