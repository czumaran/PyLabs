import json 

def readJsonFile(filename):
    data=""
    try:
        with open('Lab14/insulin.json') as json_file:
            data = json.load(json_file)
    except:
        print("Could not read file")
    return data