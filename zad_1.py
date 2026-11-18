punkty=int(input("Podaj ilość zdobytych punktów: "))
if punkty>80:
    print("Zaliczenie egzaminu w terminie 0")
elif punkty<=80 and punkty>=50:
    print("Można poprawić wynik egzaminu")
else:
    print("Egzamin nie zaliczony. Wymagana poprawka!")