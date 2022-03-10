class Person(object):  # object can be taken as the parent. *** Parent Class ***

    def __init__(self, name, aadhar, phone):
        self.name = name
        self.aadhar = aadhar
        self.phone = phone

    def displayDetails(self):
        print(self.name + "\n" + self.aadhar + "\n" + self.phone)

class Employee(Person):  # child class

    def __init__(self, name, aadhar, phone, salary, designation):
        self.salary = salary
        self.designation = designation

        Person.__init__(self, name, aadhar, phone)

    def printDetails(self):
        print("Name =", self.name)
        print("Aadhar =", self.aadhar)
        print("Phone =", self.phone)
        print("Salary =", self.salary)
        print("Designation =", self.designation)

x = Employee("Sherlock", "2345677889", "8263783928", "30000", "Software")

x.printDetails()  # property of a child

x.displayDetails()  # property of a parent

# y = Person("Name", "48462674", "2374873628784")