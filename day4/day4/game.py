
from dataclasses import dataclass
import re

@dataclass
class Game:
    id: int
    winning_numbers: list[int]
    bets: list[int]
    copies: int

    def __init__(self, id: int, winning_numbers: list[int], bets: list[int]) -> None:
        self.id = id 
        self.winning_numbers = winning_numbers
        self.bets = bets
        self.copies = 1

    @staticmethod
    def deserialize(serialized: str):
        id_match = re.search(r'Card\ (\d+)', serialized)
        id = int(id_match.group(1))  if id_match is not None else 0
        winning_numbers_segment = serialized.split(':')[1].split('|')[0]
        bets_segment = serialized.split(':')[1].split('|')[1]
        winning_numbers = list(map(int, filter(None,winning_numbers_segment.split(' '))))
        bets = list(map(int, filter(None, bets_segment.split(' '))))
        return Game(id, winning_numbers, bets)

    def get_match_count(self):
        count = 0
        for bet in self.bets:
            if bet in self.winning_numbers:
                count += 1
        return count

    def calculate_score(self,match_count: int) -> int:
        if(match_count == 0): return 0
        if(match_count == 1): return 1
        return self.calculate_score(match_count - 1) * 2

    def get_score(self):
        return self.calculate_score(self.get_match_count())

