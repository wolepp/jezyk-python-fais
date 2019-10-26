line = """To jest wielowierszowy
tekst z ciagiem GvR wewnatrz
zapisany do zmiennej
o nazwie line"""
word = "Konstantynopol"
L = [1, 1, 2, 3, 5, 8, 11, 100]
duza_liczba_calkowita = 235125032030634069206324980

def z2_10():
    print(len(line.split()))

def z2_11():
    print('_'.join(list(word)))

def z2_12():
    pierwszeZnaki = ''
    ostatnieZnaki = ''
    for w in line.split():
        pierwszeZnaki += w[0]
        ostatnieZnaki += w[-1]
    print('pierwsze znaki: ' + pierwszeZnaki)
    print('ostatnie znaki: ' + ostatnieZnaki)

def z2_13():
    print(len(''.join(line.split())))

def z2_14():
    max_length = 0
    longest_word = ''
    for word in line.split():
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    print('najdluzsze slowo: "%s", znakow: %d' % (longest_word, max_length))

def z2_15():
    print(''.join([str(x) for x in L]))

def z2_16():
    print(line.replace('GvR', 'Guido van Rossum'))

def z2_17():
    print(sorted(line.split(), key=str.lower))
    print(sorted(line.split(), key=len))

def z2_18():
    print(str(duza_liczba_calkowita).count('0'))

def z2_19():
    print(''.join([str(x).zfill(3) for x in L]))

z2_10()
z2_11()
z2_12()
z2_13()
z2_14()
z2_15()
z2_16()
z2_17()
z2_18()
z2_19()
