from Mymodule import*

failide_kustutamine()

�mber_kirjuta_fail(input("Faili nimi: "))

kirjuta_failisse("P�evad.txt")

p�evad=loe_failist("P�evad.txt")
#1
print(p�aevad)
#2
for p�ev in p�evad:
    print(p�ev)


