import json
from full_record_obj import full_record_obj

with open('full_record_obj.json', 'w') as outfile:
    json.dump(full_record_obj['metadata'], outfile, indent=2)
