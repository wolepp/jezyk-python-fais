# Algorytm Floyda-Warshalla

Znajdowanie najkrótszych ścieżek pomiędzy wszystkimi parami wierzchołków w grafie ważonym.

## Opis algorytmu

Algorytm F-W jest przykładem programowania dynamicznego. Służy do rozwiązania problemu najkrótszych ścieżek między wszystkimi parami wierzchołków w grafie skierowanym $G = (V, E)$. Graf $G$ może posiadać krawędzie z ujemnymi wagami, wtedy algorytm F-W może służyć do wykrywania ujemnych cykli w grafie, to jest takich, że suma wag krawędzi w ścieżce $(v_1, v_2, v_1$) jest ujemna.

Algorytm F-W korzysta z tego, że jeśli najkrótsza ścieżka pomiędzy wierzchołkami $v_1$ i $v_2$ prowadzi przez wierzchołek $u$, to ta ścieżka jest połączeniem najkrótszych ścieżek prowadzących z $v_1$ do $u$ oraz tych od $u$ do $v_2$.

Aktualne wyniki zapisywane są na bieżąco do macierzy `d`, to jest tablicy $n\times n$ ($n$ to ilość wierzchołków). Tablica ta jest wypełniona wartościami $\infty$ (w kodzie jest to `inf` z modułu `math`), a następnie wartości na diagonali są ustawiane na $0$.

Algorytm porównuje wszystkie możliwe ścieżki pomiędzy każdą parą wierzchołków. Używane są trzy zagnieżdzone pętle `for`, każda przechodzi przez wszystkie wierzchołki grafu. Wierzchołki te nazwijmy $i, j, k$ (w kodzie nazwy te zmienione są na `source`, `target` oraz `middle`). Dla każdego wierzchołka $i$ porównywana jest długość ścieżki idąca bezpośrednio (o ile taka istnieje) do wierzchołka $j$ z tą, która przechodzi przez wierzchołek $k$. Jeżeli ta druga jest krótsza, do tablicy na pozycji $d_{i,j}$ (`d[source][target]`) wpisywana jest suma wag ścieżek $(i, k)$ i $(k, j)$.

## Złożoność

Na czas działania algorytmu najbardziej wpływa potórjnie zagnieżdżona pętla `for`. Kod wewnątrz najbardziej zagnieżdzonej pętli:

```Python
new_weight = d[source][middle] + d[middle][target]

if target is source and new_weight < 0:
    raise ValueError('Wykryto cykl ujemny: {}~>{}~>{}'.format(
        target, middle, source))

if d[source][target] > new_weight:
    d[source][target] = new_weight
```

jest $\mathcal{O}(1)$. Każda pętla `for` jest $\mathcal{O}(|V|)$. Cała zagnieżdżona struktura pętl jest $\mathcal{O}(|V|^3)$, i jest to najbardziej złożona czasowo część algorytmu, więc cały algorytm też jest $\mathcal{O}(|V|^3)$.

## Spis funkcji

## Licencja

W programie używane są dane ze zbioru danych [CITIES](https://people.sc.fsu.edu/~jburkardt/datasets/cities/cities.html) udostępnianych na licencji [GNU LGPL](https://people.sc.fsu.edu/~jburkardt/txt/gnu_lgpl.txt).
