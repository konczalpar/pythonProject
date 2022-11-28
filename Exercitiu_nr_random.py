import random
nr_calc = random.randint(1,10)
while True:
    nr_util = int(input("Introduceti numarul: "))
    print("Numarul dumneavoastra:", nr_util)
    print("Numarul calculatorului:", nr_calc)
    a = nr_util == nr_calc
    print("Hit:", a)