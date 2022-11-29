x = input("string= ")
y = x.split(",")
for i in range(0, len(y)):
    y[i] = int(y[i])
    y[i] = y[i]**2
for i in range(0, len(y)):
    y[i] = str(y[i])
a = ",".join([str(elem) for elem in y])
print("string=", a)