# write a Python program to count Even and Odd numbers in a List.

lis = [12,13,15,17,99,44,84,63,46]
even = 0
odd = 0
for i in lis:
    if i % 2 == 0:
        even += 1
    else:
        odd+=1

print(even)
print(odd)
