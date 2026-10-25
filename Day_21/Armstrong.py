num = int(input("enter number: "))
temp = num

length = len(str(num))

add = 0

try:
    while temp > 0:
        add += ((temp % 10) ** length)
        temp = temp // 10

    print(f" add: {add}")

    if  add == num:
        print(f" Number: {num} is an armstrog number")
    else:
        print(f" Number: {num} is not an armstrong number")

except Exception as e:
    print(f"{e}")

finally:
    print(f"Code executed with its desired output or exceptions")
 

