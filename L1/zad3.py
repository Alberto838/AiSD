firsttwo = input("Podaj dwie pierwsze cyfry aktualnego roku: ")
lasttwo = input("Podaj dwie ostatnie cyfry aktualnego roku: ")
rokur = input("Podaj rok urodzenia: ")

def foo(firsttwo, lasttwo, rokur):
    return int(firsttwo + lasttwo) - int(rokur)

print(f"Twoj rok urodzenia to: {foo(firsttwo, lasttwo, rokur)}")
