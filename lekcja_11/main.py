"""
Zadanie 11.4 - porównanie czasów działania algorytmów sortowania.

Uwaga - uruchomienie przy ilości próbek>=3 może trwać kilka minut.

Ze względu na ilość czasu potrzebnego na posortowanie algorytmami
klasy O(N^2) - te uruchamiane są dla N <= 10**4. Tylko dla insertsort
uruchomiłem N = 10**5. Czas sortowania wyniósł 602 sekundy.
"""
import timeit
from operator import itemgetter
from itertools import groupby
from math import log10
import matplotlib.pyplot as plt
import sort_test_data as lists
import sort


def print_results(wyniki, key=None):
    """Funkcja do wypisania wyników na ekran terminala."""
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


def plot(wyniki):
    """Funkcja do wyrysowania wykresów z użyciem Matplotlib."""
    wyniki.sort(key=itemgetter('N', 'time'))

    for group_key, group in groupby(wyniki, itemgetter('N')):
        potega = log10(group_key)
        plt.xticks(rotation=45)
        plt.ylabel('sekundy')
        plt.title("N = 10^{:n}".format(potega))
        for result in group:
            plt.bar(result.get('name'), result.get('time'))

        plt.show()  # wyświetlenie wykresu
        # zapisanie do pliku png, np. N_1E4 dla N = 10^4
        # filename = "N_1E{:n}.png".format(potega)
        # plt.savefig(filename)


if __name__ == "__main__":
    lista = lists.random_integer_list
    wyniki = []
    ILOSC_PROBEK = 3

    # Quicksort, Mergesort i Timsort
    for N in [10**2, 10**3, 10**4, 10**5, 10**6]:
        czas_mergesort = timeit.timeit(lambda: sort.mergesort(lista(N), 0, N-1),
                                       number=ILOSC_PROBEK) / ILOSC_PROBEK
        czas_quicksort = timeit.timeit(lambda: sort.quicksort(lista(N), 0, N-1),
                                       number=ILOSC_PROBEK) / ILOSC_PROBEK
        czas_timsort = timeit.timeit(lambda: lista(N).sort(),
                                     number=ILOSC_PROBEK) / ILOSC_PROBEK
        wyniki.append({
            "name": "quicksort",
            "N": N,
            "time": czas_quicksort
        })
        wyniki.append({"name": "mergesort", "N": N, "time": czas_mergesort})
        wyniki.append({"name": "timsort", "N": N, "time": czas_timsort})

    # Selectsort, Insertsort, Bubblesort, Shakersort i Shellsort
    for N in [10**2, 10**3, 10**4]:
        czas_selectsort = timeit.timeit(lambda: sort.selectsort(lista(N), 0, N-1),
                                        number=ILOSC_PROBEK) / ILOSC_PROBEK
        czas_insertsort = timeit.timeit(lambda: sort.insertsort(lista(N), 0, N-1),
                                        number=ILOSC_PROBEK) / ILOSC_PROBEK
        czas_bubblesort = timeit.timeit(lambda: sort.bubblesort(lista(N), 0, N-1),
                                        number=ILOSC_PROBEK) / ILOSC_PROBEK
        czas_shakersort = timeit.timeit(lambda: sort.shakersort(lista(N), 0, N-1),
                                        number=ILOSC_PROBEK) / ILOSC_PROBEK
        czas_shellsort = timeit.timeit(lambda: sort.shellsort(lista(N), 0, N-1),
                                       number=ILOSC_PROBEK) / ILOSC_PROBEK

        wyniki.append({"name": "selectsort", "N": N, "time": czas_selectsort})
        wyniki.append({"name": "insertsort", "N": N, "time": czas_insertsort})
        wyniki.append({"name": "bubblesort", "N": N, "time": czas_bubblesort})
        wyniki.append({"name": "shakersort", "N": N, "time": czas_shakersort})
        wyniki.append({"name": "shellsort", "N": N, "time": czas_shellsort})

    print_results(wyniki)

    # można też wyrysować wykresy przy użyciu Matplotlib
    # plot(wyniki)
