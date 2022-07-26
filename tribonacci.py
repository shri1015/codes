def tribonacci(m):

    if m<0:
        print("incorrect input")
    elif m==0:
        return 0
    elif m==1 or m==2:
        return 1
    elif m==3:
        return 2
    else:
        return tribonacci(m-1) + tribonacci(m-2)+ tribonacci(m-3)
print(tribonacci(5))