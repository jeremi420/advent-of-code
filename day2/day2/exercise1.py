import re

red_max = 12
green_max = 13
blue_max = 14


def exercise1(filename: str):
    with open(filename) as file:
        lines = file.readlines()
    sum = 0
    for line in lines:
        gamesText = line.split(': ')[1]
        id = int(re.search(r'Game\ (\d+)', line).group(1))
        possible = True
        for game in gamesText.split(';'):
            match = re.search(r'(\d*)\ blue')
            blue = 0 if match is None else int(match.group(1))
            match = re.search(r'(\d*)\ red')
            red = 0 if match is None else int(match.group(1))
            match = re.search(r'(\d*)\ green')
            green = 0 if match is None else int(match.group(1))
            if red > red_max or green > green_max or blue > blue_max:
                possible = False
        if possible:
            sum += id
    print(sum)
