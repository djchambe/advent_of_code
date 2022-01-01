from time import perf_counter
import operator

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

    houses = {(0, 0)}
    santa = (0, 0)
    robo_santa = (0, 0)

    for index, direction in enumerate(clean_line):
        if index % 2:
            robo_santa = tuple(map(operator.add, robo_santa, DELTA[direction]))
            houses.add(robo_santa)
        else:
            santa = tuple(map(operator.add, santa, DELTA[direction]))
            houses.add(santa)

    answer = len(houses)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()