# Program to print duplicates from a list of integers
# List product excluding duplicates
list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
li = []
mul = 1
for i in list1:
    if i not in li:
        li.append(i)
        mul *= i
          
print(li)
print(mul)