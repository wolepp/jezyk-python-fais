#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-

# TODO: sprawdzic kodowanie!

def zad4_2_miarka():
    length = int(input('podaj dlugosc miarki: '))
    miarka = ('|....' * length) + '|'
    miarka += '\n0'
    for i in range(1, length+1):
        miarka += ("%5d" % i)
    return miarka

def zad4_2_prostokat():
    x = int(input('dlugosc prostokota: '))
    y = int(input('wysokosc prostokota: '))
    prostokat = ''
    for i in range(y):
        prostokat += ('+---' * x) + '+\n'
        prostokat += ('|   ' * x) + '|\n'
    prostokat += ('+---' * x) + '+'
    return prostokat

def zad4_3(n):
    """Iteracyjna wersja funkcji factorial(n)."""
    if n < 0:
        raise ValueError('n musi byc naturalne')
    silnia = 1
    #TODO: silnia z 0?
    for i in range(1, n+1):
        silnia *= i
    return silnia

def zad4_4():
    pass

def zad4_5():
    pass

def zad4_6():
    pass

def zad4_7():
    pass

if __name__ == '__main__':
    print(zad4_3(4))
