import json


def test_get_full_record(full_record):
    fname = 'tests/data/full_record.json'
    with open(fname, 'w') as outfile:
        json.dump(full_record, outfile, indent=2)
