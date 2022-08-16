# Avoid Spaces in string length
str1 = "hi i am very happy"
res = sum(not i.isspace() for i in str1)
print(res)
     