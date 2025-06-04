# creating student class and student manager class
class Student:
    def __init__(self,stu_id,name,branch):
        self.stu_id = stu_id
        self.name = name
        self.branch = branch
    
# creating a student manager which will manage all the functionalities
class studentmanager:
    def addstudent(self):
        f = open("sms/stdfile.txt","a")
        stu_id = int(input("Enter student id: "))
        name = input("enter student name: ")
        branch = input("enter student branch: ")
        student = Student(stu_id,name,branch)
        f.write(f"student: {name} id: {stu_id} branch: {branch}"+'\n')
        f.close()
    # adding a view students method
    def viewstudents(self):
        with open("sms/stdfile.txt","r") as f:
            data = f.read()
            print("--student records are--")
            print(data if data else "no records found")
# main function
def main():
    sm = studentmanager()
    print("select one option:")
    print('''1. Add Student
    2. View Students
    3. Update Student
    4. Delete Student
    5. Exit''')
    option = int(input())
    if(option == 1):
        sm.addstudent()
    elif(option == 2):
        sm.viewstudents()
    
main()
# '''1. Add Student
# 2. View Students
# 3. Update Student
# 4. Delete Student
# 5. Exit'''
# def addstudent():
#     f = open("sms/stdfile.txt","a")
#     stu_id = int(input("Enter student id: "))
#     name = input("enter student name: ")
#     branch = input("enter student branch: ")
#     f.write(f"student: {name} id: {stu_id} branch: {branch}"+'\n')
#     f.close()
# print("select one option:")
# print('''1. Add Student
# 2. View Students
# 3. Update Student
# 4. Delete Student
# 5. Exit''')
# option = int(input())
# if(option == 1):
#     addstudent()