while True:
    select_lang = input("Choose language (en, ro, de): ")
    if select_lang.lower() in "english":
        a = int(input("First number: "))
        b = int(input("Second number: "))
        c = input("Operation (add, sub, mul, div): ")
        if c == "add":
            print("Result:", a+b)
        if c == "sub":
            print("Result:", a-b)
        if c == "mul":
            print("Result:", a*b)
        if c == "div":
            print("Result:", a/b)
    else:
        print("Unknow")
        continue

if select_lang.lower() in "romana":
    a = int(input("Primul numar: "))
    b = int(input("Al doilea numar: "))
    c = input("Operatia (add, sub, mul, div): ")
    if c == "add":
        print("Rezultat:", a+b)
    if c == "sub":
        print("Rezultat:", a-b)
    if c == "mul":
        print("Rezultat:", a*b)
    if c == "div":
        print("Rezultat:", a/b)

if select_lang.lower() in "deutsch":
    a = int(input("Geben Sie die erste Nummer ein: "))
    b = int(input("Geben Sie die zweite Nummer ein: "))
    c = input("Operation wahlen (add, sub, mul, div): ")
    if c == "add":
        print("Das Ergebnis ist:", a+b)
    if c == "sub":
        print("Das Ergebnis ist:", a-b)
    if c == "mul":
        print("Das Ergebnis ist:", a*b)
    if c == "div":
        print("Das Ergebnis ist:", a/b)