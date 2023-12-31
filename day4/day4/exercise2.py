from day4.game import Game

def exercise2(games: list[Game]):
    for index, game in enumerate(games):
        matches = game.get_match_count()
        for i in range(index + 1, index + matches + 1):
            games[i].copies += game.copies
    print(sum(list(map(lambda x: x.copies, games))))
