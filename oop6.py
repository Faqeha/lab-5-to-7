#Lab6:
#Qno1:

# class Course:
#     def __init__(self, course_code, course_name):
#         self.course_code = course_code
#         self.course_name = course_name

#     def display_info(self):
#         print(f'Course Code: {self.course_code}')
#         print(f'Course Name: {self.course_name}')
# if __name__ == "__main__":
#     course = Course("AI555", "programming fundamentals")
#     course.display_info()

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

# class Course:
#     def __init__(self, course_code, course_name):
#         self.course_code = course_code
#         self.course_name = course_name

#     def display_info(self):
#         print(f'Course Code: {self.course_code}')
#         print(f'Course Name: {self.course_name}')


# class UndergraduateCourse(Course):
#     def __init__(self, course_code, course_name, year_level):
#         super().__init__(course_code, course_name)
#         self.year_level = year_level

#     def additional_info(self):
#         print(f'Year Level: {self.year_level}')


# class GraduateCourse(Course):
#     def __init__(self, course_code, course_name, research_area):
#         super().__init__(course_code, course_name)
#         self.research_area = research_area

#     def additional_info(self):
#         print(f'Research Area: {self.research_area}')


# def register_course():
#     course_type = input("Enter course type (Undergraduate/Graduate): ").strip().lower()
    
#     course_code = input("Enter course code: ")
#     course_name = input("Enter course name: ")

#     if course_type == 'undergraduate':
#         year_level = input("Enter year level (1, 2, 3, or 4): ")
#         course = UndergraduateCourse(course_code, course_name, year_level)
    
#     elif course_type == 'graduate':
#         research_area = input("Enter research area: ")
#         course = GraduateCourse(course_code, course_name, research_area)
    
#     else:
#         print("Invalid course type. Please enter 'Undergraduate' or 'Graduate'.")
#         return None

#     return course

# if __name__ == "__main__":
#     registered_course = register_course()
    
#     if registered_course:
#         print("\nRegistered Course Information:")
#         registered_course.display_info()
#         registered_course.additional_info()



