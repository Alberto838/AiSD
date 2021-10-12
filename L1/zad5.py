x = int(input("Podaj pierwsza liczbe: "))
y = int(input("Podaj druga liczbe: "))


def podziel(x, y):
    if x>0 and y>0:
        return (x/y)
    print("Liczba jest ujemna lub jest zerem")

print(podziel(x, y))