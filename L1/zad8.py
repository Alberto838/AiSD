list = []

for i in range(4):
    a = input("Podaj liczbe: ")
    list.append(a)

def zamien(list):
    return tuple(list)

print(zamien(list))
