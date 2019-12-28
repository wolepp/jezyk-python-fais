"""
Zadanie 11.4 - porównanie czasów działania algorytmów sortowania.

Ze względu na ilość czasu potrzebnego na posortowanie algorytmami
klasy O(N^2) - te uruchamiane są dla N <= 10**4. Tylko dla insertsort
uruchomiłem N = 10**5. Czas sortowania wyniósł 602 sekundy.
"""
import timeit
import matplotlib.pyplot as plt
from operator import itemgetter
from math import log10
import sort_test_data as lists
import sort


def print_results(wyniki, key=None):
    if key is None:
        key = itemgetter('N', 'time')
    wyniki.sort(key=key)

    longest_alg_name = max((w.get('name') for w in wyniki), key=len)
    name_width = 1 + len(longest_alg_name)
    n_width = 5
    time_width = 9

    header = "{word: >{width}}|".format(word='algorytm', width=name_width)
    header += "{word: >{width}}|".format(word='N', width=n_width)
    header += "{word: >{width}}".format(word='sekund', width=time_width)
    print(header)
    print('|'.join(['-'*name_width, '-'*n_width, '-'*time_width]))

    for wynik in wyniki:
        nazwa = wynik.get('name')
        count = "10^{:n}".format(log10(wynik.get('N')))
        time = "{:.{prec}f}".format(wynik.get('time'), prec=time_width-4)

        row = "{name: >{width}}|".format(name=nazwa, width=name_width)
        row += "{count: >{width}}|".format(count=count, width=n_width)
        row += "{time: >{width}}".format(time=time, width=time_width)
        print(row)


if __name__ == "__main__":
    lista = lists.random_integer_list
    wyniki = []

    # Quicksort, Mergesort i Timsort
    for N in [10**2, 10**3, 10**4, 10**5, 10**6]:
        ilosc_probek = 1
        czas_mergesort = timeit.timeit(lambda: sort.mergesort(lista(N), 0, N-1),
                                       number=ilosc_probek) / ilosc_probek
        czas_quicksort = timeit.timeit(lambda: sort.quicksort(lista(N), 0, N-1),
                                       number=ilosc_probek) / ilosc_probek
        czas_timsort = timeit.timeit(lambda: lista(N).sort(),
                                     number=ilosc_probek) / ilosc_probek
        wyniki.append({
            "name": "quicksort",
            "N": N,
            "time": czas_quicksort
        })
        wyniki.append({"name": "mergesort", "N": N, "time": czas_mergesort})
        wyniki.append({"name": "timsort", "N": N, "time": czas_timsort})

    # Selectsort, Insertsort, Bubblesort, Shakersort i Shellsort
    for N in [10**2, 10**3, 10**4]:
        ilosc_probek = 1

        czas_selectsort = timeit.timeit(lambda: sort.selectsort(lista(N), 0, N-1),
                                        number=ilosc_probek) / ilosc_probek
        czas_insertsort = timeit.timeit(lambda: sort.insertsort(lista(N), 0, N-1),
                                        number=ilosc_probek) / ilosc_probek
        czas_bubblesort = timeit.timeit(lambda: sort.bubblesort(lista(N), 0, N-1),
                                        number=ilosc_probek) / ilosc_probek
        czas_shakersort = timeit.timeit(lambda: sort.shakersort(lista(N), 0, N-1),
                                        number=ilosc_probek) / ilosc_probek
        czas_shellsort = timeit.timeit(lambda: sort.shellsort(lista(N), 0, N-1),
                                       number=ilosc_probek) / ilosc_probek

        wyniki.append({"name": "selectsort", "N": N, "time": czas_selectsort})
        wyniki.append({"name": "insertsort", "N": N, "time": czas_insertsort})
        wyniki.append({"name": "bubblesort", "N": N, "time": czas_bubblesort})
        wyniki.append({"name": "shakersort", "N": N, "time": czas_shakersort})
        wyniki.append({"name": "shellsort", "N": N, "time": czas_shellsort})

    #      Insertsort dla N=10**5
    # czas_insertsort_duzeN = timeit.timeit(
    #     lambda: sort.insertsort(lista(10**5), 0, 10**5-1), number=1)
    # wyniki.append({
    #     "name": "insertsort",
    #     "N": 10**5,
    #     "time": czas_insertsort_duzeN
    #     })

    print_results(wyniki)
