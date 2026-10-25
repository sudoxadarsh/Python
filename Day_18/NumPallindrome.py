str1 = int(input())


temp = str(str1)

temp = temp[::-1]

if int(temp) == str1: 
    print("Yes, pallindrome")

else:
    print("not, pallindrome")