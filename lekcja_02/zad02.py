line = """To jest wielowierszowy
tekst zapisany
do zmiennej
o nazwie line"""
word = "Konstantynopol"

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
    print('piewrsze znaki: ', pierwszeZnaki)
    print('ostatnie znaki: ', ostatnieZnaki)

def z2_13():
    print(len(''.join(line.split())))

def z2_14():
    max_length = 0
    for word in line.split():
        if len(word) > max_length:
            max_length = len(word)

def z2_15():
    pass

def z2_16():
    pass

def z2_17():
    pass

def z2_18():
    pass

def z2_19():
    pass

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
