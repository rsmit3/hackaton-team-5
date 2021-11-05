import json

def get_data(file_to_read):
    with open(file_to_read) as json_file:
        data = json.load(json_file)
        keysToDelete=[]
    for key,value in data.items():
        if int(key) < int(0.0*len(data)) or int(key) > int(1*len(data)):
            keysToDelete.append(str(key))
    for key in keysToDelete:
        del data[key]
    return data
