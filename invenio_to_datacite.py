import sys
import json

from jsonbender import bend, K, S
from jsonbender.list_ops import ForallBend



MAPPING = {
    # optional because it's not mandatory
    'subjects': S('subjects').optional() >> ForallBend({
        'subject': S('subject'),
        'subjectScheme': S('scheme'), # not present in https://support.datacite.org/docs/schema-optional-properties-v43
        'schemeURI': S('uri').optional(),
        'lang': S('lang').optional(), # not present in https://support.datacite.org/docs/schema-optional-properties-v43
        'valueURI': S('value').optional(),
    })
}
_MAPPING = {
    'subjects': S('subjects').optional()
}



if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname) as jsonf:
        j = json.load(jsonf)
        result = bend(MAPPING, j["metadata"])
        print(json.dumps(result))
