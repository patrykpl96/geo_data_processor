import csv

def load_locations(file_path):

    dane = []

    with open(file_path, mode = "r", encoding = "utf-8") as plik:

        czytnik = csv.DictReader(plik)

        for element in czytnik:
            dane.append(element)

    return dane

