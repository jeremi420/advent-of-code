from .game import Game

def exercise1(games: list[Game]):
    sum = 0
    for game in games:
        sum += game.get_score()
    print(sum)
