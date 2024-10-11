#Lab 5
#Qno1:


class Item:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')

if __name__ == "__main__":
    item = Item("jane austen", "stephen covey")
    item.display_info()

#Qno2:

class Item:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')


class Book(Item):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def additional_info(self):
        print(f'Pages: {self.pages}')


class Magazine(Item):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    def additional_info(self):
        print(f'Issue Number: {self.issue_number}')

if __name__ == "__main__":
    book = Book("david copperfield", "charles dickens", 206)
    magazine = Magazine("the room on the roof", "huge", 200)

    print("Book Information:")
    book.display_info()
    book.additional_info()

    print("\nMagazine Information:")
    magazine.display_info()
    magazine.additional_info()



#Lab6:
#Qno1:

class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

    def display_info(self):
        print(f'Course Code: {self.course_code}')
        print(f'Course Name: {self.course_name}')
if __name__ == "__main__":
    course = Course("AI555", "programming fundamentals")
    course.display_info()

#Qno2:
class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

    def display_info(self):
        print(f'Course Code: {self.course_code}')
        print(f'Course Name: {self.course_name}')


class UndergraduateCourse(Course):
    def __init__(self, course_code, course_name, year_level):
        super().__init__(course_code, course_name)
        self.year_level = year_level

    def additional_info(self):
        print(f'Year Level: {self.year_level}')


class GraduateCourse(Course):
    def __init__(self, course_code, course_name, research_area):
        super().__init__(course_code, course_name)
        self.research_area = research_area

    def additional_info(self):
        print(f'Research Area: {self.research_area}')

if __name__ == "__main__":
    undergrad_course = UndergraduateCourse("SE232", "Probability and statistics", 3)
    grad_course = GraduateCourse("AI341", "Software engineering", "Machine Learning")

    print("Undergraduate Course Information:")
    undergrad_course.display_info()
    undergrad_course.additional_info()

    print("\nGraduate Course Information:")
    grad_course.display_info()
    grad_course.additional_info()



#Qno3:

class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

    def display_info(self):
        print(f'Course Code: {self.course_code}')
        print(f'Course Name: {self.course_name}')


class UndergraduateCourse(Course):
    def __init__(self, course_code, course_name, year_level):
        super().__init__(course_code, course_name)
        self.year_level = year_level

    def additional_info(self):
        print(f'Year Level: {self.year_level}')


class GraduateCourse(Course):
    def __init__(self, course_code, course_name, research_area):
        super().__init__(course_code, course_name)
        self.research_area = research_area

    def additional_info(self):
        print(f'Research Area: {self.research_area}')


def register_course():
    course_type = input("Enter course type (Undergraduate/Graduate): ").strip().lower()
    
    course_code = input("Enter course code: ")
    course_name = input("Enter course name: ")

    if course_type == 'undergraduate':
        year_level = input("Enter year level (1, 2, 3, or 4): ")
        course = UndergraduateCourse(course_code, course_name, year_level)
    
    elif course_type == 'graduate':
        research_area = input("Enter research area: ")
        course = GraduateCourse(course_code, course_name, research_area)
    
    else:
        print("Invalid course type. Please enter 'Undergraduate' or 'Graduate'.")
        return None

    return course

if __name__ == "__main__":
    registered_course = register_course()
    
    if registered_course:
        print("\nRegistered Course Information:")
        registered_course.display_info()
        registered_course.additional_info()





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


