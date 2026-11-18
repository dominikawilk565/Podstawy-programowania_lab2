plik = "notowania_gieldowe.txt"

with open(plik, "r") as file:
    for line in file:
        print(line, end="")