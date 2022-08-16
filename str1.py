# program to check whether the string is Symmetrical or Palindrome
str1 = "khokho"
half = int(len(str1)/ 2)
if len(str1)%2 == 0:
    first_str = str1[:half]
    last_str = str1[half:]
else:
    first_str = str1[:half]
    last_str = str1[half+1 :]

if first_str == last_str :
    print("string is symmetrical")
else:
    print("string is not symmetrical")

if first_str == last_str[::-1]:
    print("string is palindrome")

else: 
    print("string is not palindrome")


