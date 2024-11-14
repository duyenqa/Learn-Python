class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayInfo(self):
        print("Name:, ", self.name)
        print("Age:, ", self.age)


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name,age)
        self.major = major

    def show(self):
        super().displayInfo()
        print("Major: ", self.major)


student = Student("Kim Duyen", 30, "IT")
student.show()