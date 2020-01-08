"""
Algorytm Floyda-Warshalla.

Wojciech Lepich
"""
import graphutil

def floydwarshall(graph):
    n = len(graphutil.list_nodes(graph))

if __name__ == "__main__":

    graph = {
        "A": {"B": 1, "C": 2},
        "B": {"C": 3, "D": 4},
        "C": {"D": 5},
        "D": {"C": 6},
        "E": {"C": 7},
        "F": {}
    }

    graphutil.add_node(graph, "G")
    graphutil.add_edge_directed(graph, ('G', 'C', 9))

    graphutil.print_graph(graph)
    print(graphutil.list_edges(graph))
    print(graphutil.list_nodes(graph))
    print('wierzchołków:', len(graphutil.list_nodes(graph)))
