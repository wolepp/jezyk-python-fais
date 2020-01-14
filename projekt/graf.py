"""
Algorytm Floyda-Warshalla.

Wojciech Lepich
"""
from math import inf
import graphutil

def floydwarshall(graph):
    nodes = graphutil.list_nodes(graph)
    edges = graphutil.list_edges(graph)

    # ilość wierzchołków
    n = len(nodes)

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
                if d[source][target] > new_weight:
                    d[source][target] = new_weight

    return d

if __name__ == "__main__":

    graph = {
        "A": {"B": 1, "C": 2},
        "B": {"C": 3, "D": 5, "F": 8},
        "C": {"A": 3, "D": 1},
        "D": {"C": 6},
        "E": {"C": 7},
        "F": {"B": 1, "E": 3}
    }

    # d = floydwarshall(graph)
    # graphutil.print_graph(d)

    randomowy = graphutil.random_graph(4, 30)
    floyd = floydwarshall(randomowy)
    graphutil.print_graph(randomowy)
    print()
    graphutil.print_graph(floyd)
    