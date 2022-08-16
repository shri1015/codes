# find the sum and average of the list
lst = [23, 67, 9, 45, 12, 80, 4]
sum= 0
count = 0
avg= 0
for i in lst:
    sum= sum+i
    count = count + 1
    avg = sum / count

print("sum =", sum)
print("average =",avg)