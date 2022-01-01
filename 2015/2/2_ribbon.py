from time import perf_counter
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
        sorted_dimensions = sorted(dimensions)
        answer += 2 * (sorted_dimensions[0] + sorted_dimensions[1]) + prod(sorted_dimensions)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()