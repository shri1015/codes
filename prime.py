# to find out number is prime or not
n = int(input("enter a number"))

if n > 0:
   
    for i in range(2,int(n/2)+1):
     if n % i ==0:
         print("number is not a prime number")
         break
    else:
        print("number is prime")
else:
    print("number is not a prime number")