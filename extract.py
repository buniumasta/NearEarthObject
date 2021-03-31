"""
Extract data on near-Earth objects and close approaches from CSV and JSON
files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path="./data/neos.csv"):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth
    objects.
    :return: A collection of `NearEarthObject`s.

    Following paraments are stored in files:
        id,spkid,full_name,pdes,name,prefix,neo,pha,H,G,M1,M2,K1,K2,PC,diameter
    Function loads only following: pdes, name,pha, diameter
    """

    loaded_neos = list()
    nm_lines = 0
    with open(neo_csv_path) as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            if nm_lines == 0:
                try:
                    pdes_i = line.index('pdes')
                    name_i = line.index('name')
                    pha_i = line.index('pha')
                    diameter_i = line.index('diameter')
                except ValueError as error:
                    print(f'Error: No valid indexes found: {error}')
                    return None
            else:
                loaded_neos.append(
                    NearEarthObject(
                        line[pdes_i],
                        line[name_i],
                        line[diameter_i],
                        line[pha_i]))
            nm_lines += 1
    return loaded_neos


def load_approaches(cad_json_path="./data/cad.json"):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close
      approaches.
    :return: A collection of `CloseApproach`es.

    Json file structrtucture:
        fields":["des","orbit_id","jd","cd","dist","dist_min","dist_max",
                 "v_rel","v_inf","t_sigma_f","h"]
            des - primary designation of the asteroid or comet
                  (e.g., 443, 2000 SG344)
            orbit_id - orbit ID
            jd - time of close-approach (JD Ephemeris Time)
            cd - time of close-approach (formatted calendar date/time, in UTC)
            dist - nominal approach distance (au)
            dist_min - minimum (3-sigma) approach distance (au)
            dist_max - maximum (3-sigma) approach distance (au)
            v_rel - velocity relative to the approach body at close
                    approach (km/s)
            v_inf - velocity relative to a massless body (km/s)
            t_sigma_f - 3-sigma uncertainty in the time of close-approach
                        (formatted in days, hours, and minutes; days are not
                        included if zero; example "13:02" is 13 hours 2 minutes
                        example "2_09:08" is 2 days 9 hours 8 minutes)
            h - absolute magnitude H (mag)
    Function loads only following :
        des,cd,dist,v_rel
    """

    loaded_approaches = list()

    with open(cad_json_path) as json_file:
        data = json.load(json_file)

    fields = data['fields']
    try:
        des_index = fields.index('des')
        cd_index = fields.index('cd')
        dist_index = fields.index('dist')
        v_rel_index = fields.index('v_rel')
    except ValueError as error:
        print(f'Error: No valid indexes found: {error}')
        return None
    else:
        list_approaches = data['data']
        for record in list_approaches:
            loaded_approaches.append(
                                CloseApproach(
                                    record[des_index],
                                    record[cd_index],
                                    record[dist_index],
                                    record[v_rel_index]))

    return loaded_approaches
