# finding the summation of digits of numbers
lst = [23, 67, 19, 45, 12, 80, 14]
li = []
for i in lst:
    sum = 0
    for digit in str(i):
        sum = sum + int(digit)
    li.append(sum)

print("the sum of digit is = ", li)
