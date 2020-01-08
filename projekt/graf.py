"""
Algorytm Floyda-Warshalla.

Wojciech Lepich
"""
import graphutil


graph = {
    "A": {"B": 1, "C": 2},
    "B": {"C": 3, "D": 4},
    "C": {"D": 5},
    "D": {"C": 6},
    "E": {"C": 7},
    "F": {}
}


if __name__ == "__main__":
    graphutil.add_node(graph, "G")
    graphutil.add_edge_directed(graph, ('G', 'C', 9))

    graphutil.print_graph(graph)
    print(graphutil.list_edges(graph))
    print(graphutil.list_nodes(graph))
