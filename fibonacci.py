# program to find nterms of fibonacci

# nterms = int(input("enter a number"))

# n1,n2 = 0,1
# c=0
# if (nterms < 0):
#     print("enter a positive number")
# elif nterms==1:
#     print(n1)
# else:
#     while c < nterms:
#         print(n1)
#         n3= n1 + n2
#         n1 = n2
#         n2 = n3
#         c += 1

# fibonacci using function

def fibonacci(n):

  if (n<0):
    print("incorrect input")
  elif (n==0):
    return 0
  elif n==1 or n==2 :
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(9))


