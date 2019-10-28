#!/usr/bin/python3
# -*- coding: utf-8 -*-

def z3_1():
    # Ten kod jest poprawny skladniowo zarowno w python2 jak i python3
    x = 2 ; y = 3 ;
    if (x > y):
        result = x;
    else:
        result = y;
    assert result == 3

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
    L = [3, 5, 4] ; L = L.sort()
    # Powyzszy kod, dziala, jest semantycznie poprawny, ale dziala inaczej
    # niz mozna podejrzewac. Metoda sort() klasy list sortuje ja i zwraca None,
    # ktore jest nastepnie przypisane do L. Wywolujac type(L) otrzymujemy
    # <class 'NoneType'>
    assert type(L) == type(None)

    # x, y = 1, 2, 3 
    # Powyzszy kod jest niepoprawny ze wzgledu na inna ilosc zmiennych po
    # lewej stronie przypisania i wyrazen po prawej. Wyjatek ValueError

    # X = 1, 2, 3 ; X[1] = 4
    # Pierwsze wyrazenie to przypisanie trzyelementowej tablicy do zmiennej X
    # (jak najbardziej poprawne), natomiast drugie wyrazenie to proba przypisa-
    # nia drugiemu elementowi krotki wartosci - tego zrobic sie nie da:
    # zwracany jest wyjatek TypeError

    # X = [1, 2, 3]; X[3] = 4
    # Kod niepoprawny - X jest tablica, gdzie ostatni indeks to 2. Przypisanie
    # powoduje wyjatek IndexError

    # X = "abc" ; X.append("d")
    # X jest stringiem, ktory nie ma metody append, wyjatek AttributeError
    
    # map(pow, range(8))
    # Funkcja pow wymaga podania dwoch argumentow, a podany jest tylko jeden:
    # range(8). Przykladowy dzialajacy kod:
    L = [0, 1, 4, 9, 16, 25, 36, 49]
    M = map(pow, range(8), [2 for x in range(8)])
    for (x, i) in zip(L, M):
        assert x == i

def z3_3():
    for i in range(31):
        if i % 3 == 0:
            print(i)

def z3_4():
    while True:
        x = input('Wpisz liczbe rzeczywista: ')
        try:
            x = float(x)
            print(x, x**3)
        except:
            if x == 'stop':
                break
            else:
                print('Nie podano liczby rzeczywistej')

def z3_5():
    length = int(input('podaj dlugosc miarki: '))
    miarka = ('|....' * length) + '|'
    miarka += '\n0'
    for i in range(1, length+1):
        miarka += ("%5d" % i)
    print(miarka)

def z3_6():
    x = int(input('dlugosc prostokota: '))
    y = int(input('wysokosc prostokota: '))
    prostokat = ''
    for i in range(y):
        prostokat += ('+---' * x) + '+\n'
        prostokat += ('|   ' * x) + '|\n'
    prostokat += ('+---' * x) + '+'
    print(prostokat)

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
