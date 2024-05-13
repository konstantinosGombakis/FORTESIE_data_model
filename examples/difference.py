import json

def load_json_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_key_difference(json1, json2):
    keys1 = set(json1.keys())
    keys2 = set(json2.keys())
    
    difference_in_1 = keys1 - keys2
    difference_in_2 = keys2 - keys1
    
    return difference_in_1, difference_in_2

# Load JSON from files
file_path1 = 'file1.json'
file_path2 = 'file2.json'

json1 = load_json_from_file('example-normalized.jsonld')
json2 = load_json_from_file('test1.json')

# Get the difference in keys
diff1, diff2 = get_key_difference(json1, json2)
print("Keys in json1 but not in json2:", diff1)
print("Keys in json2 but not in json1:", diff2)
