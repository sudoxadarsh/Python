x = int(input("upto how many terms: "))

a = 0

b = 1
print(f"{a} {b} ", end="")
for i in range(1, x):
    print(f"{a + b} ", end="")
    a = b
    b = i