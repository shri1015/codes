# Test if List contains elements in Range
lst = [3,5,6,7,9]
i,j = 2, 9
res = True
for i in lst:
    if i<2 or i>9:
        res = False

print("does List contains elements in Range", res)
