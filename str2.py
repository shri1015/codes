# Reverse words in a given String in Python
str1 = "hello the weather is nice outside"
str2 = str1.split()[::-1]
l1 = []
for i in str2:
    l1.append(i)

print(" ".join(l1))
