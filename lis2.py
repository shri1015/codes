# swap two element in a list

def swapelement(lst, pos1, pos2):

    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst


lst = [1,4 ,7 ,9, 10]
pos1 = 1
pos2 = 3
print(swapelement(lst, pos1-1, pos2-1))


# using function
li = ['hello', 2, 3, 'hi', 5, 6, 7, 8]
pos1 , pos2 = 1, 4
def interchange(li, pos1, pos2):
    temp = li[pos1]
    li[pos1]= li[pos2]
    li[pos2]= temp
    return li

print(interchange(li, pos1-1, pos2-1))