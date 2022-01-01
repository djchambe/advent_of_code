from time import perf_counter
from hashlib import md5

def handler():
    start_time = perf_counter()
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()

    answer = 0

    while True:
        answer += 1
        hash_result = md5(f'{clean_line}{answer}'.encode('utf-8')).hexdigest()
        if hash_result.startswith('00000'):
            break

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()