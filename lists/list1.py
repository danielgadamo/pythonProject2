# list1=[4,5,8,9,10,14]
# print(max(list1))
# print(min(list1))
# print(sum(list1) / len(list1))

# from random import randint
# list1=[]
# for i in range(10):
#    num=randint(1,100)
#    list1.append(num)
#
# print(list1)

# list1=[20,30,70,80,90]
# list2=[100,110,120,130,200]
# list3=list1+list2
# print(list3)
# print(len(list3))

# list2=[]
# list3=[]
# for i in range(10):
#     grade=int(input("enter grade:"))
#     if(grade>=60 and grade<=100):
#       list2.append(grade)
#     else:
#         list3.append(grade)
# print(len(list2),len(list3))

list1=[]
for i in range(1,11):
    list1.append(i)
print(list1)

list2=list1[-3:len(list1)]
print(list2)
print(list1[::2])
list3=list1[1::2]
print(list3)
print(list1)
# list1[4:6]=[10,100,list.append(100)]
# print(list1)
# list3//check gitmkm
list4=[]

for i in list1:
    list4.append(i*2)
print(list4)
list5=[list1[0],list1[len(list1)-1]]
print(list5)
