# extract all elements whose frequency is greater than K.
test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3
res = []

for i in test_list:
    freq = test_list.count(i)
    if freq > k  and i not in res:
        res.append(i)

print(res)