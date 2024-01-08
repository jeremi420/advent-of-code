import argparse
from day6.exercise1 import exercise1
from day6.utils import read_one_race, read_races_file

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-e', '--exercise', type=int, choices=[1,2], default=1)


def main():
    args = parser.parse_args()
    if(args.exercise == 1):
        exercise1(read_races_file(args.filename))
    if(args.exercise == 2):
        exercise1(read_one_race(args.filename))

if __name__ == "__main__":
    main()
