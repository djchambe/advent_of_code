from datetime import datetime
from itertools import product
import functools

@functools.cache
def play_dirac_dice(position_0, position_1, score_0, score_1):
    wins_0 = 0
    wins_1 = 0
    for rolls in product((1, 2, 3), repeat=3):
        new_position_0 = (position_0 + sum(rolls) - 1) % 10 + 1
        new_score_0 = score_0 + new_position_0
        if new_score_0 >= 21:
            wins_0 += 1
        else:
            future_wins_1, future_wins_0 = play_dirac_dice(
                position_1, new_position_0, score_1, new_score_0)
            wins_0 += future_wins_0
            wins_1 += future_wins_1

    return wins_0, wins_1
    
def handler():
    print(f'Start: {datetime.now()}')
    starting_positions = []
    # with open('./2021/21/input.txt') as input_file:
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            starting_positions.append(int(clean_line.split(' ')[-1]))

    answer = max(play_dirac_dice(
        starting_positions[0], starting_positions[1], 0, 0))
    
    print(f'The answer is {answer}')
    print(f'End: {datetime.now()}')

if __name__ == '__main__':
    handler()
