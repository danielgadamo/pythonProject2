 # num=int(input("enter number:"))
#
# while 99<=num<=999:
#  print((num//100)+(num//10%10)+(num%10))
#  num = int(input("enter number:"))
# print("error")

# age= int(input("enter number:"))
# while 0<=age<=120:
#     if 0<age<=18:
#         print("child")
#     elif 18<age<=60:
#         print("adult")
#     else:
#         print("senior")
#     age = int(input("enter number:"))


# num1 = int(input("enter number:"))
# num2 = int(input("enter number:"))
#
# while num1%2==0 and num2%2==0:
#     print(num1+num2)
#     num1 = int(input("enter number:"))
#     num2 = int(input("enter number:"))
#
# print(num1*num2)


# num1 = int(input("enter number:"))
# num2 = int(input("enter number:"))
#
# while num1+num2==10:
#     num1 = int(input("enter number:"))
#     num2 = int(input("enter number:"))
# print("end")

# grade=0  תרגיל 5
# sum=0
# count=0
# while 0<=grade<=100:
#     grade = int(input("enter grade"))
#     if grade>=60 and grade<=100:
#       count = count + 1
#       sum=sum+grade
#
#
#
# sum=sum/count
# print("the average is",sum)

grade=0
sum=0
sum2=0
count=0
count2=0
while 0<=grade<=100:
    grade = int(input("enter grade"))
    if grade>=60 and grade<=100:
      count+=1
      sum=sum+grade
    elif grade>=0 and grade<=100:
        sum2+=grade
        count2+=1


sum=sum/count
sum2=sum2/count2
print("the averages is", sum, sum2)




