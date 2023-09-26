from pathlib import Path
import json


# load data from json file
THIS_DIR = Path(__file__).parent
json_f   = THIS_DIR/'my_store_d.json'

s = open(json_f).read()
print(s)
print(type(s))

print('\n---\n')

d = json.loads(s)
print(d)
print(type(d))
