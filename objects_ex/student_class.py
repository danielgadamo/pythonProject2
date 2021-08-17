
class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.grades={}

    def add_grade(self,subject,grade):
        self.grades[subject]=grade

    # def __str__(self):
    #     return f"name:{self.name} id:{self.id} the grades list is {self.grades}"

    def __repr__(self):
        return f"name:{self.name} id:{self.id} the grades list is {self.grades}"


    def calc_factor(self,factor,subject):
        self.grades+=self.grades[subject]*factor/100
        return self.grades

    def avarage(self):
        avarage=0
        for i in self.grades:
            avarage+=self.grades[i]
        return avarage/len(self.grades)

    def avarage2(self,dic1):
     for i in dic1:
       sum1 = 0
       for k in dic1.values():
        if type(k) is int :
         sum1+=k
       return  sum1/len(dic1)-1

#     list5.append(sum1/len(i))
        # avarage = 0
        # for j in dic1.values:
        #   if type(j) is int:
        #     avarage += dic1[j]
        # return (avarage / len(dic1))

student2=Student("11","yoni")
# student2.grades=[80,90,100,90,95]
print(student2)
print(student2.name)
# sum1=0
dic4={'a':'111',"b":90,'c':90,"d":100}

# list5=[]
list4=[{1:70,2:90,3:95,4:100},{1:90,2:85,3:95,4:95}]
# for i in list4:
#     sum1 = 0
#     for k in i.values():
#       if type(k) is int :
#        sum1+=k
#     list5.append(sum1/len(i))
# print(list5)
# print(list4)


for i in list4:
 print(type(i))
 print(student2.avarage2(i))
