# write a Python program to print all even numbers in the given list
lis = [2,6,89, 45, 34, 90,62, 5, 44]
li =[]
for i in lis:
    if i % 2 == 0:
     li.append(i)

print("all even number =", li)

# write a Python program to print all odd numbers in the given list
lis = [2,6,89, 45, 34, 90,62, 5, 44]

for i in lis:
    if i % 2 != 0:
     print(i, end=" ")

