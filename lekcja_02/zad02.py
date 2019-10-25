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
    for w in line.split():
        pierwszeZnaki += w[0]
    print(pierwszeZnaki)

z2_10()
z2_11()
z2_12()
