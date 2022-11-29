while True:
    varsta = int(input("Introdceti varsta: "))
    if not varsta in range(16, 70):
        print("No acces")
    elif varsta >=18:
        print("Acces")
    else:
        gen = input("Introduceti genul (f/m): ")
        if gen == "m":
            print("No acces")
        else:
            print("Acces")
