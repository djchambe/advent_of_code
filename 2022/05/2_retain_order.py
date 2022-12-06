from time import perf_counter
from collections import deque


def create_crates(crate_input):
    crate_numbers = crate_input.pop()
    locations = {}
    for index, character in enumerate(crate_numbers):
        if character in crate_numbers.strip().split():
            locations[character] = index
    crates = {}
    for crate_number in locations:
        crates[crate_number] = deque()
    for crate_row in crate_input:
        for crate_number, location in locations.items():
            if crate_row[location] != ' ':
                crates[crate_number].appendleft(crate_row[location])
    return crates, int(max(locations.keys()))


def move_crates(crates, raw_data):
    instructions = raw_data.split()
    to_move = deque()
    for _ in range(int(instructions[1])):
        to_move.append(crates[instructions[3]].pop())
    for _ in range(int(instructions[1])):
        crates[instructions[5]].append(to_move.pop())
    return crates


def handler():
    start_time = perf_counter()
    crate_lines = True
    crate_input = []
    crates = {}
    with open('input.txt') as input_file:
        for line in input_file:
            if line.strip():
                if crate_lines:
                    crate_input.append(line)
                else:
                    crates = move_crates(crates, line.strip())
            else:
                crate_lines = False
                crates, number_of_crates = create_crates(crate_input)

    answer = ''
    for i in range(1, number_of_crates + 1):
        answer += crates[str(i)][-1]

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')


if __name__ == '__main__':
    handler()
