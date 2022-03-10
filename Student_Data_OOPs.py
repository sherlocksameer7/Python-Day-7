class Student:

    def __init__(self,name,roll_number,admn_no,college):  # whenever the object is created there must be initialise of function has been performed.

        self.name = name
        self.roll_number = roll_number
        self.admn_no = admn_no
        self.college = college

    def printStudentData(self):  # In user defined functions never use the initialisation process.

        print(self.name)
        print(self.roll_number)
        print(self.admn_no)
        print(self.college)

get_Student_name = input("Enter the Student Name:\n")
get_Roll_number = input("Enter the Roll Number:\n")
get_admission_number = input("Enter Admission Number:\n")
get_college_name = input("Enter College Name:\n")

student_data = Student(get_Student_name,get_Roll_number,get_admission_number,get_college_name) # object creation


# (input("Enter the Student Name:\n"),  # it is an object creation and to read the data of the user manual.
#                        input("Enter the Roll Number:\n"),
#                        input("Enter the Admission Number:\n"),
#                        input("Enter the College Name:\n"))

student_data.printStudentData()  # this can be must in the printing indentation of only class, object line of alignment.