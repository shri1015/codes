#  remove i’th character from string 
str1 = "helloeveryone"
str2 = " "


for i in range(len(str1)):
    if i!=3:
      str2 = str2 + str1[i]

print(str2)