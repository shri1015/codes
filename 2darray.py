#creare 2D array with 4 rows and 5 columns
array=[[23,45,43,23,45],[45,67,54,32,45],[89,90,87,65,44],[23,45,67,32,10]]

# display array
print(array)

#access a row
#accessing row of index 1
print(array[1])

#access a coloumn
#accessing 3rd index of column of 1st index of row
print(array[1][3])

#insert values in array
array.insert(2, [1,2,3,4,5])
print(array)

#updating values of row
array[2] = [1,4,6,8,23]
print(array)

#updating values of column
array[3][1] = 89
print(array) 

#deleting any index
del array[3]
print(array)