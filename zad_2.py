x=float(input("Podaj pierwszą liczbę: "))
y=float(input("Podaj drugą liczbę: "))
z=float(input("Podaj trzecią liczbę: "))

if x>y:
    x, y = y,x
if x>z:
    x, z = z,x
if y>z:
    y, z = z,y

print(f"Liczby w kolejnościod najmniejszej do największej: ")