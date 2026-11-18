plik="notowania_gieldowe.txt"

with open(plik, "a") as file:
 file.write("\nALR, 113")

with open(plik,"r") as file:
    for line in file:
        print(line, end="")