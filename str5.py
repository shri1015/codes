# program to print even length words in a string
str1 = " this is a python programme"
str2 = str1.split(" ")
for i in str2:
    if len(i)%2==0:
      print(i)