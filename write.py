"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json

#def writeCSV(filename, data):
#    with open(filename, 'w', newline='') as csvfile:
#        fieldnames = data[0].keys()
#        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#        writer.writeheader()
#        for row in data:
#            writer.writerow(row)

# below method will try utilitize serilization
def write_to_csv1(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """

    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')

    with open(filename, 'w', newline='') as csv_fl:
        #fieldnames1 = results[0].keys()
        writer = csv.DictWriter(csv_fl, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """

    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')

    with open(filename, 'w', newline='') as csv_fl:
        csv_writer=csv.writer(csv_fl)
        csv_writer.writerow(fieldnames)
        for result in results:
            if result.neo.name == None:
                f_name=''
            else:
                f_name=result.neo.name
            #row=f'row:datetime:{result.time_str},distance_au:{result.distance}, velocity_km_s:{result.velocity}, designation:{result.designation}, name:{f_name}, diameter_km{result.neo.diameter}, hazardous:{result.neo.hazardous}'
            #print(row)
            row_to_file=(result.time_str,str(result.distance),str(result.velocity),result.designation,f_name,str(result.neo.diameter),str(result.neo.hazardous))
            #print(row_to_file)
            csv_writer.writerow(row_to_file)

def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    #fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')

    lista=[]
    for result in results:
        #print(result.serialize())
        lista.append(result.serialize())

    print(lista)

    with open(filename,'w') as json_fl:
        #
        json.dump([lista], json_fl, indent=4)

if __name__ == '__main__':
    pass
    ##write_to_csv()
