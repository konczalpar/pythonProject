x = input("string = ")
y = list(x)
lista = [y[1], y[3], y[5] + y[6], y[8], y[10] + y[11]]
for i in range(0, len(lista)):
    lista[i] = int(lista[i])
lista[0] = lista[0]**2
lista[1] = lista[1]**2
lista[2] = lista[2]**2
lista[3] = lista[3]**2
lista[4] = lista[4]**2
for i in range(0, len(lista)):
    lista[i] = str(lista[i])
a = ",".join([str(elem) for elem in lista])
print("string =", "\"" + a + "\"")
