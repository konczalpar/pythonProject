import random
nr_calc = random.randint(1,10)
nr_util = int(input("Introduceti numarul: "))
print("Numarul dumneavoastra:", nr_util)
print("Numarul calculatorului:", nr_calc)
if nr_util == nr_calc:
    a = bool(1)
else:
    a = bool(0)
print("Hit:", a)