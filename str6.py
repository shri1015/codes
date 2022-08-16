# Count the Number of matching characters in a pair of string
str1 = "aaaabcdefg"
str2 = "dfghijkl"

str1_set = set(str1)
str2_set = set(str2)

matched_string = str1_set & str2_set

print(len(matched_string))


