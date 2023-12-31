
from .engine_schematic import EngineSchematic

def exercise1(lines: list[str]):
    engine_schenmtic = EngineSchematic(lines) 
    print(sum(engine_schenmtic.find_all_part_numbers()))

