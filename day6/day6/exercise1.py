from .utils import Race

def find_number_of_wining_combinations(race: Race):
    for i in range(race.distance // 2):
        result = (race.time - i ) * i
        if(result > race.distance):
            combinations = race.time - (i * 2) + 1
            return combinations
    return 0

def exercise1(races: list[Race]):
    result = 1 
    for race in races:
        combinations = find_number_of_wining_combinations(race)
        result = result * combinations
    print(result)
