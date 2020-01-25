"""
Moduł zawierający funkcje pomagające budować właściwy graf.

Graf typu dict+dict
"""

from random import randrange


def add_node(graph, node):
    """Wstawia wierzchołek do grafu."""
    if node not in graph:
        graph[node] = {}


def add_edge_directed(graph, edge):
    """Dodaje krawędź do grafu skierowanego."""
    source, target, weight = edge
    add_node(graph, source)
    add_node(graph, target)
    # Możemy wykluczyć pętle.
    # if source == target:
    #     raise ValueError("pętle są zabronione")
    if target not in graph[source]:
        graph[source][target] = weight


def list_nodes(graph):
    """Zwraca listę wierzchołków grafu."""
    return graph.keys()


def list_edges(graph):
    """Zwraca listę krawędzi (3-krotek) grafu skierowanego ważonego."""
    L = []
    for source in graph:
        for target in graph[source]:
            L.append((source, target, graph[source][target]))
    return L


def print_graph(graph):
    """Wypisuje postać grafu skierowanego ważonego na ekranie."""
    for source in graph:
        print(source, ": ", end="")
        for target in graph[source]:
            print("{}({})".format(target, graph[source][target]), end=" ")
        print()  # nowa linia


def random_graph(size, max_weight=10, keys=None):
    """Tworzy losowy graf o alfabetycznych etykietach.

    Parametr size oznacza ilość wierzchołków.
    Parametr max_weight (opcjonalny) oznacza największą możliwą wagę krawędzi.
    Parametr keys (opcjonalny) to własne etykiety wierzchołków.
    """
    if keys is None:
        if size <= 26:
            keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        else:
            keys = list(range(1, size+1))

    if len(keys) < size:
        raise ValueError('Zbyt mała ilość etykiet')
    keys = keys[:size]

    graph = {}
    for source in keys:
        graph[source] = {}
        for i in range(size):
            target = keys[randrange(size)]
            # wykluczone krawędzie do źródłowego węzła
            if target == source:
                continue
            weight = randrange(1, max_weight)
            graph[source][target] = weight

    return graph
