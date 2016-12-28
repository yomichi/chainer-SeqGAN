# -*- coding: utf-8 -*-
#

import json
import glob

o = []
files = glob.glob("g*.json")
for fname in files:
    with open(fname, 'r') as f:
        j = json.load(f)
    #
    for x in j:
        if not 'story' in x.keys():
            continue
        #text = m.parse(x['story']).split()
        text = x['story']
        o.append({'summary': text})
            
    #
with open('../dataset/output.json', 'w') as f:
    json.dump(o, f)

