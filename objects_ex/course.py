from objects_ex.student_class import Student
class Course:
    def __init__(self,num_of_corse,name_of_course,max):
        self.num=num_of_corse
        self.name=name_of_course
        self.max = max
        self.subjects_teachers={}
        self.students=[]

    def __repr__(self):
     return f"course:{self.name} number of course:{self.num} students max:{self.max } list:{self.students}"

    # def ____(self):
    #     return f" class: {self.students}  {self.subjects}"

    # def __eq__(self,other):
    #     if other is None:
    #         return False
    #
    #     if self.id == other.id:
    #         return True
    #     else:
    #         return False
    def add_student(self,student):
        if len(self.students)<self.max:
            self.students.append(student.name)
            return True
        else:
            return False

    def addfactor(self,factor,subject):
        for i in self.students:
            Student.grades=Student.calc_factor(factor,subject)

    # def del_student(self,Student.id):
    #     if Student.id in self.students:
    #         self.students.remove(Student)




num=int(input("enter number course"))
name=input("enter course name")
max=int(input("enter max number of students"))
course1=Course(num,name,max)
print(course1)

for i in range(5):
    subject = input("enter subject name")
    name1 = input("enter teacher name")
    course1.subjects_teachers[subject]=name1
print(course1.subjects_teachers)
num2=int(input("enter the number of student"))
list_of_all=[]
list4=[]
while num2>0:
    id=input("enter id")
    name_s=input("enter name")
    student1=Student(id,name_s)
    # course1.subjects_teachers[id]=name_s
    # course1.students.append(name)
    # list_of_all.append(id+" "+name_s)

    for i in course1.subjects_teachers:
        print(i)
        grade=int(input("enter grade"))
        student1.add_grade(name_s,id)
        student1.add_grade(i,grade)
    course1.add_student(student1)
    print(student1.grades)
    list4.append(student1.avarage2(student1.grades))
    list_of_all.append(student1.grades)
    # course1.students.append(student1.name)
    num2 = int(input("enter the number of student"))
#
print(list_of_all)
# print(course1)
print(len(list_of_all))

# if "111" in list_of_all:
#     print("aaa")
#     print(list_of_all.index(111))
#
# if "111" in list_of_all[0]:
#  print("bb")
#  if 111 in list_of_all[0]:
#      print("cc")
print(type(list_of_all))
newlist=list_of_all[0]
print(newlist)
print(type(newlist))
print(course1.students)
student3=Student("111","yosi")
# list4=[]
# for i in list_of_all:
#     list4.append(student3.avarage2(i))

print(list4)
