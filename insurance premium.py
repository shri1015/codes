while 1:
 typ = input("user type (p/c)")
 amt = int(input("amount insured"))
 claims=int(input("no. of claims"))
 if typ == "p" :
      if amt < 100000:
        s=(amt*0.003)+50
        if claims == 0:
          s = (s * 0.1)
      elif amt >= 10000:
        s=(amt*0.0025)+50
        if claims == 0:
          s = ( s* 0.1)
          
      print("premium summary")
      print("amount insured =",amt)
      print("no of claims =",claims)
      print("premium=",s)
 elif typ == "c":
        if amt < 250000:
            s=(amt*0.005)+80
            if claims == 0:
                s=(s*0.15)
        elif amt>=250000:
             s=(amt*0.0075)+80
             if claims==0: 
                 s=(s*0.15)
             prem=s+80
        print("premium summary")
        print("amount insured =",amt)
        print("no of claims =",claims)
        print("premium=",s)
 a=input("another client (y/n)")
 if a=="n":
  break

    
    
