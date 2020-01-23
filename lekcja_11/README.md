# Sortowanie

Zawiera moduły generujące różne listy liczb, funkcje sortujące oraz program do mierzenia czasu funkcji sortujących.

## Generowanie danych

Uruchomienie modułu wymaga **matplotlib**

Moduł `sort_test_data` zawiera funkcje do generowania różnych list liczb, np. losowe liczby całkowite, liczby prawie posortowane, itp. Uruchomiony rysuje za pomocą biblioteki matplotlib wykresy na podstawie list o różnych rozmiarach.

## Funkcje sortujące

Moduł `sort` zawiera różne funkcje sortujące:

* przez wybór (selectsort)
* przez wstawianie (insertsort)
* przez zamianę (bubblesort)
* przez wstrząsanie (shakersort)
* Shella (shellsort)
* szybkie (quicksort)
* scalanie (mergesort)

## Główny program

Wymaga **matplotlib**
Program `main` mierzy czasy sortowań listy z losowymi liczbami. Każdy algorytm badany jest dla list o wielkościach $10^2, 10^3, 10^4$. Algorytmy o złożoności mniejszej niż $O(N^2)$, to jest mergesort, quicksort oraz timsort (sortowanie Pythona), są dodatkowo badane dla list o wielkościach $10^5$ oraz $10^6$. 

Czasy mierzone są z użyciem modułu `timeit`.

Wyniki są wypisywane. Można też wyrysować wykresy przy użyciu biblioteki `matplotlib` odkomentowując na końcu pliku linię `# plot(wyniki)`.
