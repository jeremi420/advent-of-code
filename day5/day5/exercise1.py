import sys
from collections import namedtuple

Range = namedtuple('Range', ['destination_start', 'source_start', 'length'])


def parse_map(ranges: list[str]):
    mapping: list[Range] = []
    for r in ranges:
        destination_start, source_start, length = list(map(int, r.split(' ')))
        mapping.append(Range(destination_start, source_start, length))
    return mapping

def parse_seeds(header: str):
    seeds_segment = header.split(': ')[1]
    return list(map(int, seeds_segment.split(' ')))

def get_destination_value(mapping: list[Range], source_value: int):
    for m in mapping:
        if source_value >= m.source_start and source_value < m.source_start + m.length:
            difference = source_value - m.source_start
            return m.destination_start + difference
    return source_value

def exercise1(filename: str):
    with open(filename) as file:
        lines = file.readlines()
    initial_seeds = parse_seeds(lines[0])
    ranges: list[list[str]] = []
    r: list[str] = []
    for line in lines[2:]:
        if line[0].isalpha():
            continue
        elif line == "\n":
            ranges.append(r)
            r = []
        else:
            r.append(line[:-1])
    ranges.append(r)
    mappings = list(map(parse_map, ranges))
    min = sys.maxsize
    for seed in initial_seeds:
        value = seed
        for mapping in mappings:
            value = get_destination_value(mapping, value) 
        if value < min:
            min = value
    print(min)
