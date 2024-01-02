import argparse
from day5.exercise1 import exercise1

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-e', '--exercise', type=int, choices=[1, 2], default=1)

def main():
    args = parser.parse_args()
    if(args.exercise == 1):
        exercise1(args.filename)

if __name__ == "__main__":
    main()
