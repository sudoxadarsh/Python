# Lexicographical Comparison

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if str1 < str2:
    print(f"{str1} is lexicographically smaller than {str2}")
elif str1 > str2:
    print(f"{str1} is lexicographically greater than {str2}")
else:
    print(f"{str1} and {str2} are equal")
