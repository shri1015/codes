def bubblesort(arr):
 
 for i in range (0, len(arr)-1):
     for j in range(len(arr)-1):
         if arr[j]>arr[j+1]:
             temp = arr[j]
             arr[j] = arr[j+1]
             arr[j+1] = temp
 return arr 

arr  = [5, 3, 8, 6, 7, 2]  
print ("unsorted list is ", arr)
# calling bubble sort function
print("sorted list is", bubblesort(arr))