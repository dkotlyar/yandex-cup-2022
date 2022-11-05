import json
from copy import copy
from itertools import chain

with open('input.txt', 'r') as f:
    input_txt = f.readlines()
    n, m = map(int, input_txt[0].strip().split())
    subscribers = map(lambda s: s.strip().split(), input_txt[1:n + 1])
    subscribers = [
        dict(
            triggers=s[2:int(s[0]) + 2],
            shipments=s[int(s[0]) + 2:int(s[0]) + int(s[1]) + 2],
        )
        for s in subscribers
    ]
    requests = list(map(lambda s: json.loads(s.strip()), input_txt[n + 1:]))[:m]


offers = []

fields = [
    'price',
    'stock_count',
    'partner_content.title',
    'partner_content.description',
]


def update_field(field, offer, req):
    if '.' in field:
        _fields = field.split('.')
        parent = _fields[0]
        nested = _fields[1:]
        if parent in req:
            if parent not in offer:
                offer[parent] = dict()
            trigger = update_field('.'.join(nested), offer[parent], req[parent])
            if trigger:
                return [parent] + [
                    f'{parent}.{t}'
                    for t in trigger
                ]
    elif field in req:
        if field not in offer or offer[field] != req[field]:
            offer[field] = req[field]
            return [field]


def insert_field(field, data, offer):
    if '.' in field:
        _fields = field.split('.')
        parent = _fields[0]
        nested = _fields[1:]
        if parent in offer:
            if parent not in data:
                data[parent] = dict()
            insert_field('.'.join(nested), data[parent], offer[parent])
    elif field in offer:
        data[field] = offer[field]


def build_data(s, offer):
    data = dict(id=offer['id'])
    for f in chain(s['triggers'], s['shipments']):
        insert_field(f, data, offer)
    return data


for req in requests:
    _req_offer = req['offer']
    offer = [o for o in offers if o['id'] == _req_offer['id']]
    if offer:
        offer = offer[0]
    else:
        offer = dict(id=_req_offer['id'])
        offers.append(offer)

    subscribers_candidates = list(enumerate(subscribers))
    subscribers_for_req = []

    for f in fields:
        triggers = update_field(f, offer, _req_offer)
        if triggers:
            subscribers_for_trigger = [
                (i, s)
                for i, s in subscribers_candidates
                if any(trig in triggers for trig in s['triggers'])
            ]
            subscribers_for_req += subscribers_for_trigger
            for s in subscribers_for_trigger:
                subscribers_candidates.remove(s)

    # print(req)
    subscribers_for_req.sort(key=lambda s: s[0])
    # print(subscribers_for_req)

    for i, s in subscribers_for_req:
        data = build_data(s, offer)
        trace = dict(
            trace_id=req['trace_id'],
            offer=data
        )
        print(json.dumps(trace))

    # print()