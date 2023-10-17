import json

input_file = input("Enter the path and name of the input JSON file: ")
output_file = input("Enter the path and name of the output JSON file: ")

with open(input_file, 'r') as json_file:
    json_data = json.load(json_file)
    for tag in json_data['tags']:
        json_data['tags'].sort(key=lambda x: x['name'])
    for path, methods in json_data["paths"].items():
        for method in ["put", "get", "delete", "post", "patch"]:
            if method in methods and "Supported API" in methods[method].get("tags", []):
                methods[method]["tags"].remove("Supported API")

with open(output_file, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)