def z3_1():
    # Ten kod jest poprawny skladniowo zarowno w python2 jak i python3
    x = 2 ; y = 3 ;
    if (x > y):
        result = x;
    else:
        result = y;
    print(result)

    # Kod linijke nizej jest niepoprawny
    # for i in "qwerty": if ord(i) < 100: print i
    # Poprawny kod w python2: (gdzie print jest instrukcja)
    for i in "qwerty":
        if ord(i) < 100:
            print(i)

    # Kod poprawny w python2, w python3 trzeba odpowiednio zastosowac print().
    # Poprawny, zakomentowany w celu kompatybilnosci
    # for i in "axby": print ord(i) if ord(i) < 100 else i
    for i in "axby": print(ord(i) if ord(i) < 100 else i)

def z3_2():
    pass

def z3_3():
    pass

def z3_4():
    pass

def z3_5():
    pass

def z3_6():
    pass

def z3_8():
    pass

def z3_9():
    pass

def z3_10():
    pass

z3_1();
z3_2();
z3_3();
z3_4();
z3_5();
z3_6();
z3_8();
z3_9();
z3_10();
