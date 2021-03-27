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
    # TODO: Load NEO data from the given CSV file.
    """
    id,spkid,full_name,pdes,name,prefix,neo,pha,H,G,M1,M2,K1,K2,PC,diameter
    Interested in: pdes, name,pha, diameter
    """
    neos = {}
    nm_lines = 0
    with open(neo_csv_path) as csv_file:
        reader=csv.reader(csv_file)
        for line in reader:
            if nm_lines == 0:
                try:
                    pdes_i=line.index('pdes')
                    name_i=line.index('name')
                    pha_i=line.index('pha')
                    diameter_i=line.index('diameter')
                except ValueError as error:
                    print(f'Error: No valid indexes found: {error}')
                    return {}
            else:
                #print(f"data:{line[3]},{line[4]},{line[15]},{line[7]}")
                neos[line[pdes_i]]=models.NearEarthObject(line[pdes_i],line[name_i],line[diameter_i],line[pha_i])
            nm_lines += 1
            #if nm_lines > 1005:
            #    break
    return neos


def load_approaches(cad_json_path="./data/cad.json"):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """

    """
    "count":"406785","fields":["des","orbit_id","jd","cd","dist","dist_min","dist_max","v_rel","v_inf","t_sigma_f","h"]
    des - primary designation of the asteroid or comet (e.g., 443, 2000 SG344)
    orbit_id - orbit ID
    jd - time of close-approach (JD Ephemeris Time)
    cd - time of close-approach (formatted calendar date/time, in UTC)
    dist - nominal approach distance (au)
    dist_min - minimum (3-sigma) approach distance (au)
    dist_max - maximum (3-sigma) approach distance (au)
    v_rel - velocity relative to the approach body at close approach (km/s)
    v_inf - velocity relative to a massless body (km/s)
    t_sigma_f - 3-sigma uncertainty in the time of close-approach (formatted in days, hours, and minutes; days are not included if zero; example "13:02" is 13 hours 2 minutes; example "2_09:08" is 2 days 9 hours 8 minutes)
    h - absolute magnitude H (mag)
    following fields will be taken into the account:
        des,cd,dist,v_rel
    """
    # TODO: Load close approach data from the given JSON file.
    return_approaches={}
    #print('Loadding data:')
    with open(cad_json_path) as json_file:
        data=json.load(json_file)

    #print('Printing read keys in loaded collection:')
    for item in data.keys():
        type_of_item=type(data[item])
        #print(f' {item}:{type_of_item}')

    fields=data['fields']
    try:
        des_index=fields.index('des')
        cd_index=fields.index('cd')
        dist_index=fields.index('dist')
        v_rel_index=fields.index('v_rel')
    except ValueError as error:
        #print(f'Error: No valid indexes found: {error}')
        return {}
    else:
        #print(f'des_index:{des_index}, cd_index:{cd_index}, dist_index:{dist_index}, v_rel_index:{v_rel_index}')
        list_approaches=data['data']
        nb_lines=0
        for record in list_approaches:
            #_(self, time=None, distance=0.0, velocity=0.0):
            current_des=record[des_index]
            #print(current_des)
            if current_des in return_approaches.keys():
                current_approach=CloseApproach(record[cd_index],record[dist_index],record[v_rel_index])
                #print(current_approach)
                return_approaches[current_des].append(current_approach)
            else:
                my_list=list()
                current_approach=CloseApproach(record[cd_index],record[dist_index],record[v_rel_index])
                #print(current_approach)
                my_list.append(current_approach)
                return_approaches[current_des]=my_list

            #if nb_lines > 1000:
            #    break
            nb_lines+=1

    return return_approaches

if __name__ == "__main__":
    neos=load_neos()

    for item in neos.values():
        print(item)
    print(neos["2010 CJ188"])
    print(len(neos.values()))

    approaches=load_approaches()

    for key,value in approaches.items():
        print(f'{key}: {value}')
