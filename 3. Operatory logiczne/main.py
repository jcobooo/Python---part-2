wiek = int(input("Wpisz swój wiek: "))
czyA2 = True if input("Czy masz prawo jazdy kat. A2? (t/n): ") \
    in ("t", "ta", "tak", "T") else False
odIluA2 = 0
if czyA2:
    odIluA2 = int(input("Jak długo masz A2? Podaj ilość lat: "))

if wiek>=24 or (czyA2==True and odIluA2>=2 and wiek>=20):
    print("Mozesz przystapic do egzaminu")
    pass
else:
    print("Nie mozesz przystapic do egzaminu")
    pass
