#  print all Possible Combinations from the three Digits
def comb(li):

    for i in range(3):
        for j in range(3):
            for k in range(3):

                if li[i]!= li[k] and li[k]!= li[j] and li[j]!= li[i]:
                    print(li[i],li[j],li[k])

li = [1,2,3]
comb(li)