tast = input("Introduceti limba: ")

# tast_ro = ["RO", "ro", "Ro", "Romana", "romana", "ROMANA"]
# tast_eng = ["EN", "en", "En", "Engleza", "engleza", "ENGLEZA"]
# if tast in tast_ro:
#     print("Salut")
# if tast in tast_eng:
#     print("Hello")

if tast.lower() in "romana":
    print("Salut")
if tast.lower() in "engleza":
    print("Hello")