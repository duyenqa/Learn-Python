class Student:
    def __init__(self, name=None, rollNo=None):
        if name is None and rollNo is None:
            print("Constructor no param")
        else:
            self.name = name
            self.rollNo = rollNo
    def displayInfo(self):
        print("Name: ", self.name)
        print("ID: ", self.rollNo)

studentNoParam = Student()

studentParam = Student("Jenny", 2)
print("Constructor has param")
studentParam.displayInfo()