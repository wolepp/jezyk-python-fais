"""Moduł zawiera funkcję do przetwarzania plików z danymi dotyczącymi
odległości między miastami na graf ważony skierowany.
"""

import re
import graphutil as gu


def parse(cities_filename, distances_filename):
    """Przetwarza dane z pliku na graf skierowany.

    Przyjmuje nazwy dwóch plików, jeden z nazwami miast, drugi z odległościami
    pomiędzy miastami.
    """
    pattern = re.compile(r'\w*, [A-Z][A-Z]')
    with open(cities_filename, 'r') as file:
        data = file.read()
    cities = pattern.findall(data)

    with open(distances_filename, 'r') as file:
        data = file.read()
    # rozdzielenie na linie i usunięcie zbędnych
    data = data.splitlines()[7:]

    graph = {}
    for i, city in enumerate(cities):
        distances = [int(distance) for distance in data[i].split()]
        gu.add_node(graph, city)
        for j, distance in enumerate(distances):
            target_city = cities[j]
            gu.add_edge_directed(graph, (city, target_city, distance))

    return graph
