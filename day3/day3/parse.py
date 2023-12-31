import argparse
from dataclasses import dataclass
from typing import Literal

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-e', '--exercise', type=int, choices=[1, 2], default=1)


@dataclass
class Args:
    filename: str
    exercise: Literal[1, 2]

    def __init__(self, fn: str, e: Literal[1, 2]):
        self.exercise = e
        self.filename = fn


def parse_args():
    args = parser.parse_args()
    return Args(args.filename, args.exercise)
