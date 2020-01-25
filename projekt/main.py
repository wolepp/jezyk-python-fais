"""
Główny program projektu.

W tym module obliczane są najkrótsze ścieżki pomiędzy wszystkimi parami
miast z danych.
"""

import os
import parser
import floyd

if __name__ == "__main__":

    dirname = os.path.dirname(__file__)
    cities_filename = os.path.join(dirname, 'data', 'sgb128_name.txt')
    distances_filename = os.path.join(dirname, 'data', 'sgb128_dist.txt')

    oryg_graf = os.path.join(dirname, 'input.txt')
    nowy_graf = os.path.join(dirname, 'output.txt')

    graph = parser.parse(cities_filename, distances_filename)
    with open(oryg_graf, 'w') as file:
        file.write(str(graph))

    shortest_distances = floyd.floydwarshall(graph)
    with open(nowy_graf, 'w') as file:
        file.write(str(shortest_distances))
