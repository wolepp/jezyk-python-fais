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
    data_dirname = os.path.join(dirname, 'data')
    cities_filename = os.path.join(data_dirname, 'sgb128_name.txt')
    distances_filename = os.path.join(data_dirname, 'sgb128_dist.txt')

    old_distances = parser.parse(cities_filename, distances_filename)
    new_distances = floyd.floydwarshall(old_distances)

    # szukanie największej bezwzględnej zmiany w odległości
    max_change = 0
    cities = old_distances.keys()
    for cityA in cities:
        for cityB in cities:
            old = old_distances[cityA][cityB]
            new = new_distances[cityA][cityB]
            if old - new > max_change:
                max_change = old - new
                max_cityA, max_cityB = cityA, cityB

    print("Największa zmiana w drodze z {} do {}, zmiana o: {} mil".format(
        max_cityA, max_cityB, max_change))
