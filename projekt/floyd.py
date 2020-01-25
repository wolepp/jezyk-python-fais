"""
Algorytm Floyda-Warshalla.

Wojciech Lepich
"""
from math import inf
import graphutil


def floydwarshall(graph):
    """
    Algorytm Floyda-Warshalla, zwraca macierz kosztów dojścia.

    Przyjmuje graf typu dict+dict.
    """
    nodes = graphutil.list_nodes(graph)
    edges = graphutil.list_edges(graph)

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
    graphutil.print_graph(shortest_path)
