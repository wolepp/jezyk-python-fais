"""Parser tworzący graf z danych."""

import re
import graphutil

def parse(cities_filename, distance_filename):
    # 'Youngstown, OH'; 'Tyler, TX'; 'Tulsa, OK'
    pattern_city = re.compile(r'\w*, [A-Z][A-Z]')
    with open(cities_filename, 'r') as file:
        data = file.read()
    cities = pattern_city.findall(data)

    N = len(cities)
    with open(distance_filename, 'r') as file:
        data = file.read()
        data = data.splitlines()[7:]
    
    # for indeks, miasto in enumerate(cities):
    #     pass


if __name__ == "__main__":
    import os
    dirname = os.path.dirname(__file__)
    miasta = os.path.join(dirname, 'data', 'sgb128_name.txt')
    odlegl = os.path.join(dirname, 'data', 'sgb128_dist.txt')
    parse(miasta, odlegl)
