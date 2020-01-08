"""
Moduł zawierający funkcje pomagające budować właściwy graf.

Graf typu dict+dict
"""


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
    if source == target:
        raise ValueError("pętle są zabronione")
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
