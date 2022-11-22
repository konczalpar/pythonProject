salar_brut = int(input("Salar brut: "))
angajat_IT = input("Angajat IT \'YES/NO\': ")
angajat_PT = input("Angajat Part time \'YES/NO\': ")

if angajat_IT == "YES":
    print(salar_brut - salar_brut*0.35)
    if angajat_PT == "YES":
        print(salar_brut - salar_brut * 0.40)
else:
    print(salar_brut*0.45)