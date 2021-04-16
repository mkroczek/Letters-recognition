import json

def export_to_json(network):
    keys = ["Layer " + str(i) + ": " for i in range(len(network))]
    dictionary = dict(zip(keys, network))
    with open('models/teaching_data.json', 'w') as json_file:
        json.dump(dictionary, json_file)


def import_from_json():
    with open('models/teaching_data_last.json') as json_file:
        dict = json.load(json_file)
    return list(dict.values())
