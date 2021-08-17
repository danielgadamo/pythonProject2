# word1=input("enter word")
# word2=input("enter word")
# c=0
# new=" "
# for i in word1:
#     if i in word2 and i not in new:
#          c += 1
#          new+=i
# print(c,new)



# # 5
# sen=input("enter sentence")
# word=input("enter word")
# # list1=[1,2,3,4,5,7,8,9,7,9]
# list1=[]
# beg=0
# st=len(sen)
# for i in range(sen.count(word)):
#  # if word in sen:
#      beg=sen.index(word,beg)
#      list1.append(beg)
#      beg += 1
# print(list1)
# if word in sen:////////////////////
#     print('a')
#     print(sen.index(word))
# if word in sen:
#     print(sen.index(word,4))
# ////////////////////////////

# 6
# sen=input("enter sen")
# new_sen=""
# for i in range(len(sen)):
#     if sen[i-1]==" " or i==0:
#         new_sen+=sen[i].capitalize()
#
#     else:
#         new_sen+=sen[i]
# print(new_sen)

# sen="kdkndc efewml;l dew;;"

7
char=input("enter char:")
sen=input("enter sen:")
new=""
for i in range (len(sen)):
    if sen[i]==char:
        new+=sen[i].capitalize()
    else:
     new+=sen[i]
print(new)



