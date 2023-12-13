# which games are possible with 12 red, 13 green, 14 blue cubes
# add up ID's of possible games


with open('input.txt', 'r') as f:
    inputPuzzle = f.read()
   
def part1(puzzle_input):

    possible = {'red': 12, 'green': 13, 'blue': 14}
    possible_games = 0
    for id, game in enumerate(puzzle_input.split('\n'), start=1):
        game = game.split(': ')[1]
        for hand in game.split('; '):
            is_impossible = False
            for subset in hand.split(', '):
                n, color = subset.split()
                if int(n) > possible[color]:
                    is_impossible = True
                    break
            if is_impossible:
                break
        else:
            possible_games += id

    return possible_games


print(part1(inputPuzzle))


