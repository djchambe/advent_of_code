from time import perf_counter

ROUND_POINTS = {
    'A': {
        'X': 3,
        'Y': 4,
        'Z': 8
    },
    'B': {
        'X': 1,
        'Y': 5,
        'Z': 9
    },
    'C': {
        'X': 2,
        'Y': 6,
        'Z': 7
    }
}

def handler():
    start_time = perf_counter()
    total_score = 0
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            play_list = clean_line.split()
            total_score += ROUND_POINTS[play_list[0]][play_list[1]]

    answer = total_score

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()
