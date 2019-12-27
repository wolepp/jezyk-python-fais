"""
Moduł zawiera funkcje sortujące listy.
"""


def swap(L, left, right):
    """Zamiana miejscami dwóch elementów."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item

# ===========================================


def selectsort(L, left, right):
    for i in range(left, right):
        k = i
        for j in range(i+1, right+1):
            if L[j] < L[k]:
                k = j
        item = L[k]
        while k > i:
            L[k] = L[k-1]
            k = k-1
        L[i] = item

# ===========================================


def insertsort(L, left, right):
    for i in range(left+1, right+1):   # L[left] jest posortowany
        item = L[i]
        j = i
        while j > left and L[j-1] > item:
            L[j] = L[j-1]   # robimy miejsce na item
            j = j-1
        L[j] = item

# ===========================================


def bubblesort(L, left, right):
    # Wersja ulepszona wg Sysły.
    limit = right
    while True:
        k = left-1   # lewy wskaźnik przestawianej pary
        for i in range(left, limit):
            if L[i] > L[i+1]:
                swap(L, i, i+1)
                k = i
        if k > left:
            limit = k
        else:
            break

# ===========================================


def shakersort(L, left, right):
    # Wersja na podstawie Wróblewskiego.
    k = right
    while left < right:
        for j in range(right, left, -1):   # od prawej
            if L[j-1] > L[j]:
                swap(L, j-1, j)
                k = j
        left = k
        for j in range(left, right):   # od lewej
            if L[j] > L[j+1]:
                swap(L, j, j+1)
                k = j
        right = k

# ===========================================


def shellsort(L, left, right):
    h = (right - left) // 2
    while h > 0:
        for i in range(left + h, right + 1):
            for j in range(i, left + h - 1, -h):
                if L[j - h] > L[j]:
                    swap(L, j - h, j)
        h = h // 2


# ===========================================

def quicksort(L, left, right):
    # Wersja wg Kernighana i Ritchiego.
    if left >= right:
        return
    swap(L, left, (left + right) // 2)   # element podziału
    pivot = left                      # przesuń do L[left]
    for i in range(left + 1, right + 1):   # podział
        if L[i] < L[left]:
            pivot += 1
            swap(L, pivot, i)
    swap(L, left, pivot)     # odtwórz element podziału
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)

# ===========================================


def mergesort(L, left, right):
    """Sortowanie przez scalanie."""
    if left < right:
        middle = (left + right) // 2   # wyznaczanie środka
        mergesort(L, left, middle)
        mergesort(L, middle + 1, right)
        merge(L, left, middle, right)   # scalanie


def merge(L, left, middle, right):
    """Łączenie posortowanych sekwencji."""
    T = [None] * (right - left + 1)
    left1 = left
    right1 = middle
    left2 = middle + 1
    right2 = right
    i = 0
    while left1 <= right1 and left2 <= right2:
        if L[left1] <= L[left2]:   # mniejsze lub równe
            T[i] = L[left1]
            left1 += 1
        else:
            T[i] = L[left2]
            left2 += 1
        i += 1
    # Lewa lub prawa część może mieć elementy.
    while left1 <= right1:
        T[i] = L[left1]
        left1 += 1
        i += 1
    while left2 <= right2:
        T[i] = L[left2]
        left2 += 1
        i += 1
    # Skopiuj z tablicy tymczasowej do oryginalnej.
    for i in range(right - left + 1):
        L[left + i] = T[i]
