imie = input("Podaj imie: ")
nazwisko = input("Podaj nazwisko: ")

def foo(imie, nazwisko):
    return imie[0].title() + '. ' + nazwisko.title()

print(foo(imie, nazwisko))