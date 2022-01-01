from time import perf_counter
from itertools import combinations
from math import prod

def handler():
    start_time = perf_counter()
    presents = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            presents.append([int(value) for value in clean_line.split('x')])

    answer = 0

    for dimensions in presents:
        sides = []
        for combination in combinations(dimensions, 2):
            sides.append(prod(combination))
        answer += 2 * sum(sides) + min(sides)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()