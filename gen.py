from os import listdir, remove
from os.path import isfile, isdir, join
import json

vocabs = listdir('vocabs')
metas = {}
for vocab in vocabs:
    # check json format
    try:
        with open(join('vocabs', vocab)) as data_file:
            data = json.load(data_file)
            metas[vocab] = {
                'depends': data['depends'],
                'langs': data['langs'],
            }
    except:
        print 'errornous', vocab

with open(join('meta', 'vocabs.json'), 'w') as f:
    json.dump(metas, f)
