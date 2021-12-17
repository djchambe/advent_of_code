def evaluate_position(position, count, x_velocity, good_velocities):
    if count % 2 == 1:
        if position % count == 0:
            y_velocity = position/count + (count-1)/2
            velocity = [x_velocity, y_velocity]
            if velocity not in good_velocities:
                good_velocities.append(velocity)
    else:
        if abs(position % count) == int(count * 0.5):
            y_velocity = int(position/count + (count-1)/2)
            velocity = [x_velocity, y_velocity]
            if velocity not in good_velocities:
                good_velocities.append(velocity)
    return good_velocities

def get_y_velocities(x_velocity, x_count, y_range, last_x, good_velocities):
    max_y = max(y_range)
    min_y = min(y_range)
    for y_position in range(min_y, max_y + 1, 1):
        good_velocities = evaluate_position(y_position, x_count, x_velocity, good_velocities)
        if last_x == 1:
            for count in range(x_count + 1, abs(min_y)*2+1, 1):
                good_velocities = evaluate_position(y_position, count, x_velocity, good_velocities)

    return good_velocities

def get_velocities(x_range, y_range):
    good_velocities = []
    max_x = max(x_range)
    min_x = min(x_range)
    for x_velocity in range(max_x, 0, -1):
        x_sum = 0
        x_count = 0
        for x_delta in range(x_velocity, 0, -1):
            x_sum += x_delta
            x_count += 1
            if x_sum >= min_x and x_sum <= max_x:
                good_velocities = get_y_velocities(x_velocity, x_count, y_range, x_delta, good_velocities)

    return good_velocities

def handler():
    with open('input.txt') as input_file:
        for line in input_file:
            instructions = line.strip()
    
    split_instructions = instructions.split(' ')
    x_strings = split_instructions[-2].strip('x=,').split('..')
    y_strings = split_instructions[-1].strip('y=').split('..')
    x_range = [int(i) for i in x_strings]
    y_range = [int(j) for j in y_strings]

    answer = len(get_velocities(x_range, y_range))
    
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()