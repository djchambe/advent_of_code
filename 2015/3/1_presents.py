from time import perf_counter

DELTA = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (1, 0),
    'v': (-1, 0)
}

def handler():
    start_time = perf_counter()
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()

    houses = {(0, 0): 1}
    position_x = 0
    position_y = 0

    for direction in clean_line:
        position_x += DELTA[direction][1]
        position_y += DELTA[direction][0]
        position = (position_y, position_x)
        if position in houses:
            houses[position] += 1
        else:
            houses[position] = 1

    answer = len(houses)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()