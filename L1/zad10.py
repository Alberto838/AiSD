word = input("Podaj slowo: ")

def palindrom(word):
    if word == word[::-1]:
        print('1')
    else:
        print('0')

palindrom(word)

