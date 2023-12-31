from .engine_schematic import EngineSchematic

def exercise2(lines: list[str]):
    engine_schematic = EngineSchematic(lines)
    print(engine_schematic.find_sum_of_all_gear_ratios())
