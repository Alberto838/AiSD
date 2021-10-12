imie = input("Podaj imie: ")
nazwisko = input("Podaj nazwisko: ")

def foo(imie, nazwisko):
    return imie[0].title() + '. ' + nazwisko.title()

def foo2(imie, nazwisko, sth):
    return sth(imie, nazwisko)

print(foo2(imie, nazwisko, foo))

