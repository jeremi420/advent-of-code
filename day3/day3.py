from day3.parse import parse_args
from day3.exercise1 import exercise1
from day3.exercise2 import exercise2


def main():
    args = parse_args()
    with open(args.filename) as file:
        lines = file.readlines()
    if (args.exercise == 1):
        exercise1(lines)
    else:
        exercise2(lines)

if __name__ == "__main__":
    main()
