compare = ['0', 'poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela']

i = int(input("Podaj liczbe od 1 do 7: "))

def foo(compare, i):
    return compare[i]

print(foo(compare, i))