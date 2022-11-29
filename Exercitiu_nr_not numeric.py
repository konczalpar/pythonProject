a=0
while True:
    x = input("Introduceti numarul: ")
    if x.isnumeric():
        x = int(x)
        a = a+x
    else:
        if x == "":
            print("Total result:",a)
            a=0
        else:
            print("Value is not numeric")