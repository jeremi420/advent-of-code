import argparse
from day4.game import Game
from day4.exercise1 import exercise1
from day4.exercise2 import exercise2

def parse_file(filename: str):
    with open(filename) as file:
        lines = file.readlines()
    return list(map(Game.deserialize, lines))

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-e', '--exercise', default=1, choices=[1,2], type=int)

def main():
    args = parser.parse_args()
    games = parse_file(args.filename)
    if(args.exercise == 1):
        exercise1(games)
    else:
        exercise2(games)

if __name__ == "__main__":
    main()
