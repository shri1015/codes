n1 =input("enter no")
if(len(n1)>=3 and len(n1)<=7):
    for i in n1 :
        if(i.isalpha()):
          o=i
    print(o)
    for num in n1:
        if(num.isalpha()):
          j=n1.index(num)
    d1=n1[0:j]
    d2=n1[j+1:]
    if len(d1)>=1 and len(d1)<=3 and len(d2)>=1 and len(d2)<=3:
        print("the first no.is",d1,"second number is",d2)
        length=len(d1)
        lent=len(d2)
        if length >3:
            print("4th charater must be a,m,d,s")
        elif length <1:
           print("there is a digit required")
        elif lent > 3:
           print("there must be 3 digit")
        elif lent<1:
           print("there is a digit required")
        def sum(a,b):
            print("sum is= ",a+b)
        def subs(a,b):
            print("substraction is= ",a-b)
        def mul(a,b):
            print("Multiplication is= ",a*b)
        def div(a,b):
            print("Division is= ",a/b)
    else:
        print("length of numbers is not valid for opration")
        exit()
    if(o=="a"):
        sum(int(d1),int(d2))
    if(o=="s"):
        subs(int(d1),int(d2))
    if(o=="m"):
        mul(int(d1),int(d2))
    if(o=="d"):
        div(int(d1),int(d2))
else:
    print("String length mismatched")
