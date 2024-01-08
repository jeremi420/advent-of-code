
from collections import namedtuple

Race = namedtuple('Race', ['time', 'distance'])

def read_races_file(filename: str):
    with open(filename) as file:
        lines = file.readlines()
    lines = map(lambda x: x.split(':')[1].strip(), lines)
    lines = map(lambda x: map(int, filter(None, x.split(' '))), lines)
    return list(map(lambda x: Race(*x), zip(*lines)))

def read_one_race(filename: str):
    with open(filename) as file:
        lines = file.readlines()
    lines = map(lambda x: x.split(':')[1].strip(), lines)
    lines = map(lambda x: int(x.replace(' ', '')), lines)
    return [Race(*lines)]
