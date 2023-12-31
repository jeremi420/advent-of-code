dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def main():
    with open('input.txt') as file:
        lines = file.readlines()
    sum = 0
    digits = []
    for line in lines:
        for i, char in enumerate(line):
            if char.isdigit():
                digits.append(char)
            for key in dict:
                if (line[i:].startswith(key)):
                    digits.append(dict[key])
        sum += int(digits[0] + digits[-1])
        digits = []
    print(sum)


if __name__ == "__main__":
    main()
