"""
Algorytm Floyda-Warshalla.

Wojciech Lepich
"""
from math import inf
import graphutil as gu


def floydwarshall(graph):
    """
    Algorytm Floyda-Warshalla, zwraca macierz kosztów dojścia.

    Przyjmuje graf typu dict+dict.
    """
    nodes = gu.list_nodes(graph)
    edges = gu.list_edges(graph)

    # macierz d[n*n], każda wartość zainicjalizowana wartością nieskończoność
    # w postaci słownika
    d = {}
    for source in nodes:
        d[source] = {}
        for target in nodes:
            d[source][target] = inf if source != target else 0

    # uzupełnienie wag przejścia między wierzchołkami o krawędzie
    for edge in edges:
        source, target, weight = edge
        d[source][target] = weight

    for middle in nodes:
        for source in nodes:
            for target in nodes:
                new_weight = d[source][middle] + d[middle][target]

                if target is source and new_weight < 0:
                    raise ValueError('Wykryto cykl ujemny: {}~>{}~>{}'.format(
                        target, middle, source))

                if d[source][target] > new_weight:
                    d[source][target] = new_weight

    return d


if __name__ == "__main__":

    graf = {
        "A": {"B": 1, "C": 2},
        "B": {"C": 2, "D": 5, "F": 8},
        "C": {"A": 3, "B": 1, "D": 1},
        "D": {"C": 6},
        "E": {"C": 7},
        "F": {"B": 1, "E": 3}
    }

    shortest_path = floydwarshall(graf)
    assert shortest_path == {
        "A": {"A": 0, "B": 1, "C": 2, "D": 3, "E": 12, "F": 9},
        "B": {"A": 5, "B": 0, "C": 2, "D": 3, "E": 11, "F": 8},
        "C": {"A": 3, "B": 1, "C": 0, "D": 1, "E": 12, "F": 9},
        "D": {"A": 9, "B": 7, "C": 6, "D": 0, "E": 18, "F": 15},
        "E": {"A": 10, "B": 8, "C": 7, "D": 8, "E": 0, "F": 16},
        "F": {"A": 6, "B": 1, "C": 3, "D": 4, "E": 3, "F": 0},
    }
