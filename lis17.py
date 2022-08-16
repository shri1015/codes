# Our task is to print the element which occurs 3 consecutive times in a Python list.
lst = [4, 5, 5, 5, 3, 8]
size = len(lst)
for i in range(size - 2):
    if lst[i] == lst[i +1] and lst[i+1 ] == lst[i + 2]:
        print(lst[i])