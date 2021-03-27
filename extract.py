"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
import models

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path="./data/neos.csv"):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = {}
    nm_lines = 0
    with open(neo_csv_path) as csv_file:
        reader=csv.reader(csv_file)
        for line in reader:
            if nm_lines == 0:
                print(f'columns: {line[3]} , {line[4]} , {line[15]} , {line[7]} ')
            else:
                print(f"data:{line[3]},{line[4]},{line[15]},{line[7]}")
                neos[line[3]]=models.NearEarthObject(line[3],line[4],line[15],line[7])
            nm_lines += 1
            #if nm_lines > 1005:
            #    break
    # TODO: Load NEO data from the given CSV file.
    #Constructor:(self, designation, name=None, diameter=float('nan'), hazardous=False)
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    return ()

if __name__ == "__main__":
    neos=load_neos()

    for item in neos.values():
        print(item)
    print(neos["2010 CJ188"])

    print(len(neos.values()))
