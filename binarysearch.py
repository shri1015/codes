def binarysearch(arr, low , high, x):

    if high >= low:
        mid = (high+ low)//2
        if arr[mid] == x:
          return mid
        elif arr[mid] < x:
          return binarysearch(arr, mid+1, high , x)
        else:
          return binarysearch(arr, low, mid-1, x)
    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10
result = binarysearch(arr, 0, len(arr)-1, x)
if result != -1:
    print ("element is present" , str(result))
else:
    print("element is not present")