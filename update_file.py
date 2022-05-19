import os
import json
import sys

json_data={}

version = os.getenv("VERSION")
file = os.getenv("FILE")
data = os.getenv("DATA")

with open(file) as json_file:
    json_data = json.load(json_file)

if data is not None:
    new_data = json.loads(data)
    new_data["version"] = version
    for note in json_data['releaseNotes']:
        if note["version"] == version:
            print(f"Existing release note for version {version}. Aborting")
            sys.exit(1)
    json_data['releaseNotes'].append(new_data)
else:
    json_data["version"] = version

with open(os.getenv("FILE"), "w") as updated_json_file: 
    json.dump(json_data, updated_json_file, indent=2)