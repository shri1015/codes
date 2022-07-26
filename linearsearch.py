#  Searching an element in a array in python
# linear

def search(arr, n, x):
    for i in range (0, n):
        if arr[i] == x:
            return i

    return -1

arr= [2,5,7,9,11]
x=7
n= len(arr)
result = search(arr, n, x)
if (result == -1):
   print("element not found")
else:
    print("element found", result)