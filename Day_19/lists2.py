x=[]
for i in range(1,11):
    x.append(i*i)

print(x)

y = [3,4]

x.append(y)

print(x)

x.extend(y)

print(x)