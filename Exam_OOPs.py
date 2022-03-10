class Student(object):

    def __init__(self, name, roll_number, admn_no, college):
        self.name = name
        self.roll_number = roll_number
        self.admn_no = admn_no
        self.college = college

    def displayDetails(self):
        print(self.name + "\n" + self.roll_number + "\n" + self.admn_no + "\n" + self.college)

class Exam(Student):

    def __init__(self, name, roll_number, admn_no, college, exam_name, english, maths, physics, chemistry):
        self.exam_name = exam_name
        self.english = english
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry

        Student.__init__(self, name, roll_number, admn_no, college)

    def printDetails(self):
        print("Name =", self.name)
        print("Roll Number =", self.roll_number)
        print("Admission Number =", self.admn_no)
        print("College =", self.college)
        print("Exam Name =", self.exam_name)
        print("English =", self.english)
        print("Maths =", self.maths)
        print("Physics =", self.physics)
        print("Chemsitry =", self.chemistry)

# new class has been created for the implementation of the inherit with parent to child. ****
# but, it is not to perfromed to inherit child to parent or viceversa.****

new_class = Exam("Sameer", "30", "45", "Adhiyamaan College of Engineering", "SSLC", "45", "49", "44", "49")

new_class.printDetails()

new_class.displayDetails()