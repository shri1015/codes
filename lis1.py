# interchange first and last element in a list

lst = [1, 4, 6, 7, 9]

temp = 0 
temp = lst[0]
lst[0] = lst[-1]
lst[-1] = temp
    
print(lst)



# using function
li=[1, 2,3,4,5,6,7,8]

def interchange(li):

    temp = li[0]
    li[0] = li[-1]
    li[-1]= temp
    return li

print(li)
print(interchange(li))