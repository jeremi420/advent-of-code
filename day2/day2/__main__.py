import argparse
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
        print(f' game id is: {id}')
        for game in gamesText.split(';'):
            match = re.search(r'(\d*)\ blue', game)
            blue = 0 if match is None else int(match.group(1))
            match = re.search(r'(\d*)\ red', game)
            red = 0 if match is None else int(match.group(1))
            match = re.search(r'(\d*)\ green', game)
            green = 0 if match is None else int(match.group(1))
            print(f'red: {red}, green: {green}, blue: {blue}')
            if red > red_max or green > green_max or blue > blue_max:
                possible = False
        if possible:
            sum += id
    print(sum)


def exercise2(filename: str):
    with open(filename) as file:
        lines = file.readlines()
    sum = 0
    for line in lines:
        red_max = 0
        green_max = 0
        blue_max = 0
        for game in line.split(': ')[1].split(';'):
            match = re.search(r'(\d*)\ blue', game)
            blue = 0 if match is None else int(match.group(1))
            match = re.search(r'(\d*)\ red', game)
            red = 0 if match is None else int(match.group(1))
            match = re.search(r'(\d*)\ green', game)
            green = 0 if match is None else int(match.group(1))
            if green > green_max:
                green_max = green
            if red > red_max:
                red_max = red
            if blue > blue_max:
                blue_max = blue
        sum += red_max * green_max * blue_max
    print(sum)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)
    parser.add_argument('-e', '--exercise',
                        choices=[1, 2], default=1, type=int)
    args = parser.parse_args()
    if (args.exercise == 1):
        exercise1(args.filename)
    if (args.exercise == 2):
        exercise2(args.filename)


if __name__ == "__main__":
    main()
