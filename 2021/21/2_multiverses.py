from copy import deepcopy

WEIGHTS = {
    0: 1,
    1: 3,
    2: 6,
    3: 7,
    4: 6,
    5: 3,
    6: 1
}

def move_and_score(game, index):
    position = game['positions'][index]
    position += game['roll']
    position = position % 10
    if position == 0:
        position = 10
    game['positions'][index] = position
    game['scores'][index] += position
    
    return game

def roll_die_and_move(games, wins, index):
    new_games = []
    for game in games:
        for i in range(7):
            game_roll = deepcopy(game)
            game_roll['roll'] = i + 3
            game_roll['weight'] *= WEIGHTS[i]
            game_roll = move_and_score(game_roll, index)
            if max(game_roll['scores']) >= 21:
                wins[index] += game_roll['weight']
            else:
                new_games.append(game_roll)
    
    return new_games, wins

def play_dirac_dice(positions):
    games = [
        {
            'positions': positions,
            'scores': [0, 0],
            'weight': 1,
            'roll': 0
        }
    ]
    wins = [0, 0]
    while games:
        for index in range(2):
            games, wins = roll_die_and_move(games, wins, index)
            print(f'{len(games)}, {wins}')
    return max(wins)
    
def handler():
    starting_positions = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            starting_positions.append(int(clean_line.split(' ')[-1]))

    answer = play_dirac_dice(starting_positions)
    
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()
