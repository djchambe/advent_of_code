from datetime import datetime

def move(position, roll):
    position += roll
    position = position % 10
    if position == 0:
        position = 10
    
    return position

def roll_die(last_roll):
    roll_total = 0
    current_roll = last_roll
    for _ in range(3):
        current_roll += 1
        if current_roll > 100:
            current_roll = 1
        roll_total += current_roll
    
    return roll_total, current_roll

def take_turn(position, score, die_values):
    turn_total_roll, current_roll = roll_die(die_values[0])
    die_values = [current_roll, die_values[1] + 3]
    new_position = move(position, turn_total_roll)
    score += new_position

    return new_position, score, die_values

def play_dirac_dice(positions):
    scores = [0, 0]
    die_values = [0, 0]
    while scores[0] < 1000 and scores[1] < 1000:
        for index in range(len(scores)):
            positions[index], scores[index], die_values = take_turn(positions[index], scores[index], die_values)
            if scores[index] >= 1000:
                break
    
    return min(scores)*die_values[1]
    
def handler():
    print(f'Start: {datetime.now()}')
    starting_positions = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            starting_positions.append(int(clean_line.split(' ')[-1]))

    answer = play_dirac_dice(starting_positions)
    
    print(f'The answer is {answer}')
    print(f'End: {datetime.now()}')

if __name__ == '__main__':
    handler()
