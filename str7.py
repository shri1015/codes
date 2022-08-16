# Least Frequent Character in String
str1="aaaabbgghik"

freq ={} 
for i in str1:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1

res = min(freq, key =freq.get) #for least frequency
result = max(freq, key =freq.get) #for max frequency
print(str(res))
print(str(result))
