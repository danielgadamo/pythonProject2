# num1=int(input("enter a number"))
# num2=int(input("enter a number"))
#
# if (num1+num2)%2==0:
#     print("zugi")
# else:
#     print("ei zugi")

# num1=int(input("enter a number"))
# if -999<num1<-99 or 99<num1<999:
#   if num1>0:
#     print((num1//100)+(num1//10%10)+(num1%10))
#   else:
#     print((-num1//100)+(-num1//10%10)+(-num1%10))
# else:
#     print("error")
day=int(input("enter a number"))
month=int(input("enter a number"))
year=int(input("enter a number"))

if 0<day<=31 and 0<month<=12 and 1950<year<2020:
    print(f"{day}/{month}/{year//10%10}{year%10}")
else:
    print("error")





