zmienna=str(input("Podaj literę: "))

if len(zmienna) == 1 and zmienna.isalpha():
    if zmienna.isupper():
        print(f"Twoja litera to {zmienna} i jest ona duża")
    else:
        print(f"Twoja litera to {zmienna} i jest ona mała")
else:
    print("To nie jest litera")