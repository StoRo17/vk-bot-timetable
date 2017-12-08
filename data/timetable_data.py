import json
from collections import OrderedDict


def load_timetable():
    return json.loads(open('bot/data/timetable.json', encoding='utf8').read(), object_pairs_hook=OrderedDict)


def load_subjects_time():
    return json.loads(open('bot/data/subjects_time.json', encoding='utf8').read(), object_pairs_hook=OrderedDict)
