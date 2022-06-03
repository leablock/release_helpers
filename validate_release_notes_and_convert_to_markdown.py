import json
import os

data = os.getenv("DATA")
read_only = os.getenv("READ_ONLY")

notes = "# Notes\n"
new_data = json.loads(data)

sections = data["sections"]
assert type(sections) == list

for section in sections:
    assert type(section["title"]) == str
    assert type(section["notes"]) == list
    notes += f'\n## {section["title"]}\n'
    for note in section["notes"]:
        assert section["type"] == str
        assert section["message"] == str
        notes += f'- {section["message"]}\n'
        
notes += "\n"

if not read_only:
    with open("notes.md", "w") as md:
        md.write(notes)