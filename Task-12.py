class Student:
    def __init__(self, name, surname, course, math, phys, informatics):
        self.name = name
        self.surname = surname
        self.course = course
        self.math = math
        self.phys = phys
        self.informatics = informatics

    def average(self):
        print((self.math + self.phys + self.informatics) / 3)


student1 = Student("Tom", "Shelby", 3, 3, 4, 5)
student1.average()