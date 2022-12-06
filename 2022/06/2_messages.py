from time import perf_counter
from collections import deque


def handler():
    start_time = perf_counter()
    with open('input.txt') as input_file:
        for line in input_file:
            data_stream = line.strip()

    last_14 = deque(maxlen=14)
    for index, character in enumerate(data_stream):
        last_14.append(character)
        if len(set(last_14)) == 14:
            answer = index + 1
            break

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')


if __name__ == '__main__':
    handler()
